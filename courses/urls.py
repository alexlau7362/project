from django.urls import path
from . import views

# urlpatterns = [
#     path('pages', views.course, name='courses'),
#     path('<int:course_id>', views.course, name='course'),
#     # path('search', views.search, name='search'),
# ]
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('course/', views.course, name='course'),
    path('course/<int:course_id>', views.course, name='course'),
    path('accounts/', views.accounts, name='accounts'),
    path('search/', views.search, name='search'),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)