import time
import uuid
from .color import suggest_color
from .rhythm import suggest_rhythm_keyframes
from .vfx import suggest_vfx
from .transitions import suggest_transitions
from ..protocol import SuggestionsMsg

def build_suggestions(context) -> SuggestionsMsg:
    items = []
    items += suggest_color(context)
    items += suggest_transitions(context)
    items += suggest_rhythm_keyframes(context)
    items += suggest_vfx(context)

    # ensure unique ids
    for it in items:
        if not it.id:
            it.id = f"sug_{uuid.uuid4().hex[:8]}"
    return SuggestionsMsg(ts=int(time.time()), items=items)
