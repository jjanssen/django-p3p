from setuptools import setup, find_packages
from p3p import __version__

# Testing dependencies
testing_extras = [
    'coverage>=4.4.2',
    'flake8>=3.5.0',
    'tox>=2.9.1'
]

setup(
    name='django-p3p',
    version=__version__,
    license='Apache License, Version 2.0',

    requires=[
        'Django (>=1.11)',
    ],

    description='''Django P3P makes it easier to set
        P3P HTTP headers to prevent session loss.''',
    long_description=open('README.rst').read(),

    author='Janneke Janssen',
    author_email='j.janssen@lukkien.com',

    keywords='session patch middleware django',

    url='http://github.com/jjanssen/django-p3p',

    packages=find_packages(),
    include_package_data=True,

    test_suite='runtests',

    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Browsers',
        'Topic :: Internet :: WWW/HTTP :: Session'
    ],

    extras_require={
        'testing': testing_extras
    },
)
