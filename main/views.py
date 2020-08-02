from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'main/index.htm')


def about(requset):
    return HttpResponse('<h1> FUCK </h1>')
