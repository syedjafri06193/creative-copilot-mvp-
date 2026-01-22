# Adobe Bridge (Stub)

Goal: connect SENSEI to Premiere Pro / After Effects.

Two common pathways:
- CEP (legacy panels) — easiest for quick prototypes in older environments
- UXP (newer extensibility) — preferred long-term

This folder contains stubs to establish:
1) UI panel shell
2) A bridge process that can talk to SENSEI service via WebSocket
3) A thin "host API" wrapper to read timeline state & apply actions

Next steps:
- Define the minimal timeline schema you can extract reliably from Adobe APIs
- Implement `getTimelineContext()` and `applyAction(action)`
