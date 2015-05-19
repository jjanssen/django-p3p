import django
from django.views.generic import TemplateView

class _XmlMixin(TemplateView):
    def render_to_response(self, context, **response_kwargs):
        content_type_name = 'mimetype'
        if int('%d%d' % (django.VERSION[0:2])) > 14:
            content_type_name = 'content_type'

        response_kwargs.update({content_type_name: 'text/xml' })
        return super(_XmlMixin, self).render_to_response(context, **response_kwargs)    


class XmlView(_XmlMixin):
    template_name = 'p3p/p3p.xml'

class P3PView(_XmlMixin):
    template_name = 'p3p/policy.p3p'
