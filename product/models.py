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
    bio = models.TextField(blank=True, max_length=160)
    contact = models.FloatField(max_length=10) 
    email = models.EmailField(blank=False)

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
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.CharField(max_length=30)
    image = models.ImageField(upload_to='media/')
    rating = models.ManyToManyField(Profile, related_name="posts")
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE , null=True)

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

    class Meta:
        ordering = ['-date_posted']
