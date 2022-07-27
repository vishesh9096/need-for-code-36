from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import *
from home.models import Contact,Queries
admin.site.register(task)
admin.site.register(Contact)
admin.site.register(Queries)