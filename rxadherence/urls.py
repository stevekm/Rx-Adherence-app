from django.urls import path
from rxadherence.views import drugs, users, usages, use

urlpatterns = [
    path('drugs/', drugs), # return all drugs JSON list of dicts
    path('drugs/<int:id>/', drugs), # return one drug in a JSON list of dicts
    path('users/', users), # return all users JSON list of dicts
    path('users/<str:username>', users), # return all users JSON list of dicts
    path('usages/', usages),
    path('usages/<str:username>/<int:drug_id>', usages),
    path('use/<str:username>/<int:drug_id>', use),
]
