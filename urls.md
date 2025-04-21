# courses/urls.py
from django.urls import path
from .views import index, course, search, about, accounts

app_name = 'courses'
urlpatterns = [
    path('', index, name='courses'),  # Course list
    path('course/<int:course_id>/', course, name='course_detail'),
    path('search/', search, name='search'),
    path('about/', about, name='about'),
    path('accounts/', accounts, name='accounts'),
]