from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='exam-home'),
    path('about/', views.about, name='exam-about')
]
