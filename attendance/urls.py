from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.handleRegister, name='register'),
    path('login', views.handleLogin, name='login'),
    path('staff', views.staff, name='staff'),
    path('student', views.student, name='student'),
    path('generate_qr', views.generate_qr, name='qr'),
    path('mark_present', views.markPresent, name='markpresent'),
    path('view_attendance', views.view_attendance, name='view_attendance'),
    path('download_attendance', views.download_attendance, name='download_attendance'),
    path('update_attendance', views.update_attendance, name='update_attendance')
]
