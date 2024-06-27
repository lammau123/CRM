from django.shortcuts import redirect
from ms_identity_web.django.middleware import MsalMiddleware
try:    
    from ms_identity_web.errors import NotAuthenticatedError
    from django.conf import settings
except:
    pass

class MsLoginUrlMiddleware(MsalMiddleware):
    def process_exception(self, request, exception):
        if isinstance(exception, NotAuthenticatedError):
            return redirect('{}/{}'.format(settings.AAD_CONFIG.django.auth_endpoints.prefix, settings.AAD_CONFIG.django.auth_endpoints.sign_in))
        else:
            return super().process_exception(request, exception)
        return None