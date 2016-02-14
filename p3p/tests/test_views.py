from django.test import Client, SimpleTestCase
from django.core.urlresolvers import reverse


class ResolveP3PViewTests(SimpleTestCase):
    client = Client()

    def test_p3p_xml_url(self):
        p3p_url = reverse('p3p:p3p')
        response = self.client.get(p3p_url)

        self.assertEqual(response.status_code, 200)

        self.assertTrue(response.has_header('Content-Type'))
        self.assertEqual(response.get('Content-Type'), 'text/xml')

    def test_policy_url(self):
        policy_url = reverse('p3p:policy')
        response = self.client.get(policy_url)

        self.assertEqual(response.status_code, 200)

        self.assertTrue(response.has_header('Content-Type'))
        self.assertEqual(response.get('Content-Type'), 'text/xml')
