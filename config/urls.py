from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from appointments import views

from django.shortcuts import render

def root_redirect(request):
    return render(request, 'welcome.html')

urlpatterns = [
    path('', root_redirect, name='home'),
    path('admin/', admin.site.urls),
    path('appointments/', include('appointments.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('redirect/', views.role_redirect, name='role_redirect'),
]