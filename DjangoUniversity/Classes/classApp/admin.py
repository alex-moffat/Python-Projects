from django.contrib import admin

#========== IMPORT model (Class) from module 'models'
from .models import DjangoClasses

#========== REGISTER model (Class) inside 'products' app
admin.site.register(DjangoClasses)