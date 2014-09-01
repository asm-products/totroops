from django.http import HttpResponse
import datetime

def home(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def beta_signup(request):
    html = "<html><body>this is the beta email signup.</body></html>"
    return HttpResponse(html)
