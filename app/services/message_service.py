from app.models.message import Message
from app.repositories.message_repository import MessageRepository
from datetime import datetime, timezone
from app.workers.message_producer import send_message

class MessageService:
    def __init__(self, repository: MessageRepository):
        self.repository = repository

    def create_message(self, content: str) -> Message:
        message_id = str(len(self.repository.get_messages()) + 1)
        timestamp = datetime.now(timezone.utc).isoformat()  # Utilisation de datetime.now avec timezone UTC
        message = Message(id=message_id, content=content, timestamp=timestamp)
        self.repository.add_message(message)
        # Envoyer le message à RabbitMQ
        send_message(content)
        
        return message

    def get_all_messages(self):
        return self.repository.get_messages()
