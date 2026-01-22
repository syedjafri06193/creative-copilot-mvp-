export type ContextFrame = {
  type: "context_frame";
  ts: number;
  playhead: number;
  scene: { shot_id: string; emotion?: string; lighting?: string; notes?: string };
  timeline: {
    clips: Array<{ id: string; in: number; out: number; kind: "video" | "audio"; label?: string }>;
    cuts: number[];
    audio: { bpm?: number; beats: number[] };
  };
};

export function makeFrame(playhead: number): ContextFrame {
  const beats = Array.from({ length: 16 }, (_, i) => 10 + i * 0.65);

  return {
    type: "context_frame",
    ts: Math.floor(Date.now() / 1000),
    playhead,
    scene: {
      shot_id: "A012_C003",
      emotion: playhead % 8 > 4 ? "tense" : "neutral",
      lighting: "low-key",
      notes: "night interior, neon spill"
    },
    timeline: {
      clips: [{ id: "c1", in: 10.0, out: 14.2, kind: "video", label: "Wide" }],
      cuts: [14.2],
      audio: { bpm: 92, beats }
    }
  };
}
