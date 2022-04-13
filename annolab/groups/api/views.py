from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser, FileUploadParser

from .serializer import GroupSerializer
from annolab.groups.models import Group


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    parser_classes = [MultiPartParser]
