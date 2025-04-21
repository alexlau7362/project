# tutors/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.core.mail import send_mail
from django.http import JsonResponse
from django.conf import settings
from courses.models import Course
from .models import Enquiry, Tutor
from pages.models import Page
from courses.choices import course_code_choices, course_name_choices, location_choices, start_date_choices, fee_choices
import logging

logger = logging.getLogger(__name__)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('tutors:noticeboard')
        else:
            messages.error(request, 'Invalid credentials!')
            return redirect('tutors:login')
    else:
        # Clear messages on GET
        storage = messages.get_messages(request)
        storage.used = True
        return render(request, 'tutors/login.html')

@login_required
def noticeboard(request):
    try:
        tutor = Tutor.objects.get(login_id=request.user.username)
    except Tutor.DoesNotExist:
        messages.error(request, "You are not registered as a tutor.")
        return redirect('home')
    courses = tutor.courses.all()
    return render(request, 'tutors/noticeboard.html', {'tutor': tutor, 'courses': courses})

@login_required
def enquiry(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST.get('phone', '')
        message = request.POST['message']
        enquiry = Enquiry(
            course=course,
            name=name,
            email=email,
            phone=phone,
            message=message,
            user=request.user
        )
        enquiry.save()
        try:
            send_mail(
                subject=f'New Enquiry for {course.course_name}',
                message=f'From: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['alauct@google.com'],
                fail_silently=False,
            )
            messages.success(request, 'Your enquiry has been submitted successfully!')
        except Exception as e:
            logger.error(f"Failed to send email for enquiry {enquiry.id}: {str(e)}")
            messages.error(request, 'Your enquiry was submitted, but we failed to send the confirmation email. Please contact support.')
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': True, 'message': 'Enquiry submitted successfully!'})
        return redirect('tutors:noticeboard')
    return render(request, 'tutors/noticeboard.html', {'course': course})

def logout(request):
    auth.logout(request)
    messages.success(request, 'You are now logged out!')
    courses = Course.objects.order_by('-published_date').filter(is_published=True)
    pages = Page.objects.all()
    context = {
        'pages': pages,
        'courses': courses,
        'course_code_choices': course_code_choices,
        'course_name_choices': course_name_choices,
        'location_choices': location_choices,
        'start_date_choices': start_date_choices,
        'fee_choices': fee_choices,
    }
    response = render(request, 'pages/index.html', context)
    # Clear messages after rendering
    storage = messages.get_messages(request)
    storage.used = True
    return response