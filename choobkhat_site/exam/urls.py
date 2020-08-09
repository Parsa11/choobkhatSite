from django.urls import path
from . import views
from .views import ExamListView

urlpatterns = [
    path('', ExamListView.as_view(), name='exam-home'),
    path('about/', views.about, name='exam-about'),
]
