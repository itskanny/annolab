from django.db import models


class TeamListingManager(models.Manager):
    def with_details(self):
        return self.annotate(
            total_members=models.Count('members')
        )
