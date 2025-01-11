from django import forms
from .models import Post, Comment
from taggit.forms import TagWidget  # Explicitly import TagWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Include tags
        widgets = {
            'tags': TagWidget(),  # Explicitly use TagWidget here
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
