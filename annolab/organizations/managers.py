from django.db import models


class OrganizationQueryManager(models.Manager):
    def with_details(self):
        return self.annotate(
            total_projects=models.Count('projects', distinct=True),
            total_teams=models.Count('teams', distinct=True)
        )
