from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from goodreads.mixins import TimeStampMixin

class User(AbstractUser, TimeStampMixin):

    email = models.EmailField(
        _("Email"),
        unique=True,
        validators=[],
        error_messages={"unique": "This email is already taken."},
        help_text="The email of the user.",
    )
