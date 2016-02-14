from django.http import HttpResponse
from django.test import RequestFactory, SimpleTestCase

from ..middleware import P3PMiddleware


class P3PMiddlewareTest(SimpleTestCase):

    rf = RequestFactory()

    def test_p3p_response_header(self):
        request = self.rf.get('/')
        response = HttpResponse("Example response")

        self.assertEqual(
            P3PMiddleware().process_response(request, response),
            response
        )

        self.assertTrue(response.has_header('P3P'))
        self.assertEqual(response.get('P3P'), 'CP=""')
