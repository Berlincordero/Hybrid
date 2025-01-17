from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
    sender = models.ForeignKey(
        User,
        related_name='chats_sent',
        on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        User,
        related_name='chats_received',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat entre {self.sender.username} y {self.receiver.username}"


class Message(models.Model):
    sender = models.ForeignKey(
        User,
        related_name='messages_sent',
        on_delete=models.CASCADE
    )
    destinatario = models.ForeignKey(
        User,
        related_name='messages_received',
        on_delete=models.CASCADE
    )
    text = models.TextField(blank=True)
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensaje de {self.sender} para {self.destinatario} a las {self.timestamp}"
