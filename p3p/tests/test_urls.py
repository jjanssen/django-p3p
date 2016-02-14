from django.test import SimpleTestCase
from django.core.urlresolvers import reverse


class ResolveP3PUrlTests(SimpleTestCase):

    def test_p3p_xml_url(self):
        p3p_url = reverse('p3p:p3p')
        self.assertTrue(p3p_url.endswith('/p3p.xml'))

    def test_policy_url(self):
        policy_url = reverse('p3p:policy')
        self.assertTrue(policy_url.endswith('/policy.p3p'))
