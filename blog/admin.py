from django.contrib import admin
from .models import *
from res_users.models import Customer

admin.site.register(Blog)
admin.site.register(Customer)

