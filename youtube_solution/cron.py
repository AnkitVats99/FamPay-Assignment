from videos.models import Video
import requests
from datetime import datetime, timedelta

def fill_data_in_video_model():
    time_now = datetime.now()
    last_request_time = time_now - timedelta(minutes=5)
    url='https://youtube.googleapis.com/youtube/v3/search'
    payload={'part': 'snippet',
    'order': 'date',
    'q': 'c++',
    'maxResults': 1,
    'key':'AIzaSyDMO4xx23T-8SAFPXJrWZGtTIZNXzBg3HQ',
    'publishedAfter':(last_request_time.replace(microsecond=0).isoformat()+'Z')
       }
    res=requests.get(url, params=payload, verify=False).json()
    for item in res['items']:
        video_id = item['id']['videoId']
        publishedDateTime = item['snippet']['publishedAt']
        title = item['snippet']['title']
        description = item['snippet']['description']
        thumbnailsUrls = item['snippet']['thumbnails']['default']['url']
        channel_id = item['snippet']['channelId']
        channel_title = item['snippet']['channelTitle']
        Video.objects.create(
            video_id=video_id,
            title=title,
            description=description,
            channel_id=channel_id,
            channel_title=channel_title,
            publishedDateTime=publishedDateTime,
            thumbnailsUrls=thumbnailsUrls,
        )


