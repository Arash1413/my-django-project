from django.urls import path
from .views import StoryListApiView, StoryDetailAPIView

urlpatterns = [
    path('stories2/', StoryListApiView.as_view()),
    path("stories2/<int:pk>/", StoryDetailAPIView.as_view())
]