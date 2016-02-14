#!/usr/bin/env python
import sys
import django
from django.conf import settings
from django.core.management import execute_from_command_line
from os import path


if not settings.configured:
    module_root = path.dirname(path.realpath(__file__))
    sys.path.insert(0, path.join(module_root, 'example'))

    settings.configure(
        INSTALLED_APPS=(
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sites',
            'django.contrib.admin',
            'django.contrib.sessions',
            'p3p'
        ),
        TEST_RUNNER='django.test.simple.DjangoTestSuiteRunner' if django.VERSION < (1, 6) else 'django.test.runner.DiscoverRunner',
    )


def runtests():
    argv = sys.argv[:1] + ['test', 'p3p'] + sys.argv[1:]
    execute_from_command_line(argv)

if __name__ == '__main__':
    runtests()
