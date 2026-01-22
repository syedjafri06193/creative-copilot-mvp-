import React, { useEffect, useMemo, useState } from "react";
import SuggestionCard from "./components/SuggestionCard";

type Suggestion = {
  id: string;
  kind: string;
  title: string;
  confidence: number;
  rationale: string;
  action: { op: string; params: Record<string, any> };
};

export default function App() {
  const [items, setItems] = useState<Suggestion[]>([]);
  const wsUrl = useMemo(() => "ws://localhost:8000/ws/host", []);

  useEffect(() => {
    // UI can connect directly for demo; in production it would subscribe via a local bridge.
    const ws = new WebSocket(wsUrl);

    ws.onopen = () => {
      ws.send(JSON.stringify({
        type: "hello",
        host: { name: "copilot-ui", version: "0.1" },
        project: { id: "ui-session", fps: 24 }
      }));
    };

    ws.onmessage = (evt) => {
      try {
        const msg = JSON.parse(evt.data);
        if (msg.type === "suggestions") {
          setItems(msg.items);
        }
      } catch {}
    };

    return () => ws.close();
  }, [wsUrl]);

  return (
    <div style={{ padding: 18, fontFamily: "system-ui" }}>
      <h1 style={{ margin: 0 }}>SENSEI</h1>
      <p style={{ marginTop: 6, opacity: 0.75 }}>
        Real-time creative copilot — suggestions stream in as your timeline context changes.
      </p>

      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 12 }}>
        {items.map((s) => (
          <SuggestionCard key={s.id} s={s} />
        ))}
      </div>
    </div>
  );
}
