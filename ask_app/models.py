from django.db import models

class Story_v2(models.Model):
    title = models.CharField(max_length=200)
    user_prompt = models.TextField()
    ai_generated_story = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Create your models here.
