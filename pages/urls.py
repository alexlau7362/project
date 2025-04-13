"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('course', views.course, name='course'),
    path('accounts', views.accounts, name='accounts')
    path('about', views.tutor, name='tutor')
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""