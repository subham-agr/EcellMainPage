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

class GallerySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gallery
        fields = ('sequence','image_name','image')

class PatronagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patronages
        fields = ('sequence','image_name','image')

class VisionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vision
        fields = ('vision','vision_image')

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ('name','designation','image','linkedin','facebook','instagram','whatsapp','email')