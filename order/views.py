from django.http import HttpResponseRedirect
from django.contrib.formtools.wizard.views import SessionWizardView
from django.shortcuts import render_to_response
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.template import RequestContext
from order.models import Order
import os

def done(request):
    return render_to_response('order/done.html', context_instance=RequestContext(request))

class OrderWizard(SessionWizardView):
    instance = None
    # Temporary storage for uploaded files
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'temp'))

    def get_form_instance(self, step):
        if self.instance is None:
            self.instance = Order()
        return self.instance

    def get_template_names(self):
        return 'order/step.html'

    def done(self, form_list, **kwargs):
        # Do something with form data
        forms = [form.cleaned_data for form in form_list]
        # Save an order
        order = self.instance
        order.save()
        return HttpResponseRedirect('done')