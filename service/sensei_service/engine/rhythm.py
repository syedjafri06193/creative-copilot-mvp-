from ..protocol import SuggestionItem, Action

def suggest_rhythm_keyframes(ctx):
    audio = ctx.timeline.audio
    if not audio or not audio.beats:
        return []

    # Find nearest beat to playhead and suggest snapping an upcoming keyframe
    playhead = ctx.playhead
    nearest = min(audio.beats, key=lambda b: abs(b - playhead))
    return [SuggestionItem(
        id="",
        kind="keyframe",
        title=f"Snap next keyframe to nearest beat @ {nearest:.2f}s",
        confidence=0.70,
        rationale="Rhythmic alignment increases perceived polish (especially for motion text / speed ramps).",
        action=Action(op="snap_keyframe_to_time", params={
            "time": nearest,
            "target": "next_keyframe"
        })
    )]
