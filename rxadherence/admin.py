from django.contrib import admin

# Register your models here.
from .models import Drug
from .models import User
admin.site.register(Drug)
admin.site.register(User)
