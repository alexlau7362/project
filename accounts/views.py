"""
# accounts/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from enquiries.models import Enquiry
from .models import UserProfile
from tutors.models import Tutor

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if user.is_superuser:
                return redirect('/admin/')
            try:
                Tutor.objects.get(login_id=username)
                return redirect('tutors:noticeboard')
            except Tutor.DoesNotExist:
                return redirect('accounts:user_enquiries')
        else:
            messages.error(request, 'Invalid credentials!')
            return redirect('accounts:login')
    else:
        return render(request, 'accounts/login.html')
"""
# accounts/views.py
from django.shortcuts import redirect, render
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from tutors.models import Tutor
from courses.models import Course
from pages.models import Page
from courses.choices import course_code_choices, course_name_choices, location_choices, start_date_choices, fee_choices

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if user.is_superuser:
                return redirect('/admin/')
            try:
                Tutor.objects.get(login_id=username)
                return redirect('tutors:noticeboard')
            except Tutor.DoesNotExist:
                return redirect('accounts:user_enquiries')
        else:
            messages.error(request, 'Invalid credentials!')
            return redirect('accounts:login')
    else:
        # Clear messages on GET
        storage = messages.get_messages(request)
        storage.used = True
        return render(request, 'accounts/login.html')

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


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!')
                return redirect('accounts:register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists!')
                    return redirect('accounts:register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(request, 'You are now registered and can log in!')
                    return redirect('accounts:login')
        else:
            messages.error(request, 'Passwords do not match!')
            return redirect('accounts:register')
    else:
        return render(request, 'accounts/register.html')

@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        if 'photo' in request.FILES:
            user_profile.photo = request.FILES['photo']
            user_profile.save()
            messages.success(request, 'Profile photo updated successfully!')
            return redirect('accounts:profile')
    context = {
        'user_profile': user_profile
    }
    return render(request, 'accounts/profile.html', context)

@login_required
def user_enquiries(request):
    user_enquiry = Enquiry.objects.filter(user=request.user).order_by('-created_at')
    context = {
        'user_enquiry': user_enquiry
    }
    return render(request, 'accounts/noticeboard.html', context)

@login_required
def delete_enquiry(request, enquiry_id):
    enquiry = get_object_or_404(Enquiry, id=enquiry_id, user=request.user)
    if request.method == 'POST':
        enquiry.delete()
        messages.success(request, 'Enquiry deleted successfully!')
        return redirect('accounts:user_enquiries')
    return render(request, 'accounts/confirm_delete.html', {'enquiry': enquiry})

# accounts/views.py (temporary debug view)
def debug_user(request):
    print(f"User: {request.user}, Authenticated: {request.user.is_authenticated}")
    return render(request, 'accounts/login.html')