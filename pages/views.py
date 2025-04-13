from django.shortcuts import render
from tutors.models import Tutor
from pages.models import Page

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