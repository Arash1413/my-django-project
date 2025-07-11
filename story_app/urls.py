from django.urls import path
from .views import StoryListCreatApiView, StoryDetailAPIView

urlpatterns = [
    path("stories/", StoryListCreatApiView.as_view()),
    path("stories/<int:pk>/", StoryDetailAPIView.as_view())
]