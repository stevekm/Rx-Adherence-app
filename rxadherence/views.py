from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from rxadherence.models import Drug, User
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

all_drugs = Drug.objects.all()
all_users = User.objects.all()

def drugs(request, id = None):
    """
    """
    if id == None:
        data = [{'name': item.name} for item in all_drugs]
    else:
        print(id)
        queryset = Drug.objects.filter(id = id)
        print(queryset)
        data = [{'name': item.name} for item in queryset]
        print(data)
    response = JsonResponse(data, safe = False)
    return(response)

def users(request, username = None):
    """
    """
    if username == None:
        data = [{'name': item.username} for item in all_users]
    else:
        queryset = User.objects.filter(username = username)
        data = [{'name': item.username} for item in queryset]
    response = JsonResponse(data, safe = False)
    return(response)
