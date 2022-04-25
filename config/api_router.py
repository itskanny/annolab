from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from annolab.teams.api.views import TeamViewSet
from annolab.users.api.views import UserViewSet
from annolab.groups.api.views import GroupViewSet
from annolab.organizations.api.views import OrganizationViewSet
from annolab.projects.api.views import ProjectViewSet
from annolab.images.api.views import ImageViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("groups", GroupViewSet)
router.register("organizations", OrganizationViewSet)
router.register("projects", ProjectViewSet)
router.register("teams", TeamViewSet)
router.register("images", ImageViewSet)


app_name = "api"
urlpatterns = router.urls
