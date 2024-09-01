"""
This module contains the Book model.
"""


from django.db import models
from django.utils.translation import gettext_lazy as _

from goodreads.mixins import TimeStampMixin

class Book(TimeStampMixin):
    """
    Django model representing a Book.
    
    The Book model represents a book entity in the system. Each book has a title 
    and an optional summary. The model tracks when a book was created and last modified 
    through the TimeStampMixin, which provides created and modified timestamp fields.
    """

    title = models.CharField(
        _("Title"),
        max_length=255,
        unique=True,
        help_text=_("Enter a unique title."),
    )

    summary = models.TextField(
        _("Summary"),
        null=True,
        blank=True,
        help_text=_(
            "Provide a summary of the book. This helps users understand the book's content."
        ),
    )

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")
        get_latest_by = ("created", "modified")
        indexes = [
            models.Index(fields=("title",), name="title_idx"),
        ]


    def __str__(self) -> str:
        return f"{self.title}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}: {self.title}"