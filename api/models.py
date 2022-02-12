from django.db import models
from datetime import datetime

class Achievement(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(max_length=200, blank=True, default='')

    def __str__(self):
        return f"{self.name}"


class Event(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    img = models.ImageField(upload_to='event')
    description = models.TextField(max_length=200, blank=True, default='')

    def __str__(self):
        return f"{self.name}"


class Blog(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    link = models.CharField(max_length=200, blank=True, default='')

    def __str__(self):
        return f"{self.title}"
