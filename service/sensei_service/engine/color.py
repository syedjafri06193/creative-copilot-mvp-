from ..protocol import SuggestionItem, Action

def suggest_color(ctx):
    emotion = (ctx.scene.emotion or "").lower()
    lighting = (ctx.scene.lighting or "").lower()
    items = []

    if "tense" in emotion or "noir" in lighting or "low-key" in lighting:
        items.append(SuggestionItem(
            id="",
            kind="color_grade",
            title="Moody teal shadows + warm highlights",
            confidence=0.78,
            rationale="Tension + low-key lighting benefits from cooler shadows and controlled warmth.",
            action=Action(op="apply_color_grade", params={
                "lut": "teal_orange_07",
                "contrast": 1.10,
                "sat": 0.92,
                "shadow_tint": "teal",
                "highlight_tint": "warm"
            })
        ))
    else:
        items.append(SuggestionItem(
            id="",
            kind="color_grade",
            title="Balanced filmic grade (soft highlights)",
            confidence=0.62,
            rationale="A safe filmic baseline when emotion/lighting is neutral.",
            action=Action(op="apply_color_grade", params={
                "lut": "filmic_neutral_03",
                "contrast": 1.05,
                "sat": 1.00
            })
        ))
    return items
