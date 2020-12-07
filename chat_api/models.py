from django.db import models

# Create your models here.


class Message(models.Model):

    name = models.TextField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
