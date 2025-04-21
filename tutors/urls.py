"""
# tutors/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import noticeboard, enquiry, logout

app_name = 'tutors'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='tutors/login.html',
        redirect_authenticated_user=True,
        next_page='tutors:noticeboard'
    ), name='login'),
    path('logout/', logout, name='logout'),
    path('noticeboard/', noticeboard, name='noticeboard'),
    path('enquiry/<int:course_id>/', enquiry, name='enquiry'),
]
"""

# tutors/urls.py
from django.urls import path
from .views import login, noticeboard, enquiry, logout

app_name = 'tutors'
urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('noticeboard/', noticeboard, name='noticeboard'),
    path('enquiry/<int:course_id>/', enquiry, name='enquiry'),
]
