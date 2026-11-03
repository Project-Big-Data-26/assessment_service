"""Deterministic mathematical diagrams: bounded specs, SVG source and PNG input.

Specs describe visible facts only. They never supply a verified answer key.
"""
import hashlib
from html import escape
import json
from pathlib import Path
from typing import Literal

from PIL import Image, ImageDraw, ImageFont
from pydantic import BaseModel, ConfigDict, Field, model_validator

from .workflow import atomic_json, digest


class VisualGroup(BaseModel):
    model_config = ConfigDict(extra="forbid")
    label: str = Field(pattern=r"^[A-Z]$", description="group identifier, not its count")
    shape: Literal["circle", "square", "triangle"]
    count: int = Field(ge=1, le=20)


class VisualSpec(BaseModel):
    model_config = ConfigDict(extra="forbid")
    kind: Literal["object_groups", "shape_pattern", "clock"]
    groups: list[VisualGroup] = Field(default_factory=list, max_length=3)
    pattern: list[Literal["circle", "square", "triangle", "?"]] = Field(default_factory=list, max_length=12)
    hour: int | None = Field(default=None, ge=0, le=11)
    minute: int | None = Field(default=None, ge=0, le=55, multiple_of=5)

    @model_validator(mode="after")
    def check_kind(self):
        if self.kind == "object_groups":
            if not self.groups or len({g.label for g in self.groups}) != len(self.groups):
                raise ValueError("object groups need unique group labels")
            if self.pattern or self.hour is not None or self.minute is not None:
                raise ValueError("object groups cannot contain clock/pattern fields")
        elif self.kind == "shape_pattern":
            if not 4 <= len(self.pattern) <= 12 or self.pattern.count("?") != 1:
                raise ValueError("a pattern needs 4..12 entries and exactly one unknown")
            if self.groups or self.hour is not None or self.minute is not None:
                raise ValueError("pattern cannot contain groups/clock fields")
        elif self.hour is None or self.minute is None or self.groups or self.pattern:
            raise ValueError("a clock needs hour and minute only")
        return self


def render(spec, base):
    """Render semantic primitives to both formats with the same coordinates."""
    import math
    spec = VisualSpec.model_validate(spec)
    payload = spec.model_dump(mode="json")
    spec_hash = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
    assets = Path(base) / "assets"
    assets.mkdir(parents=True, exist_ok=True)
    prefix = assets / spec_hash[:24]
    width, height = (760, 140 + len(spec.groups) * 200) if spec.kind == "object_groups" else (760, 460)
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default(size=28)
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
           '<rect width="100%" height="100%" fill="white"/>']

    def text(x, y, value):
        draw.text((x, y), value, fill="#172033", font=font, anchor="mm")
        svg.append(f'<text x="{x}" y="{y}" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="28" fill="#172033">{escape(value)}</text>')

    def line(x1, y1, x2, y2, thickness=4):
        draw.line((x1, y1, x2, y2), fill="#172033", width=thickness)
        svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#172033" stroke-width="{thickness}"/>')

    def shape(x, y, kind):
        fill, outline, radius = "#d6e7fa", "#172033", 20
        if kind == "circle":
            draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill=fill, outline=outline, width=3)
            svg.append(f'<circle cx="{x}" cy="{y}" r="20" fill="{fill}" stroke="{outline}" stroke-width="3"/>')
        elif kind == "square":
            draw.rectangle((x-radius, y-radius, x+radius, y+radius), fill=fill, outline=outline, width=3)
            svg.append(f'<rect x="{x-radius}" y="{y-radius}" width="40" height="40" fill="{fill}" stroke="{outline}" stroke-width="3"/>')
        elif kind == "triangle":
            points = [(x, y-22), (x-23, y+20), (x+23, y+20)]
            draw.polygon(points, fill=fill)
            draw.line([*points, points[0]], fill=outline, width=3)
            svg.append(f'<polygon points="{x},{y-22} {x-23},{y+20} {x+23},{y+20}" fill="{fill}" stroke="{outline}" stroke-width="3"/>')
        else:
            text(x, y, "?")

    if spec.kind == "object_groups":
        for index, group in enumerate(spec.groups):
            y = 100 + index * 200
            text(42, y + 30, group.label)
            for n in range(group.count):
                shape(110 + n % 10 * 65, y + n // 10 * 65, group.shape)
    elif spec.kind == "shape_pattern":
        for n, value in enumerate(spec.pattern):
            shape(90 + n % 6 * 112, 155 + n // 6 * 125, value)
    else:
        cx, cy, radius = 380, 225, 175
        draw.ellipse((cx-radius, cy-radius, cx+radius, cy+radius), outline="#172033", width=4)
        svg.append(f'<circle cx="{cx}" cy="{cy}" r="{radius}" fill="white" stroke="#172033" stroke-width="4"/>')
        for n in range(1, 13):
            angle = math.radians(n * 30 - 90)
            text(round(cx + 145*math.cos(angle)), round(cy + 145*math.sin(angle)), str(n))
        for degrees, length, thickness in ((spec.minute * 6 - 90, 120, 5),
                                            (spec.hour * 30 + spec.minute / 2 - 90, 82, 9)):
            angle = math.radians(degrees)
            line(cx, cy, round(cx+length*math.cos(angle)), round(cy+length*math.sin(angle)), thickness)
    svg.append("</svg>")
    png = prefix.with_suffix(".png")
    source = prefix.with_suffix(".svg")
    # Content-addressed assets are immutable and can be reused on resume.
    svg_text = "\n".join(svg)
    if source.exists() and source.read_text(encoding="utf-8") != svg_text:
        raise ValueError("immutable visual SVG differs")
    if not source.exists():
        source.write_text(svg_text, encoding="utf-8")
    from io import BytesIO
    stream = BytesIO()
    image.save(stream, format="PNG")
    pixels = stream.getvalue()
    if png.exists() and png.read_bytes() != pixels:
        raise ValueError("immutable visual PNG differs")
    if not png.exists():
        png.write_bytes(pixels)
    provenance = {"source": "generated_svg", "rendererVersion": "math-diagrams-v1", "semanticSpec": payload,
                  "specHash": spec_hash, "pngSha256": digest(png), "svgSha256": digest(source),
                  "visualEssentialStatus": "pending_independent_validation", "width": width, "height": height}
    metadata = prefix.with_suffix(".json")
    if metadata.exists() and json.loads(metadata.read_text(encoding="utf-8")) != provenance:
        raise ValueError("immutable visual provenance differs")
    if not metadata.exists():
        atomic_json(metadata, provenance)
    return png.relative_to(base).as_posix(), provenance
