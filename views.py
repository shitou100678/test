from django.http import HttpResponse
from django.shortcuts import redirect

def index(request):
    return HttpResponse('ok')

def login(request):
    redirect('/index')
