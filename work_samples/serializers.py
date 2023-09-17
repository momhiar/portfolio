from rest_framework import serializers
from .models import *


class TagSeializer(serializers.ModelSerializer):
    class Meta:
        model = WorkSampleTag
        fields = '__all__'


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkSampleImage
        fields = '__all__'


class WorkSampleSerializer(serializers.ModelSerializer):
    gallery = GallerySerializer(read_only=True, many=True)
    tags = TagSeializer(read_only=True, many=True)

    class Meta:
        model = WorkSample
        fields = '__all__'
