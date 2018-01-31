from django.conf.urls import url
from .views import XmlView, P3PView

app_name = 'p3p'

urlpatterns = [
    url(r'^p3p.xml$', XmlView.as_view(), name='p3p'),
    url(r'^policy.p3p$', P3PView.as_view(), name='policy'),
]
