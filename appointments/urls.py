from django.urls import path
from . import views

urlpatterns = [
    path('role_redirect/', views.role_redirect, name='role_redirect'),
    path('appointments/student/', views.student_dashboard, name='student_dashboard'),
    path('appointments/book/', views.book_appointment, name='book_appointment'),
    path('appointments/edit/<int:pk>/', views.edit_appointment, name='edit_appointment'),
    path('appointments/delete/<int:pk>/', views.delete_appointment, name='delete_appointment'),
    path('advisor_dashboard/', views.advisor_dashboard, name='advisor_dashboard'),
    path('advisor/approve/<int:pk>/', views.approve_appointment, name='approve_appointment'),
    path('advisor/reject/<int:pk>/', views.reject_appointment, name='reject_appointment'),
]