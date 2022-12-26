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