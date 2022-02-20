import imp
from pkgutil import ImpImporter
from django import http
from django.contrib.auth import login, authenticate
# Create your views here.
from django.http.response import HttpResponse

from django.shortcuts import redirect, render


# Create your views here.

def loginfn(request):


    return render(request , 'loginsignup.html')

def validation(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request,username= username, password=password)

    if user is not None:
        login(request, user)
        return redirect('/dashboard/dashboard')

    else:
        return HttpResponse('Sorry you cannot login in')

