from django.contrib import admin

# Register your models here.
from .models import Drug
from .models import User
from .models import Usage

admin.site.register(Drug)
admin.site.register(User)
admin.site.register(Usage)
