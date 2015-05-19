from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^p3p/', include('p3p.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
