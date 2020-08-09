from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Exam


# Create your views here.
def home(request):
    return render(request, 'exam/base.html')


def about(request):
    return HttpResponse('<h1>Fuck Neda</h1>')


class ExamListView(ListView):
    model = Exam
    context_object_name = 'exams'
    template_name = 'exam/list_of_exams.html'

    paginate_by = 3
    ordering = ['-date']
