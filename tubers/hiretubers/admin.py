
from django.contrib import admin
from .models import Hiretuber
# Register your models here.

class Htuber(admin.ModelAdmin):
    list_display = ('first_name', 'tuber_name','city', 'phone', 'state',)
    list_display_links = ('first_name', 'city', 'phone')


admin.site.register(Hiretuber, Htuber)