"""
Defines the custom User model.

Extends Django's AbstractUser with additional fields and functionality,
including a unique email field and timestamp tracking.
"""

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from goodreads.mixins import TimeStampMixin


class User(AbstractUser, TimeStampMixin):
    """
    Custom User model with unique email and timestamp fields.

    - Inherits from AbstractUser for standard user management.
    - Adds unique email validation and timestamp fields for creation and modification
    tracking.
    """

    email = models.EmailField(
        _("Email"),
        unique=True,
        validators=[],
        error_messages={"unique": "This email is already taken."},
        help_text="The email of the user.",
    )
