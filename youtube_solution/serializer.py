from rest_framework import serializers
from django.db.models.fields import TextField
from django.core.validators import RegexValidator

class TitleAndDescriptionSerializer(serializers.Serializer):
    page_number = serializers.IntegerField(default=1,required=False)
    title = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
