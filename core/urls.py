from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('stop_process/', views.stop_process, name='stop_process'),
    path('resume_process/', views.resume_process, name='resume_process'),
]