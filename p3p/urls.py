from django.conf.urls.defaults import patterns, url
from p3p.views import XmlView, P3PView

urlpatterns = patterns('p3p.views',
    url(r'^p3p.xml$', XmlView.as_view(), name='p3p'),
    url(r'^policy.p3p$', P3PView.as_view(), name='policy'),
)
