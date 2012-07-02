from django.template.loader import render_to_string


class P3PMiddleware(object):

    def process_response(self, request, response):
        response['P3P'] = render_to_string('p3p/headers.txt')
        return response