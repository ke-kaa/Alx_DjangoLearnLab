from django.urls import path
from .views import LikePostView, UnlikePostView
from .views import FeedView
urlpatterns = [
    path('posts/<int:pk>/like/', LikePostView.as_view(), name='like-post'),
    path('posts/<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),
    path('feed/', FeedView.as_view(), name='feed'),
]
