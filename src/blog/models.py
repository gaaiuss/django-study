from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        # https://docs.djangoproject.com/en/6.1/ref/models/options/
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    categoty = models

    def __str__(self) -> str:
        return self.title
