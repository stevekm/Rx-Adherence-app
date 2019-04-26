from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from rxadherence.models import Drug, User, Usage
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

all_drugs = Drug.objects.all()
all_users = User.objects.all()

def drugs(request, id = None):
    """
    """
    if id == None:
        data = { item.id : item.name for item in all_drugs}
    else:
        queryset = Drug.objects.filter(id = id)
        data = { item.id : item.name for item in queryset}
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

# def usage(request, username, drug)
