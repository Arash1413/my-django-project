from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Story_v2
from .serializers import StorySerializer
from .services import generate_story_continuation
from django.http import Http404

class StoryListApiView(APIView):
    def get(self, request, *args, **kwargs):
        stories = Story_v2.objects.all()
        seializer = StorySerializer(stories, many=True)

        return Response(seializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = StorySerializer(data=request.data)
        if serializer.is_valid():
           
            validated_data = serializer.validated_data
            user_prompt = validated_data.get('user_prompt')

            
            try:
                ai_text = generate_story_continuation(user_prompt)
            except Exception as e:
               
                return Response(
                    {"error": "Failed to generate story from AI service."},
                    status=status.HTTP_503_SERVICE_UNAVAILABLE
                )

            
            story_data = {
                'user_prompt': user_prompt,
                'ai_generated_story': ai_text,
               
            }
            
            
            story_instance = Story_v2.objects.create(**story_data)
            
            
            response_serializer = StorySerializer(story_instance)
            
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
class StoryDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Story_v2.objects.get(pk=pk)
        except Story_v2.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        story = self.get_object(pk)
        serializer = StorySerializer(story)
        return Response(serializer.data)
    
    
    def put(self, request, pk):
        story = self.get_object(pk)
        if story:
            serializer = StorySerializer(story, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    
    def delete(self, request, pk):
        story = self.get_object(pk)
        story.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


# Create your views here.
