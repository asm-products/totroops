from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'totroops.views.beta_signup', name='beta_signup'),
    url(r'^thanks/$', 'totroops.views.thanks', name='thanks'),
    url(r'^faq/$', 'totroops.views.faq', name='faq'),
    url(r'^poll/$', 'polls.views.poll', name='poll'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
