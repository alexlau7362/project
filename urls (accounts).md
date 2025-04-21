# accounts/urls.py
from django.urls import path
from .views import register, login, logout, profile, user_enquiries, delete_enquiry

app_name = 'accounts'
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('enquiries/', user_enquiries, name='user_enquiries'),
    path('enquiries/delete/<int:enquiry_id>/', delete_enquiry, name='delete_enquiry'),
]