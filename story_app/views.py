from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Story
from .serializer import StorySerializer
from django.http import Http404



class StoryListCreatApiView(APIView):
    def get(self, request, *args, **kwargs):
        stories = Story.objects.all()
        serializer = StorySerializer(stories, many=True)   
        return Response(serializer.data)
    

    
    def post(self, request, *args, **kwargs):
        serializer = StorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class StoryDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Story.objects.get(pk=pk)
        except Story.DoesNotExist:
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
