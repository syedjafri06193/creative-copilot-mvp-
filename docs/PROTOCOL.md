# SENSEI Protocol (v0.1)

Transport: WebSocket JSON

## Host -> Service

### hello
{
  "type": "hello",
  "host": { "name": "mock-host", "version": "0.1" },
  "project": { "id": "p1", "fps": 24 }
}

### context_frame
{
  "type": "context_frame",
  "ts": 1730000000,
  "playhead": 12.4,
  "scene": {
    "shot_id": "A012_C003",
    "emotion": "tense",
    "lighting": "low-key",
    "notes": "night interior, neon spill"
  },
  "timeline": {
    "clips": [
      { "id": "c1", "in": 10.0, "out": 14.2, "kind": "video", "label": "Wide" }
    ],
    "cuts": [14.2],
    "audio": { "bpm": 92, "beats": [12.0, 12.65, 13.3] }
  }
}

## Service -> Host/UI

### suggestions
{
  "type": "suggestions",
  "ts": 1730000001,
  "items": [
    {
      "id": "sug_001",
      "kind": "color_grade",
      "title": "Moody teal shadows + warm highlights",
      "confidence": 0.78,
      "rationale": "Matches 'tense' emotion + neon spill lighting",
      "action": {
        "op": "apply_color_grade",
        "params": { "lut": "teal_orange_07", "sat": 0.92, "contrast": 1.1 }
      }
    }
  ]
}

## UI/Host -> Service (feedback)
{
  "type": "feedback",
  "suggestion_id": "sug_001",
  "verdict": "accepted"
}
