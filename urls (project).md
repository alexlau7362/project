# project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from courses.views import index
from accounts.views import logout
from django.shortcuts import redirect

urlpatterns = [
    path('', index, name='home'),  # Root URL maps to courses.views.index
    path('index/', index, name='index'),  # Handle /index
    path('courses/', include('courses.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/logout/', lambda request: redirect('/logout/', permanent=False)),  
    path('admin/', admin.site.urls),
    path('tutors/', include('tutors.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

