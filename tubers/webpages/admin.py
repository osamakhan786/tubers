from django.contrib import admin
from .models import Abouter, Slider, Team
from django.utils.html import format_html

# Register your models here.
    
    

class TeamerAdmin(admin.ModelAdmin):

    def myphoto(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))

    list_display = ('headline','myphoto', 'subtitle', 'created_date')
    list_display_links = ('headline',)
    
    

class TeamAdmin(admin.ModelAdmin):

    def myphoto(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))

    list_display = ('id','myphoto', 'frist_name','role','created_date')
    list_display_links = ('frist_name',)
    search_fields = ('frist_name', 'role')
    list_filter = ('role',)



    



admin.site.register(Slider, TeamerAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Abouter)