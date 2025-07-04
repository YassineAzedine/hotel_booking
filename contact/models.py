# contact/models.py
from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the message was sent

    def __str__(self):
        return f"Message from {self.name} ({self.email})"
