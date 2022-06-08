from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser

from annolab.annotations.api.serializer import AnnotationSerializer
from annolab.annotations.models import Annotation


class AnnotationViewSet(viewsets.ModelViewSet):
    serializer_class = AnnotationSerializer
    queryset = Annotation.objects.all()
    model = Annotation
    parser_classes = [MultiPartParser,
                       JSONParser, FormParser]

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('image',)

    # def get_queryset(self):
    #     return self.queryset.filter(image=self.request.data.image)
