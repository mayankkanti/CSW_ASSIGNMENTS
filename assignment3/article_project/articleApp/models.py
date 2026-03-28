from django.db import models
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
