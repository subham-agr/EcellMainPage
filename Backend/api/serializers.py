from rest_framework import serializers
from .models import *

class HomeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Home
        fields = ('about','about_image')

class InitiativesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Initiatives
        fields = ('initiative_id','initiative_name','coverimage','introtext')

class HomeCoverImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HomeCoverImage
        fields = ('sequence','image_name','image')