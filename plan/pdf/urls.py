from django.conf.urls.defaults import *


urlpatterns = patterns('plan.pdf.views',
    url(r'^(?P<year>\d{4})/(?P<semester_type>\w+)/(?P<slug>[a-zA-Z0-9-_]+)/pdf/(?:(?P<size>A\d)/)?$', 'pdf', name='schedule-pdf'),
)
