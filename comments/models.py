from django.db import models
from django.contrib.auth.models import User 
from profiles.models import UserProfile
from events.models import Event


class Comment(models.Model):
    # Use UserProfile instead of User
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    # Adjust this based on your Event model
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.user.username} on {self.event.title}'
