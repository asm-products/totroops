from django.conf.urls import patterns, url

from order.forms import OrderForm1, OrderForm2, OrderForm3
from order.views import OrderWizard

urlpatterns = patterns('',
    url(r'^$', OrderWizard.as_view([OrderForm1, OrderForm2, OrderForm3])),
    url(r'^done/$', 'order.views.done', name='done')
)
