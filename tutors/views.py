from django.shortcuts import render
from django.http import HttpResponse
#from courses.models import Course
#from tutors.models import Tutor
#from courses.choices import course_code_choices, course_name_choices, location_choices
# Create your views here.

def index(request):
    tutor = Tutor.objects.all()
    context = {'tutor' : tutor}
    return render(request, 'pages/index.html', context)

def about(request):
    tutor = Tutor.objects.all()
    context = {'tutor' : tutor}
    return render(request, 'pages/about.html', context)
"""
def about(request):
    tutors = Tutor.objects.order_by('-hire_date')
    registered_tutors = tutors.object.all().filter(is_registered=True)
    context = {'tutors' : tutors, "registered_tutors" : registered_tutors}
    return render(request, 'pages/about.html', context)
"""
"""
def course(request):
    return render(request, 'pages/course.html')

def accounts(request):
    return render(request, 'pages/accounts.html')

"""