# pages/views.py
from django.shortcuts import render
from pages.models import Page
from django.apps import apps

Tutor = apps.get_model('tutors', 'Tutor')

def index(request):
    # Fetch data for index.html (e.g., courses, pages)
    courses = apps.get_model('courses', 'Course').objects.filter(is_published=True)[:6]  # Limit to 6 courses
    pages = Page.objects.all()
    context = {
        'courses': courses,
        'pages': pages,
        'location_choices': apps.get_model('courses', 'Course')._meta.get_field('location').choices,
        'start_date_choices': [],  # Add if defined in courses.models
        'fee_choices': [],  # Add if defined
    }
    return render(request, 'pages/index.html', context)

def about(request):
    tutors = Tutor.objects.order_by('-hire_date')
    registered_tutors = tutors.filter(is_registered=True)
    pages = Page.objects.all()
    context = {
        'pages': pages,
        'tutors': tutors,
        'registered_tutors': registered_tutors
    }
    return render(request, 'pages/about.html', context)