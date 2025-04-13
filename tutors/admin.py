from django.contrib import admin

# Register your models here.
from . models import Tutor

class TutorAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_registered' ,'email', 'hire_date', 'login_id')
    #list_display_links = 'name'
    #search_fields = 'name'
    #list_editable = 'is_registered',
    #list_editable = 'login_id'
    #list_per_page = '25'

admin.site.register(Tutor,TutorAdmin)