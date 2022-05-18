from django.db import models


class ProjectQueryManager(models.Manager):
    def with_details(self):
        return self.annotate(
            total_images=models.Count('images'),
            annotated_images=models.Count('images', filter=models.Q(images__is_annotated=True))
        )
