
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_video/', views.search_youtube_videos, name="get_video"),
]
