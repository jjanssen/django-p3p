#!/usr/bin/env python
import sys
import django
import warnings

from django.conf import settings
from django.core.management import execute_from_command_line


if not settings.configured:
    settings.configure(
        INSTALLED_APPS=(
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sites',
            'django.contrib.admin',
            'django.contrib.sessions',
            'p3p'
        ),
        ROOT_URLCONF='p3p.tests.urls',
        TEST_RUNNER='django.test.runner.DiscoverRunner',
        TEMPLATES=[
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'APP_DIRS': True,
            },
        ]
    )


def runtests():
    # Don't ignore DeprecationWarnings
    warnings.simplefilter('default', DeprecationWarning)

    argv = sys.argv[:1] + ['test', 'p3p'] + sys.argv[1:]
    execute_from_command_line(argv)

if __name__ == '__main__':
    runtests()
