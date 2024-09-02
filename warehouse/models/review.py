"""This module contains the Review model."""

from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from goodreads.mixins import TimeStampMixin


class Review(TimeStampMixin):
    """
    Review Model

    Represents a review submitted by a user for a specific book. Each review
    includes a rating (from 1 to 5 stars) and an optional text comment. The model also
    tracks the
    timestamp when the review was created.
    """

    book = models.ForeignKey(
        "Book",
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name=_("Book"),
        help_text=_("Select the book for which this review was submitted."),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="reviews",
        verbose_name=_("User"),
        help_text=_(
            "Select the user who submitted this review. If the user is deleted, the "
            "review will remain but the user reference will be removed."
        ),
    )

    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name=_("Rating"),
        help_text=_(
            "Enter a rating for the book, ranging from 1 (worst) to 5 (best) stars."
        ),
        blank=True,
        null=True,
    )

    comment = models.TextField(
        verbose_name=_("Comment"),
        help_text=_(
            "Enter any additional comments or feedback provided by the user about the "
            "book."
        ),
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")
        ordering = ["-created"]
        indexes = [
            models.Index(fields=["created"]),
            models.Index(fields=["book", "user"]),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["book", "user"], name="unique_book_user_review"
            )
        ]

    def __str__(self):
        return (
            f"{self.user.username if self.user else 'Unknown User'}'s review of"
            f" {self.book.title}"
        )
