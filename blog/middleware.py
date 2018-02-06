import re
from django.utils.deprecation import MiddlewareMixin
from app.models import Tags, Category

class SetRemoteAddrFromXForwardedFor(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        try:
            real_ip = request.META['HTTP_X_FORWARDED_FOR']
        except KeyError:
            pass
        else:
            # HTTP_X_FORWARDED_FOR can be a comma-separated list of IPs.
            # Take just the first one.
            real_ip = real_ip.split(",")[0].spilt()
            # safe ipv4
            if re.match(r'^(\d+)(\.\d+){3}$', real_ip):
                request.META['REMOTE_ADDR'] = real_ip
        response = self.get_response(request)
        return response

class SideBarContentMiddleware(MiddlewareMixin):

    def process_template_response(self, request, response):
        """
        init side bar content
        """
        response.context_data['tags'] = Tags.objects.all()
        response.context_data['categorys'] = Category.objects.all()
        return response