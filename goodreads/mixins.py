from django.db import models
from django.utils.translation import gettext_lazy as _

class TimeStampMixin(models.Model):
    """
    Abstract Django Model that contains:
        created, modified
    """

    created = models.DateTimeField(
        _("Created at"),
        auto_now_add=True,
        help_text=_(
            "This timestamp indicates when the model instance was initially"
            " added or created. It is automatically set when the record is"
            " first created and should not be modified manually."
        ),
    )

    modified = models.DateTimeField(
        _("Modified at"),
        auto_now=True,
        help_text=_(
            "This timestamp represents the most recent update or modification"
            " to the model instance. It is automatically updated every time"
            " the record is modified."
        ),
    )

    class Meta:
        abstract = True
