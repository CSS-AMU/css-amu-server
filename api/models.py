from xml.parsers.expat import model
from django.db import models
from datetime import datetime

class Achievement(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(max_length=200, blank=True, default='')

    def __str__(self):
        return f"{self.name}"


class Event(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    img = models.ImageField(upload_to='event')
    description = models.TextField(max_length=200, blank=True, default='')
    date = models.DateField()

    def __str__(self):
        return f"{self.name}"


class Publication(models.Model):
    author = models.CharField(max_length=100, blank=True, default='')
    details = models.CharField(max_length=300, blank=True, default='')
    date = models.DateField()

    def __str__(self):
        return f"{self.details}"


class Member(models.Model):
    name = models.CharField(max_length=100, default='')
    email = models.CharField(max_length=100, default='')
    course = models.CharField(max_length=100, default='')

    def __str__(self):
        return f"{self.name} : {self.course}"
