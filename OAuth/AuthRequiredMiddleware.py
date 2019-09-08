from django.shortcuts import HttpResponseRedirect
from django.conf import settings
from PeerReview.Logger import getLogger

log = getLogger("AuthRequiredMiddleware")

class AuthRequiredMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # for each request before the view (and later middleware) are called
        # should execute this code
        allowed_url = ['/auth/oauth2callback/', '/auth/portalLogin/','/accounts/login/', '/about/', '/']
        if request.path_info in allowed_url:
            return self.get_response(request)
        elif 'credentials' not in request.session:
            log.info("Redirecting to authentication page")
            return HttpResponseRedirect(settings.LOGIN_URL)

        response = self.get_response(request)

        return response
