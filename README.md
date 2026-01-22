# SENSEI — AI Copilot for Editing + Motion Graphics

SENSEI connects to professional editing and motion-graphics software to provide real-time creative suggestions,
automation, and intelligent enhancements:
- Emotion-aware color grade suggestions
- Context-aware transitions
- Rhythm-synced keyframe snapping to soundtrack beats
- Shot-aware VFX preset recommendations

## Monorepo Layout
- `service/` — FastAPI realtime suggestion engine (WebSocket)
- `apps/copilot-desktop/` — Electron + React desktop UI
- `adapters/` — Host integrations (mock host included)

## Quickstart (Demo)
Requirements: Node 18+, Python 3.11+

### 1) Start AI service + mock host
```bash
docker-compose up --build
