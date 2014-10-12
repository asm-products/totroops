import datetime

from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext, loader

import logging


logger = logging.getLogger('testlogger')

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
        template = loader.get_template('thanks.html')
        context = RequestContext(request, {
                'user': user,
            })
        logger.info("%s just signed up!" % email)
        return HttpResponse(template.render(context))

    return render(request, 'beta_signup.html')

def thanks(request):
    return render(request, 'thanks.html')
