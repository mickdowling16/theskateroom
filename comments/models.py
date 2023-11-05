from django.db import models
from profiles.models import UserProfile
from events.models import Event
from django.utils import timezone


class Comment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    parent_comment = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE)
