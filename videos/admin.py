from django.contrib import admin
from videos.models import *

# Register your models here.
class VideoAdmin(admin.ModelAdmin):
    list_display = ('video_id','publishedDateTime','title','description')

admin.site.register(Video,VideoAdmin)