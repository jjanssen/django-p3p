from django.views.generic import TemplateView


class XmlView(TemplateView):
    content_type = 'text/xml'
    template_name = 'p3p/p3p.xml'


class P3PView(TemplateView):
    content_type = 'text/xml'
    template_name = 'p3p/policy.p3p'
