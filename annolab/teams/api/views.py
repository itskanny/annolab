from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, JSONParser

from annolab.teams.api.serializer import TeamSerializer, TeamListingSerializer
from annolab.teams.models import Team
from rest_framework.serializers import ValidationError


class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.with_details()
    parser_classes = [MultiPartParser, JSONParser]

    def get_queryset(self):
        if not self.request.organization:
            raise ValidationError({'non_field_errors': ['Organization with id does not exist']})
        assert isinstance(self.request.organization.id, int)

        return self.queryset.filter(organization=self.request.organization.id)

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return TeamListingSerializer
        return TeamSerializer
