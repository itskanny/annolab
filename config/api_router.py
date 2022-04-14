from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from annolab.users.api.views import UserViewSet
from annolab.groups.api.views import GroupViewSet
from annolab.organizations.api.views import OrganizationViewSet
if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("groups", GroupViewSet)
router.register("organizations", OrganizationViewSet)

app_name = "api"
urlpatterns = router.urls
