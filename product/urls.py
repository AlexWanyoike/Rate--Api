from django.urls import path , re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    
    path('',views.main,name = 'main'),
    path('details/<str:pk>/',views.details,name = 'details'),
    path('profile/<username>/',views.profile,name = 'profile'),
    path('edit_profile/',views.edit_profile,name = 'edit_profile'),
    path('register',views.register,name = 'register'),
    path('create_post/',views.create_post,name = 'create_post'),
    path('create_profile/',views.create_profile,name = 'create_profile'),
    path('registration/login',views.login,name = 'login'),
    path('welcome/', views.welcome_mail, name='welcome'),
    path('search_post/', views.search_post, name='search_post'),

    re_path('comment/(?P<post_id>\d+)', views.comment, name='comment'),
    path('api/profile/', views.ProfileList.as_view()),
    path('api/post/', views.PostList.as_view())
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)