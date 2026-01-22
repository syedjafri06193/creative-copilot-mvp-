"""
DaVinci Resolve scripting stub.

Resolve exposes scripting via Python/Lua.
You would:
- Connect to Resolve scripting API
- Read current timeline playhead, clip metadata
- Push context frames to SENSEI service
- Apply actions: LUT, OFX, transitions, keyframe adjustments
"""

def get_timeline_context():
    # TODO: implement Resolve API calls
    return {}

def apply_action(action: dict):
    # TODO: map SENSEI action ops -> Resolve operations
    return True
