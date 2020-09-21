from django.contrib import admin
from .models import Description, WaitingRoom
# Register your models here.
admin.site.register((Description, WaitingRoom))