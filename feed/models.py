from django.db import models
from django.utils import timezone

# Create your models here.

class Entry(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    number = models.CharField(max_length=15)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
