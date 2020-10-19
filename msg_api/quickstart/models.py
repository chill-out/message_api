from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserMessage(models.Model):
    """
    a message contains :
    1. sender (owner)
    2. receiver
    3. message
    4. subject
    5. creation date
    6. read status
    """
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='received_messages')
    message = models.TextField(null=False)
    subject = models.TextField(null=False)
    creation_date = models.TimeField(auto_now=True)
    unread = models.BooleanField(default=True)

  