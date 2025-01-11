from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name = 'blog'


urlpatterns = [
   # Authentication
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    
    # Profile
    path('profile/', views.profile, name='profile'),
    
    # Blog Posts
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    
    # Comments
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='add_comment'),  # Matches requirement
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='edit_comment'),  # Matches requirement
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='delete_comment'),  # Matches requirement
    
    path('tags/<slug:tag_slug>/', views.posts_by_tag, name='posts_by_tag'),
    path('search/', views.search_posts, name='search_posts'),
     path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view(), name='posts_by_tag'),
]
