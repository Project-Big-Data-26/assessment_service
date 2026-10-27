"""Private key slots shared by settings loaders and the exercise runner."""
from contextlib import contextmanager
import os


def _value(name, values):
    return str(os.environ.get(name, values.get(name) or "")).strip()


def _keys(provider, values):
    prefix = provider.upper() + "_API_KEY"
    # The unsuffixed name remains an alias for slot 1. Process variables win
    # over file aliases, including an explicitly empty process value.
    if os.environ.get(prefix + "_1", "").strip():
        first = _value(prefix + "_1", values)
    elif prefix + "_1" in os.environ:
        first = _value(prefix, values)
    elif prefix in os.environ:
        first = _value(prefix, values)
    else:
        first = str(values.get(prefix + "_1") or values.get(prefix) or "").strip()
    keys = {1: first}
    if provider in ("gemini", "groq"):
        keys.update({slot: _value(f"{prefix}_{slot}", values) for slot in (2, 3)})
    return keys


def credential_slots(provider, values):
    """Return nonempty, distinct slot numbers, never secret key values."""
    seen, slots = set(), []
    for slot, key in _keys(provider, values).items():
        if key and key not in seen:
            slots.append(slot)
            seen.add(key)
    return slots


def selected_api_key(provider, values):
    keys = _keys(provider, values)
    selected = os.getenv(f"EXERCISE_{provider.upper()}_KEY_SLOT")
    if selected is None:
        slots = credential_slots(provider, values)
        return keys[slots[0]] if slots else ""
    if selected not in ("1", "2", "3") or int(selected) not in keys or not keys[int(selected)]:
        raise ValueError(f"{provider} credential slot is invalid or empty")
    return keys[int(selected)]


@contextmanager
def use_credential_slot(provider, slot):
    """Only a non-secret slot number is inherited by child workers."""
    name = f"EXERCISE_{provider.upper()}_KEY_SLOT"
    previous = os.environ.get(name)
    os.environ[name] = str(slot)
    try:
        yield
    finally:
        if previous is None:
            os.environ.pop(name, None)
        else:
            os.environ[name] = previous
