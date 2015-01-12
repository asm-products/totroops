from datetime import datetime, date

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader

from totroops.models import Recipient

import logging


logger = logging.getLogger('testlogger')

def faq(request):
    return render(request, 'faq.html')

def home(request):
    if request.method == "POST":
        # Add an entry to the Recipient model with this info.

        name = request.POST['name']
        address = request.POST['address']

        import ipdb; ipdb.set_trace()

        recipient = Recipient.objects.get_or_create(name=name, address=address)

        # import ipdb; ipdb.set_trace()
        logger.info("%s, %s - submitted." % (name, address))

        template = loader.get_template('poll.html')
        context = RequestContext(request, {
                'recipient': recipient
            })
        return HttpResponse(template.render(context))

    data = { 'current_year': date.today().year }

    return render(request, 'home.html', data)

def thanks(request):
    return render(request, 'thanks.html')
