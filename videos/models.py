from django.db import models

class Video(models.Model):
    video_id = models.CharField(null=False,blank=False,max_length=300)
    channel_id = models.CharField(null=False,blank=False,max_length=500)
    title = models.CharField(null=True,blank=True,max_length=600)
    channel_title = models.CharField(null=True,blank=True,max_length=500)
    created = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    thumbnailsUrls = models.URLField()
    description = models.CharField(null=True,blank=True,max_length=6000)
    publishedDateTime = models.DateTimeField()
    