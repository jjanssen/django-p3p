from django.conf.urls import include, url

urlpatterns = [
    url(r'^w3c/', include('p3p.urls', namespace='p3p')),
]
