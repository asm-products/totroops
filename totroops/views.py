from django.http import HttpResponse
from django.shortcuts import render
import datetime

def home(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def beta_signup(request):

    return render(request, 'beta_signup.html')
