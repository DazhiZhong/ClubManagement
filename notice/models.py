from django.db import models

# Create your models here.

class Notice(models.Model):

    notice = models.TextField()

    def __str__(self):
        return notice

