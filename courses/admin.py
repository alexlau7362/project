from django.contrib import admin
from . models import Course
from django.apps import apps

Tutor = apps.get_model('tutors', 'Tutor')

# Register your models here.
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('tutor', 'course_name' ,'course_code', 'medium', 'admission_criteria', 
        'fee', 'start_date', 'end_date', 'parental_care', 'location', 'class_size',
            'is_published', 'published_date', 'photo_main')
    #list_display_links = 'name'
    #search_fields = 'name'
    #list_editable = 'is_registered',
    #list_editable = 'login_id'
    #list_per_page = '25'

admin.site.register(Course,CoursesAdmin)
