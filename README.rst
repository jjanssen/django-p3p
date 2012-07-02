Django P3P
==========

About Django P3P
----------------
If your webpage uses sessions you willl lose your session in Internet Explorer when your page gets embedded into in iFrame. This problem can be solved by setting application specific `P3P headers <http://en.wikipedia.org/wiki/P3P>`_.

Django P3P is an application which makes it easier to set those specific headers for your Django application. 

.. This package includes the IBM P3P Policy Editor for determining the exact headers you want to use.


Installation
------------

Install django-p3p with pip::

    $ pip install -e http://github.com/jjanssen/django-p3p#egg=django-p3p
    
    
Configuration
-------------

Configuring P3P
^^^^^^^^^^^^^^^

Add the following to your settings file:

    * Add ``p3p`` to ``INSTALLED_APPS``
    * Add ``p3p.middleware.P3PMiddleware`` to ``MIDDLEWARE_CLASSES``
    
URL Configuration
^^^^^^^^^^^^^^^^^

You need to include the `p3p.urls` urlpatterns in your root url configuration, for e.g.::

    (r'^w3c/', include('p3p.urls', namespace='p3p')),
    ...
    (r'^admin/', include(admin.site.urls)),
    
    
.. warning::

    Please keep in mind you should follow the W3C prefix in pattern. So the browser can resolve the ``/w3c/p3p.xml``. In the future I'll probably set a HTTP header for this, but right now I'm too lazy to do this.