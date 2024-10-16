Django P3P
==========

.. image:: https://travis-ci.org/jjanssen/django-p3p.svg?branch=develop
    :target: http://travis-ci.org/jjanssen/django-p3p
.. image:: https://img.shields.io/pypi/v/django-p3p.svg
    :target: https://pypi.python.org/pypi/django-p3p/
.. image:: https://img.shields.io/pypi/dm/django-p3p.svg
    :target: https://pypi.python.org/pypi/django-p3p/
.. image:: https://img.shields.io/badge/wheel-yes-green.svg
    :target: https://pypi.python.org/pypi/django-p3p/
.. image:: https://img.shields.io/pypi/l/django-p3p.svg
    :target: https://pypi.python.org/pypi/django-p3p/
.. image:: https://img.shields.io/pypi/pyversions/Django.svg
    :target: https://pypi.python.org/pypi/django-p3p/
.. image:: https://coveralls.io/repos/jjanssen/django-p3p/badge.svg?branch=develop
    :target: https://coveralls.io/github/jjanssen/django-p3p?branch=develop

About Django P3P
----------------
If your webpage uses sessions you will lose your session in Internet Explorer when your page gets embedded into in iFrame. This problem can be solved by setting application specific `P3P headers <http://en.wikipedia.org/wiki/P3P>`_.

Django P3P is an application which makes it easier to set those specific headers for your Django application. You can use an editor like IBM's P3P Policy Editor to configure your website policy to its needs.


Requirements
------------

Django 1.8.x or greater, Python 2.7 or greater.


Installation
------------

Install django-p3p with pip::

    $ pip install django-p3p


Configuration
-------------

Configuring django-p3p
^^^^^^^^^^^^^^^^^^^^^^

Add the following to your settings file:

    * Add ``p3p`` to ``INSTALLED_APPS``
    * Add ``p3p.middleware.P3PMiddleware`` to ``MIDDLEWARE_CLASSES``


URL Configuration
^^^^^^^^^^^^^^^^^

You need to include the `p3p.urls` urlpatterns in your root url configuration, for e.g.::

    (r'^w3c/', include('p3p.urls', namespace='p3p')),
    ...
    (r'^admin/', include(admin.site.urls)),


Overriding templates
^^^^^^^^^^^^^^^^^^^^

You need to override at least 2 templates to configure your project specific HTTP headers and policy:

    * `templates/p3p/headers.txt`

Contains the actual HTTP headers which are sent to the browser. For e.g.: ``CP="NOI CURa ADMa DEVa TAIa CONa OUR DELa BUS IND PHY ONL UNI PUR COM NAV DEM STA"``

    * `templates/p3p/policy.p3p`

Contains the policy as required for the application. You can generate one by using the IBM P3P Policy Editor.


.. note::

    I left the initial templates mostly blank to prevent default usage. Mainly because every application has its own specific policies and it requires you to **THINK** about what policy fits your website.
