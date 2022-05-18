from rest_framework.generics import get_object_or_404
from rest_framework.serializers import ValidationError


class URLParameterValidatorMixin:
    parameter_name = None
    parameter_model = None

    def validate_url_parameter(self, request, **kwargs):
        assert self.parameter_model is None, 'Parameter model is required'
        assert self.parameter_name is None, 'Parameter name is required'
        assert kwargs.get(self.parameter_name, None) is None, 'Parameter in request does not exist'

        get_object_or_404(self.parameter_model, pk=self.parameter_name)
