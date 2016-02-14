import django
if django.VERSION < (1, 6):
    # Expose for Django 1.5 and below (before DiscoverRunner)
    from .test_middleware import *  # noqa
    from .test_urls import *  # noqa
    from .test_views import *  # noqa
