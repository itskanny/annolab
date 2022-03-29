from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, DateField, ImageField, EmailField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Default custom user model for annolab.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=False, max_length=255)
    email = EmailField(unique=True)
    username = CharField(blank=True, null=True, unique=True, max_length=256)
    date_of_birth = DateField(blank=True, null=True)
    avatar = ImageField(blank=True, null=True, upload_to='avatars')
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
