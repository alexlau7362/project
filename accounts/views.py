from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from enquiries.models import Enquiry
from .models import UserProfile

# Create your views here.
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
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists!')
                    return redirect('register')
                else:
                   user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                   user.save()
                   messages.success(request, 'You are now registered and can log in!')
                   return redirect('login')   
        else:
            messages.error(request, 'Passwords do not match!')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    # context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            # context['message'] = 'Login successful'
            # messages.success(request, 'You are now logged in!')
            return redirect('noticeboard')
        else :
            messages.error(request, 'Invalid credentials!')
            return redirect('login')
    else :
        return render(request, 'accounts/login.html')

# def login(request):
#     context = {
#         'some_variable': 'Some Value',
#     }
#     return render(request, 'accounts/login.html', context)

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('index')
    auth.logout(request)
    messages.success(request, 'You are now logged out!')
    return redirect('home')

@login_required
def profile(request):
    # Get or create the user profile
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        if 'photo' in request.FILES:
            user_profile.photo = request.FILES['photo']
            user_profile.save()
            messages.success(request, 'Profile photo updated successfully!')
            return redirect('profile')
    
    context = {
        'user_profile': user_profile
    }
    return render(request, 'accounts/profile.html', context)
    
def noticeboard(request):
    user_enquiry = Enquiry.objects.filter(user=request.user).order_by('-created_at')
    context = {
        'user_enquiry': user_enquiry
    }
    return render(request, 'accounts/noticeboard.html', context)

