from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about')

] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)