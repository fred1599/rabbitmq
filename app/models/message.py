from pydantic import BaseModel

class Message(BaseModel):
    id: str
    content: str
    timestamp: str
