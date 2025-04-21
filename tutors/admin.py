from django.contrib import admin
from .models import Tutor, Enquiry

# Register your models here.

@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_registered' ,'email', 'hire_date', 'login_id']
    search_fields = ['name', 'login_id']

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'course', 'created_at']
    search_fields = ['name', 'email']
