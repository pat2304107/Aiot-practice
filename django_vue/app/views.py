from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from .models import BadmintonInfo
from django.core import serializers
import requests
import json



def badminton_page(request):
    data = serializers.serialize("json", BadmintonInfo.objects.all().order_by("-id")[:1])
    # [
    #   {"temperature": 1}, .....
    # ]
    #

    return HttpResponse(data)
