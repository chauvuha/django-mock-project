from enum import auto
from django.db import models

# Create your models here.

class Note(models.Model):
    body = models.TextField(null=True, blank=True)
    # autonow is automatically going to update the time when we save the note
    updated = models.DateTimeField(auto_now=True)
    # auto_now_add only takes the first time when we create
    created = models.DateTimeField(auto_now_add=True)

    # a string representation of the class, it will just be the body attribute.
    def __str__(self):
        return self.body[0:50]