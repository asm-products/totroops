from datetime import datetime, date

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader

import logging


logger = logging.getLogger('testlogger')

def faq(request):
    return render(request, 'faq.html')

def home(request):
    now = datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def beta_signup(request):
    if request.method == "POST":
        # Add an entry to the auth_user table with this email address.
        email = request.POST['email']
        user = User.objects.get_or_create(username=email, email=email)
        template = loader.get_template('poll.html')
        context = RequestContext(request, {
                'user': user,
            })
        logger.info("%s just signed up!" % email)
        return HttpResponse(template.render(context))

    data = { 'current_year': date.today().year }

    return render(request, 'beta_signup.html', data)

def thanks(request):
    return render(request, 'thanks.html')
