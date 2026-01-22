# Architecture

## Components
1. Host Adapter
   - Connects to NLE/Mograph host (Premiere, AE, Resolve, Blender)
   - Extracts timeline context: clips, cuts, metadata, audio features
   - Applies actions: transitions, color presets, keyframe edits, VFX params

2. SENSEI Service (FastAPI)
   - Receives context over WebSocket
   - Produces ranked suggestions & action payloads
   - (Future) Pluggable model backends: local LLM/VLM, remote APIs, hybrid

3. Copilot Desktop (Electron)
   - Shows suggestions in realtime
   - Lets user accept, tweak, apply
   - Captures feedback to improve suggestions

## Data flow
Host -> context frames/events -> Service -> suggestions -> UI -> user apply -> Host

## Key design choices
- WebSocket JSON protocol (simple MVP)
- Host adapters are swappable via a shared protocol
- "Apply" operations are idempotent with action IDs and host-side guards
