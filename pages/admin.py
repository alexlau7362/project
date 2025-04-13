from django.contrib import admin

# Register your models here.
from . models import Page

class PageAdmin(admin.ModelAdmin):
    list_display = ( 'medium', 'admission_criteria', 'photo_main')
    #list_display_links = 'name'
    #search_fields = 'name'
    #list_editable = 'is_registered',
    #list_editable = 'login_id'
    #list_per_page = '25'

admin.site.register(Page,PageAdmin)
#admin.site.register(Courses)