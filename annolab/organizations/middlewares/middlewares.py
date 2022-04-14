from ..models import Organization


class OrganizationRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        organization = None
        if request.headers.get('Organization', None):
            try:
                organization = Organization.objects.get(pk=request.headers['Organization'])
            except Organization.DoesNotExist:
                organization = None

        request.organization = organization
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        return response
