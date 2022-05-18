from rest_framework import viewsets
from rest_framework.serializers import ValidationError
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from rest_framework_extensions.mixins import NestedViewSetMixin

from .serializer import ImageSerializer
from ..models import Image
from annolab.projects.models import Project


class ImageViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
    model = Image
    parser_classes = [MultiPartParser,
                      # JSONParser, FormParser]
                      ]

    # def get_queryset(self):
    #
    #     print('Hello')
    #     return self.queryset.filter(project=self.kwargs['projects'])

    # def initialize_request(self, request, *args, **kwargs):
    #     print(request.body)
