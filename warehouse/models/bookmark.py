"""
This module contains the Bookmark model. """

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from goodreads.mixins import TimeStampMixin

class Bookmark(TimeStampMixin):

    """
    Bookmark Model

    Represents a bookmark created by a user for a specific book. This model links a user 
    to a book, allowing the user to keep track of books they are interested in. The model 
    also tracks when the bookmark was created and last modified through the inherited 
    TimeStampMixin.
    """

    book = models.ForeignKey(
        "Book",
        on_delete=models.CASCADE,
        verbose_name=_("Book"),
        related_name="bookmarks",
        help_text=_("The book that is bookmarked by the user."),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="bookmarks",
        verbose_name=_("User"),
        help_text=_("The user associated with the bookmark."),
    )

    class Meta:
        verbose_name = _("Bookmark")
        verbose_name_plural = _("Bookmarks")
        unique_together = ('user', 'book')
        db_table = "bookmarks"

    def __str__(self):
        return f'{self.user.username} bookmarked {self.book.title}'
