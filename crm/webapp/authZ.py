from ms_identity_web import IdentityWebPython
from functools import wraps
from django.shortcuts import redirect
from django.http import HttpResponseForbidden

class CRMIdentityWebPython(IdentityWebPython):

    def azure_ad_required_claim(self, roles):
        def decorator(f):
            @wraps(f)
            def assert_authz(*args, **kwargs):
                if self._adapter.identity_context_data.authenticated:
                    claim_roles = self._adapter.identity_context_data._id_token_claims['extension_Roles']
                    for role in claim_roles:
                        if not role in claim_roles:
                            return HttpResponseForbidden("You do not have permission to view this page.")
                    return f(*args, **kwargs)
            return assert_authz
        return decorator
