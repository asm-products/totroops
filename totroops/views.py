from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
import datetime


def home(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def beta_signup(request):
    if request.method == "POST":
        # Add an entry to the auth_user table with this email address.
        email = request.POST['email']
        user = User.objects.create_user(username=email, email=email)
        user.save()
        return render(request, 'beta_signup.html')

    return render(request, 'beta_signup.html')
