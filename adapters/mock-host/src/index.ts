import WebSocket from "ws";
import { makeFrame } from "./timeline.js";

const url = process.env.SENSEI_WS_URL ?? "ws://localhost:8000/ws/host";
const ws = new WebSocket(url);

ws.on("open", () => {
  ws.send(JSON.stringify({
    type: "hello",
    host: { name: "mock-host", version: "0.1" },
    project: { id: "p1", fps: 24 }
  }));

  let playhead = 11.5;
  setInterval(() => {
    playhead += 0.25;
    ws.send(JSON.stringify(makeFrame(playhead)));
  }, 500);
});

ws.on("message", (buf) => {
  const msg = buf.toString();
  console.log("[service]", msg);
});

ws.on("error", (e) => console.error(e));
