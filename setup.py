from setuptools import setup, find_packages

setup(
    name='django-p3p',
    version='1.0.1',
    description='Django P3P makes it easier to set P3P HTTP headers to prevent session loss.',
    long_description=open('README.rst').read(),
    author='Janneke Janssen',
    author_email='j.janssen@lukkien.com',
    keywords='session patch middleware django',
    url='http://github.com/jjanssen/django-p3p',
    packages=find_packages(exclude=['p3p_example']),
    include_package_data=True,
    platforms='any',
    license='Apache License, Version 2.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Topic :: Internet :: WWW/HTTP :: Browsers',
        'Topic :: Internet :: WWW/HTTP :: Session'
    ]
)
