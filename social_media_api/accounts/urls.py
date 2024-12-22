from django.urls import path
from . import views

urlpatterns = [
    # Routes for user authentication
    path('register/', views.register, name='register'),  # Registration route
    path('login/', views.login_user, name='login'),      # Login route
    path('profile/', views.profile, name='profile'),    # User profile management route

    # Existing routes
    path('follow/<int:user_id>/', views.follow_user, name='follow-user'),
    path('unfollow/<int:user_id>/', views.unfollow_user, name='unfollow-user'),
]
