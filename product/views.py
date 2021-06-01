from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from .models import Post , Profile , Comment
from django.contrib import messages
from .forms import  CommentForm , CreatePostForm, UpdateProfileForm , NewsLetterForm, CreateProfileForm
from .email import send_welcome_email
from django.urls import reverse_lazy
import datetime as dt
from .email import send_welcome_email
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer , PostSerializer
from rest_framework import status


# Create your views here.
def base(request):
    return render(request ,'all-products/base.html')

def main(request):
    post = request.GET.get('post')
    post = Post.objects.all()
    context = {'post': post }
    return render(request ,'all-products/main.html', context)

def details(request , pk):
    post = Post.objects.all()
    post = Post.objects.get(id=pk)
    
    profile = Profile.objects.all()
    comments = Comment.objects.all()
    context = {'post': post , 'profile': profile , 'comments': comments}
    return render(request ,'details.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('main')
    else:
        form = UserRegisterForm()
    return render(request ,'/accounts/login.html' , {'form': form})


def profile(request, username):
    
    date = dt.date.today()
    post = Post.get_post_by_user(username)
    profile = Profile.get_profile(username)

    context = {'post': post,'profile': profile, 'date': date}
    return render(request ,'profile.html' , context)

def login(request):
    return render(request ,'/registration/login.html')

def create_profile(request ):
    current_user = request.user
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
                
        return redirect('/')

    else:
        form = CreateProfileForm()
    return render(request, 'create_profile.html', {"form": form})


def edit_profile(request , username):
    user = User.objects.get(username=username)
    current_user = request.user
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        return redirect('profile', user.username)

    else:
        form = UpdateProfileForm(instance=current_user.profile)

    return render(request, 'edit_profile.html' , {"form": form})
    


def comment(request , post_id):
    current_user = request.user
    post = Post.objects.get(pk=post_id)
    content = request.GET.get("comment")   
    user = request.user
    comment = Comment(post=post,content=content,user=current_user)
    comment.save_comment()

    return redirect('main')

def create_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = CreatePostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return HttpResponseRedirect('/')
           
    else:
        form = CreatePostForm()
        return render(request, 'create_post.html', {"form": form})


def welcome_mail(request):
    user = request.user
    email = user.email
    name = user.username
    send_welcome_email(name,email)
    
    return redirect(create_profile)

def search_post(request):
    if 'keyword' in request.GET and request.GET["keyword"]:
        search_term = request.GET.get("keyword")
        searched_posts = Profile.posts(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message":message,"posts": searched_posts})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})

class ProfileList(APIView):
    def get(self, request, format=None):
        all_profile = Profile.objects.all()
        serializers = ProfileSerializer(all_profile, many=True)
        return Response(serializers.data)

class PostList(APIView):
    def get(self, request, format=None):
        all_post = Post.objects.all()
        serializers = PostSerializer(all_post, many=True)
        return Response(serializers.data)

    