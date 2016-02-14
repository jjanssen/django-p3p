import django
if django.VERSION < (1, 6):
    # Expose for Django 1.5 and below (before DiscoverRunner)
    from .test_middleware import *
    from .test_urls import *
    from .test_views import *
