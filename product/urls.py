from django.urls import path , re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    #path('',views.base,name = 'base'),
    path('',views.main,name = 'main'),
    path('details/<str:pk>/',views.details,name = 'details'),
    path('profile/<username>/',views.profile,name = 'profile'),
    path('edit_profile/',views.edit_profile,name = 'edit_profile'),
    path('register',views.register,name = 'register'),
    path('create_post/',views.create_post,name = 'create_post'),
    path('registration/login',views.login,name = 'login'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)