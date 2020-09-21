from django.contrib import admin

#========== IMPORT
from .models import Stock
from .models import Trade

#========== REGISTER
admin.site.register(Stock)
admin.site.register(Trade)
