from fastapi import APIRouter, Depends
from app.services.message_service import MessageService
from app.repositories.message_repository import MessageRepository
from app.models.message import Message
from typing import List

router = APIRouter()

message_repository = MessageRepository()
message_service = MessageService(repository=message_repository)

@router.post("/message/", response_model=Message)
def create_message(content: str):
    return message_service.create_message(content=content)

@router.get("/messages/", response_model=List[Message])
def get_messages():
    return message_service.get_all_messages()
