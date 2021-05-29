from django.urls import path , re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.base,name = 'base'),
    path('main',views.main,name = 'main'),
    path('details',views.details,name = 'details'),
    path('profile/',views.profile,name = 'profile'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)