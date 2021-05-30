import datetime as dt
from django.db import models
from django.contrib.auth.models import User 
from tinymce.models import HTMLField
from django.db.models.base import Model

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE )
    name = models.CharField(max_length=30, blank=True)
    profile_pic = models.ImageField(upload_to='media/', default='')
    bio = models.TextField(blank=True, max_length=160 , default='')
    contact = models.FloatField(max_length=10 , default='') 
    email = models.EmailField(blank=False, default='')

    def __str__(self):
        return self.user.username

    @classmethod
    def get_profile(cls,username):
        profile = cls.objects.filter(user__username__icontains=username)
        return profile

    @classmethod
    def search_user(cls,username):
        return User.objects.filter(username = username)

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(max_length=160)
    #date_posted = models.DateTimeField(auto_now_add=True, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    author = models.CharField(max_length=30)
    image = models.ImageField(upload_to='media/')
    rating = models.ManyToManyField(Profile, related_name="posts")
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE , null=True, default='')

    def __str__(self):
        return self.title

    def __str__(self):
        return self.author


    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_caption(self, new_caption):
        self.caption = new_caption
        self.save()

    def like_count(self):
        return self.likes.count()

    @classmethod
    def get_post_by_user(cls,username):
        post = cls.objects.filter(user__username__contains=username)
        return post 

    # class Meta:
    #     ordering = ['-date_posted']

class Comment(models.Model):
    content = models.TextField(max_length=300, default='')
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return self.content

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def get_post_comments(cls,post):
        return cls.objects.filter(post =post)

   
