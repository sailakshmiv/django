from django.template import Template, Context
from django.template.loader import get_template
from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("hello world")
def current_datetime(request):
    now = datetime.datetime.now()
    place = 'ShangHai'
 #   t = Template("<html><body>It is now{{current_time}}.</body></html>")#using Template
  #  t = get_template('base.html')
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_time':now,'place':place}))
 
  # html = "<html><body>It is now %s.</body></html>" % now
  #  html = t
    return HttpResponse(html)
def hours_ahead(request,offset):
    try:
        offset=int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s. </body></html>"%(offset,dt)
    return HttpResponse(html)
