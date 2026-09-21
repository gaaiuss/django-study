from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f"{self.title}"
