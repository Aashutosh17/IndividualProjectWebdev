from django.contrib import messages

from .forms import userform
# Create your views here.
from django.http.response import HttpResponse

from django.shortcuts import render


# Create your views here.

def dashboard(request):

    return render(request , 'dashboard.html')

def reservemessage(request):

    if (request.method=="POST"):
        forms = userform(request.POST)
        if(forms.is_valid()):
            forms.save()
            messages.success(request,'Your Message is sent Sucessfully!')
            return render(request,'dashboard.html')

        else:
            return HttpResponse (" Couldn't send your message try again later!")


