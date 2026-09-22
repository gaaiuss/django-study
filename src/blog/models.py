from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f"{self.title}"
