from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Real-Time Event Monitor API",
    version="0.1.0",
)

class EventCreate(BaseModel):
    type: str
    message: str
    severity: str

events = []


@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/events")
def list_events():
    return events

@app.post("/events")
def create_event(event: EventCreate):
    new_event = {
        "id": len(events)+1,
        "type": event.type,
        "message": event.message,
        "severity": event.severity,
    }
    events.append(new_event)
    
    return new_event
