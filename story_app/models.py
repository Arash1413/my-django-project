from django.db import models

class Story(models.Model):
    title = models.CharField(max_length=50, null=True)
    author = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title

# Create your models here.
