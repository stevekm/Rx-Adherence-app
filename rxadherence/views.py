from django.shortcuts import render
from rxadherence.models import Drug, User, Usage
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

all_drugs = Drug.objects.all()
all_users = User.objects.all()
all_usages = Usage.objects.all()

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
        data = { item.id : item.username for item in all_users}
    else:
        queryset = User.objects.filter(username = username)
        data = { item.id : item.username for item in queryset}
    response = JsonResponse(data, safe = False)
    return(response)

def usages(request, username = None, drug_id = None):
    """
    """
    if username == None and drug_id == None:
        data = []
        for item in all_usages:
            d = {
            'id': item.id,
            'username': item.username.username,
            'drug': item.drug.name,
            'time': item.time
            }
            data.append(d)
    elif username != None:
        username_instance = User.objects.get(username = username)
        queryset = Usage.objects.filter(username = username_instance)
        data = []
        for item in queryset:
            d = {
            'id': item.id,
            'username': item.username.username,
            'drug': item.drug.name,
            'time': item.time
            }
            data.append(d)
    response = JsonResponse(data, safe = False)
    return(response)

def use(request, username, drug_id):
    """
    """
    user_instance = User.objects.get(username = username)
    drug_instance = Drug.objects.get(id = int(drug_id))
    Usage.objects.create(
        username = user_instance,
        drug = drug_instance
        )
    return(HttpResponse('Success'))
