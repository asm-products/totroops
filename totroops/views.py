from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import datetime


def faq(request):
    return render(request, 'faq.html')

def home(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def beta_signup(request):
    if request.method == "POST":
        # Add an entry to the auth_user table with this email address.
        email = request.POST['email']
        user = User.objects.get_or_create(username=email, email=email)
        return HttpResponseRedirect(url_for('thanks'))

    return render(request, 'beta_signup.html')

def thanks(request):
    return render(request, 'thanks.html')
