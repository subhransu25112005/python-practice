# logic.py
# Advanced psychological emotion analyzer

from collections import defaultdict

# Emotion categories used across the system
PRIMARY_EMOTIONS = [
    "anxiety",
    "overthinking",
    "self_doubt",
    "anger",
    "emotional_dependency",
    "emotional_instability",
    "withdrawal",
    "avoidance",
    "confusion",
    "dependency",
    "self_criticism",
]

POSITIVE_TRAITS = [
    "balanced",
    "growth_mindset",
    "resilience",
    "emotional_regulation",
    "self_acceptance",
]

def analyze_emotion(answers):
    """
    answers: list of dicts
    example: [{"anxiety":2, "overthinking":1}, {"balanced":2}]
    """

    score = defaultdict(int)

    # Aggregate scores
    for ans in answers:
        for trait, value in ans.items():
            score[trait] += value

    # Separate negative and positive traits
    negative_scores = {k: v for k, v in score.items() if k in PRIMARY_EMOTIONS}
    positive_scores = {k: v for k, v in score.items() if k in POSITIVE_TRAITS}

    # Detect dominant emotion
    dominant_emotion = max(negative_scores, key=negative_scores.get) if negative_scores else "balanced"

    # Detect secondary traits (top 2 excluding dominant)
    secondary = sorted(
        negative_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )
    secondary_traits = [s[0] for s in secondary if s[0] != dominant_emotion][:2]

    # Mental balance index (simple but meaningful)
    positive_total = sum(positive_scores.values())
    negative_total = sum(negative_scores.values())

    if negative_total == 0:
        balance_index = 100
    else:
        balance_index = round((positive_total / (positive_total + negative_total)) * 100)

    return {
        "dominant_emotion": dominant_emotion,
        "secondary_traits": secondary_traits,
        "positive_traits": positive_scores,
        "negative_traits": negative_scores,
        "mental_balance_index": balance_index
    }
