from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Enquiry
from django.core.mail import send_mail
# Create your views here.
def enquiry(request):
    if request.method == 'POST':
        course_code = request.POST['course_code']
        course_name = request.POST['course_name']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        if request.user.is_authenticated:
            # user_id = request.user.id
            has_enquired = Enquiry.objects.all().filter(course_code=course_code)
            if has_enquired:
                messages.error(request, 'You have already made an inquiry for this course')
                return redirect('/courses/'+course_code)
        enquiry = Enquiry(course_name=course_name, course_code=course_code, name=name, email=email, phone=phone, message=message)
        enquiry.save()
        send_mail(
            'Course Inquiry',
            'There has been an inquiry for '+course_name+'. Sign into the admin panel for more info',
            'wuskella138@gmail.com',#from email
            ['skellawu@gmail.com'], #to email
            fail_silently=False
        )

        messages.success(request, 'Your request has been submitted, a tutor will get back to you soon')
        return redirect('/courses/'+course_code)

def delete_enquiry(request, course_id):
    enquiry=get_object_or_404(Enquiry, pk=course_id)
    enquiry.delete()
    return redirect('noticeboard')
    return render(request, 'enquiries/enquiry.html')
