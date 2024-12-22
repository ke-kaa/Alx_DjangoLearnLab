from rest_framework import status, generics
from rest_framework import permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post, Like
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType


class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        
        # Get or create the like (avoids duplication)
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            return Response({"detail": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create a notification only if the like is newly created
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb="liked your post",
            target=post
        )

        return Response({"detail": "Post liked."}, status=status.HTTP_200_OK)


class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        like = Like.objects.filter(user=request.user, post=post).first()

        if not like:
            return Response({"detail": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        like.delete()
        return Response({"detail": "Post unliked."}, status=status.HTTP_200_OK)
    
from rest_framework import viewsets
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    ViewSet for CRUD operations on Post model.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically set the author to the logged-in user when creating a post
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for CRUD operations on Comment model.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically set the author to the logged-in user when creating a comment
        serializer.save(author=self.request.user)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer


class FeedView(APIView):
    """
    Generates a feed of posts from users the current user follows.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Get the list of users the current user follows
        following_users = request.user.following.all()  # Assumes a ManyToManyField named 'following'
        
        # Filter posts authored by the followed users and order them by creation date (most recent first)
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        
        # Serialize the posts and return as a response
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
