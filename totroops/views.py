from datetime import datetime, date

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader

from totroops.models import Recipent

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
        # Add an entry to the Recipent model with this info.

        name = request.POST['name']
        address = request.POST['address']

        recipent = Recipent.get_or_create(name=name, address=address)

        # import ipdb; ipdb.set_trace()
        logger.info("%s, %s - submitted." % (name, address))

        template = loader.get_template('poll.html')
        context = RequestContext(request, {
                'recipent': recipent
            })
        return HttpResponse(template.render(context))

    data = { 'current_year': date.today().year }

    return render(request, 'beta_signup.html', data)

def thanks(request):
    return render(request, 'thanks.html')
