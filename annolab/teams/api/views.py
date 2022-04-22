from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser

from annolab.teams.api.serializer import TeamSerializer
from annolab.teams.models import Team


class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
    parser_classes = [MultiPartParser]
