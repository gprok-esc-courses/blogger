from django.db import models
from django.conf import settings


class Blogpost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=50, unique=True)
    content = models.TextField(blank=True)
    published = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             null=True)

    def __str__(self):
        return self.title
