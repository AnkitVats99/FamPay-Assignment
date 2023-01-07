from rest_framework import serializers

class PageNumberSerializer(serializers.Serializer):
    page_number = serializers.IntField()

class TitleAndDescriptionSerializer(serializers.Serializer):
    page_number = serializers.IntField(default=1)
    title = serializers.CharField()
    description = serializers.CharField()
