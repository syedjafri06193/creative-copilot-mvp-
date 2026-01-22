from typing import Literal, Optional, Any
from pydantic import BaseModel, Field

class HostInfo(BaseModel):
    name: str
    version: str

class ProjectInfo(BaseModel):
    id: str
    fps: float

class HelloMsg(BaseModel):
    type: Literal["hello"]
    host: HostInfo
    project: ProjectInfo

class SceneCtx(BaseModel):
    shot_id: str
    emotion: Optional[str] = None
    lighting: Optional[str] = None
    notes: Optional[str] = None

class Clip(BaseModel):
    id: str
    in_: float = Field(alias="in")
    out: float
    kind: Literal["video", "audio"]
    label: Optional[str] = None

class AudioInfo(BaseModel):
    bpm: Optional[float] = None
    beats: list[float] = []

class TimelineCtx(BaseModel):
    clips: list[Clip] = []
    cuts: list[float] = []
    audio: Optional[AudioInfo] = None

class ContextFrameMsg(BaseModel):
    type: Literal["context_frame"]
    ts: int
    playhead: float
    scene: SceneCtx
    timeline: TimelineCtx

class FeedbackMsg(BaseModel):
    type: Literal["feedback"]
    suggestion_id: str
    verdict: Literal["accepted", "rejected", "modified"]
    notes: Optional[str] = None

InboundMsg = HelloMsg | ContextFrameMsg | FeedbackMsg

class Action(BaseModel):
    op: str
    params: dict[str, Any] = {}

class SuggestionItem(BaseModel):
    id: str
    kind: Literal["color_grade", "transition", "keyframe", "vfx"]
    title: str
    confidence: float
    rationale: str
    action: Action

class SuggestionsMsg(BaseModel):
    type: Literal["suggestions"] = "suggestions"
    ts: int
    items: list[SuggestionItem]
