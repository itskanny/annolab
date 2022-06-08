from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework_extensions.routers import ExtendedSimpleRouter, ExtendedDefaultRouter

from annolab.annotations.api.views import AnnotationViewSet
from annolab.teams.api.views import TeamViewSet
from annolab.users.api.views import UserViewSet
from annolab.groups.api.views import GroupViewSet
from annolab.organizations.api.views import OrganizationViewSet
from annolab.projects.api.views import ProjectViewSet
from annolab.images.api.views import ImageViewSet

if settings.DEBUG:
    router = ExtendedDefaultRouter()
else:
    router = ExtendedSimpleRouter()

router.register("users", UserViewSet)
router.register("groups", GroupViewSet)
router.register("organizations", OrganizationViewSet)
# router.register("projects/<int:project>/images", ImageViewSet, basename='images')
router.register("projects", ProjectViewSet, basename='projects') \
    .register(r'images',
              ImageViewSet,
              basename='images',
              parents_query_lookups=['project'])
router.register("teams", TeamViewSet)
router.register("annotations", AnnotationViewSet)

app_name = "api"
urlpatterns = router.urls
