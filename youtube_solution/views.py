from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from videos.models import *
from django.core.paginator import Paginator
from youtube_solution.serializer import *


@api_view(['GET'])
def search_youtube_videos(request: Request):
    try:
        params = request.GET.dict()
        api_serializer = TitleAndDescriptionSerializer(data=params)
        api_serializer.is_valid(raise_exception=True)
        page_number = api_serializer.validated_data['page_number'] 
        filter = dict()
        if api_serializer.validated_data.get('title'):
            filter['title']=api_serializer.validated_data['title'] 
        if api_serializer.validated_data.get('description'):
            filter['description']=api_serializer.validated_data['description']

        query_list = list(Video.objects.filter(**filter).values().order_by('-publishedDateTime'))
        paginator = Paginator(query_list, 2) # Show 25 contacts per page.
        page_obj = paginator.get_page(page_number)
        return Response(page_obj.object_list, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"msg": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




