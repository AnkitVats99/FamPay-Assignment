from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import *
from django.core.paginator import Paginator
from .serializer import *
from django.db.models import Q
from .helper import rename_data_keys


@api_view(['GET'])
def fetch_youtube_videos(request: Request):
    try:
        params = request.GET.dict()
        api_serializer = TitleAndDescriptionSerializer(data=params)
        api_serializer.is_valid(raise_exception=True)
        page_number = api_serializer.validated_data['page_number'] 
        if api_serializer.validated_data.get('search'):
            search = api_serializer.validated_data['search'] 
            query_list = list(Video.objects.filter(Q(title__icontains=search)| Q(description__icontains=search)).values().order_by('-publishedDateTime'))
        else:
            query_list = list(Video.objects.all().values().order_by('-publishedDateTime'))

        paginator = Paginator(query_list, 5) # Show 5 contacts per page.
        page_obj = paginator.get_page(page_number)
        return Response(page_obj.object_list, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"msg": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)