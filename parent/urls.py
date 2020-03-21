from django.contrib import admin
from django.urls import path, include
from . views import ParentView, choice
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', ParentView.as_view(), name='signup'),
    #path('ai/', views.ai, name='ai'),
    path('login/', auth_views.LoginView.as_view(template_name='parent/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='parent/logout.html'), name='logout'),
    path('choice/', views.choice, name='choice'),
    path('stream/', views.wait, name='wait'),
    #path('videorecording/' , views.videorecording, name='video-recording'),
    path('audiorecording/', views.audiorecording, name='audio'),
    #path('mail/', views.sendmail, name='mail'),
    path('videostreaming/' , views.videostreaming, name='video-streaming'),
]

urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)