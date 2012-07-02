from setuptools import setup, find_packages

setup(
    name='django-p3p',
    version='0.1.1b',
    description='Django P3P makes it easier to set P3P HTTP headers to prevent session loss.',
    long_description=open('README.rst').read(),
    author='Janneke Janssen',
    author_email='j.janssen@lukkien.com',
    url='http://github.com/jjanssen/django-p3p',
    packages=find_packages(exclude=['p3p_example']),
    include_package_data=True
)