from django.test import TestCase
from .models import Profile , Post, Comment 
from django.contrib.auth.models import User
# Create your tests here.

class ProfileTestClass(TestCase):

    def setUp(self):
        self.user = User(id=1, username='alex', password='1234')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()


class PostTestClass (TestCase):
    def setUp(self):
        self.post = Post.objects.create(post_title='test post',
        post_image='png', post_description='bio',)

   
    
