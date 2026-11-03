"""Deterministic candidate quotas; targets never override verified difficulty."""
from fractions import Fraction


def allocate(total, weights):
    if type(total) is not int or total < 0 or not weights or any(type(w) is not int or w < 0 for w in weights.values()) or not sum(weights.values()):
        raise ValueError("allocation needs a nonnegative total and nonnegative integer weights")
    shares = {key: Fraction(total * value, sum(weights.values())) for key, value in weights.items()}
    result = {key: int(value) for key, value in shares.items()}
    order = sorted(weights, key=lambda key: -(shares[key] - result[key]))
    for key in order[:total - sum(result.values())]:
        result[key] += 1
    return result


def modality_quotas(total, difficulty_weights=None, visual_percent=70):
    if type(visual_percent) is not int or not 0 <= visual_percent <= 100:
        raise ValueError("visual_percent must be 0..100")
    levels = allocate(total, difficulty_weights or {"easy": 3, "medium": 4, "hard": 3})
    visual_total = allocate(total, {"visual": visual_percent, "text": 100 - visual_percent})["visual"]
    visual = allocate(visual_total, levels) if total else dict.fromkeys(levels, 0)
    return {level: {"visual": visual[level], "text": count - visual[level]} for level, count in levels.items()}
