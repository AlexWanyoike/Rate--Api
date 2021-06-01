from rest_framework import serializers
from .models import Profile , Post

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'name', 'profile_pic', 'bio' , 'contact', 'email', 'link')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ( 'id','title', 'content', 'date_posted','author','image')