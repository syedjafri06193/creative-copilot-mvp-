import json
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from .protocol import InboundMsg, HelloMsg, ContextFrameMsg
from .engine.suggest import build_suggestions

app = FastAPI(title="SENSEI Service", version="0.1.0")

@app.get("/health")
def health():
    return {"ok": True}

@app.websocket("/ws/host")
async def ws_host(ws: WebSocket):
    await ws.accept()
    last_ctx = None
    try:
        while True:
            raw = await ws.receive_text()
            data = json.loads(raw)

            msg_type = data.get("type")
            if msg_type == "hello":
                HelloMsg.model_validate(data)  # validates
                await ws.send_text(json.dumps({"type": "ack", "ok": True}))
                continue

            if msg_type == "context_frame":
                last_ctx = ContextFrameMsg.model_validate(data)
                suggestions = build_suggestions(last_ctx)
                await ws.send_text(suggestions.model_dump_json())
                continue

            if msg_type == "feedback":
                # accept feedback (store later)
                await ws.send_text(json.dumps({"type": "ack_feedback", "ok": True}))
                continue

            await ws.send_text(json.dumps({"type": "error", "message": "unknown msg type"}))
    except WebSocketDisconnect:
        return
