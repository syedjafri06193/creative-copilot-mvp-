from ..protocol import SuggestionItem, Action

def suggest_transitions(ctx):
    cuts = ctx.timeline.cuts or []
    if not cuts:
        return []

    # If a cut is near playhead, suggest a context-aware transition
    playhead = ctx.playhead
    near = [c for c in cuts if abs(c - playhead) < 0.6]
    if not near:
        return []

    emotion = (ctx.scene.emotion or "").lower()
    if "tense" in emotion:
        title = "Use a hard cut + 2–3 frame dip for impact"
        params = {"type": "dip_to_black", "frames": 3}
        conf = 0.72
        why = "Tension scenes often read cleaner with minimal transitions; tiny dip adds punch."
    else:
        title = "Try a 8-frame smooth cross dissolve"
        params = {"type": "cross_dissolve", "frames": 8}
        conf = 0.60
        why = "General-purpose smoothing between similar shots."

    return [SuggestionItem(
        id="",
        kind="transition",
        title=title,
        confidence=conf,
        rationale=why,
        action=Action(op="apply_transition_at_cut", params=params)
    )]
