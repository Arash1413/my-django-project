from rest_framework import serializers
from .models import Story_v2

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story_v2
        fields = ('id', 'title', 'user_prompt', 'ai_generated_story', 'created_at')
        read_only_fields = ('ai_generated_story', 'created_at') 