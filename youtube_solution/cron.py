from videos.models import Video
import requests
from datetime import datetime, timedelta
import logging
logger = logging.getLogger(__name__)

from django_cron import CronJobBase, Schedule

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1 # every 1 minute

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'youtube_solution.cron.fill_data_in_video_model'    # a unique code
   
    def do(self):
        time_now = datetime.now()
        last_request_time = time_now - timedelta(minutes=1)
        url='https://youtube.googleapis.com/youtube/v3/search'
        payload={'part': 'snippet',
        'order': 'date',
        'q': 'india',
        'maxResults': 1,
        'key':'AIzaSyDMO4xx23T-8SAFPXJrWZGtTIZNXzBg3HQ',
        'publishedAfter':(last_request_time.replace(microsecond=0).isoformat()+'Z')
           }
        res=requests.get(url, params=payload, verify=False).json()
        if res.get('items'):
            for item in res['items']:
                video_id = item['id']['videoId']
                thumbnailsUrls = item['snippet']['thumbnails']['default']['url']
                channel_id = item['snippet']['channelId']
                publishedDateTime = item['snippet']['publishedAt']
                channel_title = item['snippet']['channelTitle']
                title = item['snippet']['title']
                description = item['snippet']['description']
                
                Video.objects.create(
                    video_id=video_id,
                    title=title,
                    thumbnailsUrls=thumbnailsUrls,
                    created=datetime.now(),
                    description=description,
                    channel_id=channel_id,
                    channel_title=channel_title,
                    publishedDateTime=publishedDateTime
                )
