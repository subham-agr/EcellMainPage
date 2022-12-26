from django.shortcuts import render
import json
from http.client import HTTPResponse
from django.http.response import JsonResponse
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from typing import OrderedDict
import requests
# Create your views here.

from .models import *
from .serializers import *

@api_view(['GET'])
def home(request):
    if request.method == 'GET':
        home_data = Home.objects.all()
        data_list = []
        for home_data1 in home_data:
            img_path = request.build_absolute_uri(settings.MEDIA_URL) + str(home_data1.about_image)
            data = OrderedDict([('about_text',home_data1.about),('about_picture',img_path)])
            data_list.append(data)
        return JsonResponse(data_list,safe=False)

@api_view(['GET'])
def initiative(request):
    if request.method == 'GET':
        initatives = Initiatives.objects.all()
        data_list = []
        for initiative in initatives:
            img_path = request.build_absolute_uri(settings.MEDIA_URL) + str(initiative.coverimage)
            data = OrderedDict([('id',initiative.initiative_id),('name',initiative.initiative_name),('text',initiative.introtext),('image_link',img_path)])
            data_list.append(data)
        return JsonResponse(data_list,safe=False)

@api_view(['GET'])
def gallery(request):
    if request.method == 'GET':
        gallery_images = Gallery.objects.all()
        data_list = []
        for gallery_image in gallery_images:
            img_path = request.build_absolute_uri(settings.MEDIA_URL) + str(gallery_image.image)
            data = OrderedDict([('sequence',gallery_image.sequence),('name',gallery_image.image_name),('image_link',img_path)])
            data_list.append(data)
        return JsonResponse(data_list,safe=False)

@api_view(['GET'])
def homeimages(request):
    if request.method == 'GET':
        homecoverimages = HomeCoverImage.objects.all()
        data_list = []
        for homecoverimage in homecoverimages:
            img_path = request.build_absolute_uri(settings.MEDIA_URL) + str(homecoverimage.image)
            data = OrderedDict([('sequence',homecoverimage.sequence),('name',homecoverimage.image_name),('image_link',img_path)])
            data_list.append(data)
        return JsonResponse(data_list,safe=False)

@api_view(['GET'])
def team(request):
    if request.method == 'GET':
        members = Team.objects.all()
        data_list = []
        for member in members:
            img_path = request.build_absolute_uri(settings.MEDIA_URL) + str(member.image)
            data = OrderedDict([('member_name',member.name),('designation',member.designation),('image_link',img_path),('email',member.email),('linkedin',member.linkedin),('facebook',member.facebook),('instagram',member.instagram),('whatsapp',member.whatsapp)])
            data_list.append(data)
        return JsonResponse(data_list,safe=False)

@api_view(['GET'])
def patronages(request):
    if request.method == 'GET':
        patronages = Patronages.objects.all()
        data_list = []
        for patronage in patronages:
            img_path = request.build_absolute_uri(settings.MEDIA_URL) + str(patronage.image)
            data = OrderedDict([('sequence',patronage.sequence),('name',patronage.image_name),('image_link',img_path)])
            data_list.append(data)
        return JsonResponse(data_list,safe=False)

@api_view(['GET'])
def vision(request):
    if request.method == 'GET':
        about_vision = Vision.objects.all()
        data_list = []
        for about_vision1 in about_vision:
            img_path = request.build_absolute_uri(settings.MEDIA_URL) + str(about_vision1.vision_image)
            data = OrderedDict([('vision',about_vision1.vision),('vision_image',img_path)])
            data_list.append(data)
        return JsonResponse(data_list,safe=False)