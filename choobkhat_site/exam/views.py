from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'exam/base.html')


def about(request):
    return HttpResponse('<h1>Fuck Neda</h1>')
