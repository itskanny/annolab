from rest_framework import viewsets
from rest_framework.serializers import ValidationError
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser

from .serializer import ImageSerializer
from ..models import Image
from annolab.projects.models import Project


class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
    parser_classes = [MultiPartParser,
                      # JSONParser, FormParser]
                      ]

    def get_queryset(self):

        if not self.request.query_params.get('pid', None):
            raise ValidationError({"non_field_errors": ["Project does not exist"]})

        project = None
        try:
            project = Project.objects.get(id=self.request.query_params['pid'])
        except Project.DoesNotExist:
            raise ValidationError({"non_field_errors": ["Project does not exist"]})

        return self.queryset.filter(project=project.id)

    # def initialize_request(self, request, *args, **kwargs):
    #     print(request.body)
