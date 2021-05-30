from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from .models import Post , Profile , Comment
from django.contrib import messages
from .forms import  CommentForm , CreatePostForm
from .email import send_welcome_email


# Create your views here.
def base(request):
    return render(request ,'all-products/base.html')

def main(request):
    post = request.GET.get('post')
    post = Post.objects.all()
    
    context = {'post': post }
    return render(request ,'all-products/main.html', context)

def details(request):
    post = Post.objects.all()
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

def edit_profile(request):
    return render(request ,'edit_profile.html')


def comment(request , post_id):
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
        return HttpResponseRedirect('/main')
           
    else:
        form = CreatePostForm()
        return render(request, 'create_post.html', {"form": form})
    
    