from django.contrib import admin
from django.urls import path
from studentApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', views.student_list, name='student_list'),
]