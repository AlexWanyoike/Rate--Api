from django import forms
from .models import Post , Profile , Comment
from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserRegisterForm , CommentForm

# class UserRegisterForm(forms.ModelForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

class CommentForm(forms.ModelForm ):
    
    class Meta:
        model = Comment
        fields = ['user', 'post', 'content']

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['profile', 'date_posted ' , 'rating', 'user']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
