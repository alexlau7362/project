# from django.shortcuts import render
# from courses.choices import course_code_choices, course_name_choices, location_choices

# # Create your views here.
# def course(request):
#     context = {
#         'course_code_choices': course_code_choices,
#         'course_name_choices': course_name_choices,
#         'location_choices': location_choices,
#     }
#     return render(request, 'pages/courses.html', context)

from django.shortcuts import render, redirect
from django.http import HttpResponse
from courses.models import Course
from tutors.models import Tutor
from pages.models import Page
# from .models import Course, Tutor, Page

from .choices import course_code_choices, course_name_choices, location_choices, start_date_choices, fee_choices

def index(request):
    courses = Course.objects.order_by('-published_date').filter(is_published=True)#[:3]
    pages = Page.objects.all()
    context = {
        'pages' : pages,
        'courses': courses,
        'course_code_choices': course_code_choices,
        'course_name_choices': course_name_choices,
        'location_choices': location_choices,
        'start_date_choices': start_date_choices,
        'fee_choices': fee_choices,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    tutors = Tutor.objects.order_by('-hire_date')  #.select_related('related_field')
    registered_tutors = tutors.filter(is_registered=True)
    pages = Page.objects.all()
    context = {
        'pages' : pages,
        'tutors': tutors,
        'registered_tutors': registered_tutors
    }
    return render(request, 'pages/about.html', context)


def course(request):
    courses = Course.objects.order_by('-published_date').filter(is_published=True)
    context = {
        'courses': courses
    }
    return render(request, 'pages/course.html', context)

def accounts(request):
    return redirect('login') 

def search(request):
    courses = Course.objects.order_by('-published_date')
    
    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            courses = courses.filter(admission_criteria__icontains=keywords)
    
    # Course Name
    if 'course_name' in request.GET:
        course_name = request.GET['course_name']
        if course_name:
            courses = courses.filter(course_name__iexact=course_name)
    
    # Course Code
    if 'course_code' in request.GET:
        course_code = request.GET['course_code']
        if course_code:
            courses = courses.filter(course_code__iexact=course_code)
    
    # Location
    if 'location' in request.GET:
        location = request.GET['location']
        if location:
            courses = courses.filter(location__iexact=location)
    
    # Course_name
    if 'course_name' in request.GET:
        course_name = request.GET['course_name']
        if course_name:
            courses = courses.filter(course_name__icontains=course_name)
    
    # Start Date
    if 'start_date' in request.GET:
        start_date = request.GET['start_date']
        if start_date:
            courses = courses.filter(start_date__icontains=start_date)
    
    # Fee
    if 'fee' in request.GET:
        fee = request.GET['fee']
        if fee:
            courses = courses.filter(fee__iexact=fee)
    
    context = {
        'courses': courses,
        'course_code_choices': course_code_choices,
        'course_name_choices': course_name_choices,
        'location_choices': location_choices,
        'start_date_choices': start_date_choices,
        'fee_choices': fee_choices,
        'values': request.GET
    }
    return render(request, 'pages/search.html', context) 