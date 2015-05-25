from django.core.urlresolvers import reverse
from django.test import TestCase


from p3p.middleware import P3PMiddleware


class MiddlewareTest(TestCase):

    def test_add_deader(self):
        mw = P3PMiddleware()
        response = {}
        request = None

        response = mw.process_response(request, response)

        self.assertIn('P3P', response)


class URLSTest(TestCase):

    def test_reverse(self):
        reverse('p3p')
        reverse('policy')
        

class ViewTest(TestCase):

    def test_get_policy(self):

        url = reverse('policy')

        self.client.get(url)

    def test_get_p3p(self):

        url = reverse('p3p')

        self.client.get(url)
