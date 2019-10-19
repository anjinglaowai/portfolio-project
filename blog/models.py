
from django.db import models

from django.utils import timezone

class Blog(models.Model):
        title = models.CharField(max_length=80)
        created = models.DateTimeField(default=timezone.now)
        image = models.ImageField(upload_to='images/')
        body = models.TextField()
