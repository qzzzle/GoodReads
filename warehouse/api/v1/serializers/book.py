"""
Serializers for Book model and related details.

This module provides serializers for listing books and retrieving detailed book information,
including bookmarks and reviews.
"""

import logging
from django.db import models
from rest_framework import serializers
from rest_framework.reverse import reverse
from warehouse.models import Book, Review
from .review import ReviewSerializer

logger = logging.getLogger(__name__)

class BookSerializer(serializers.ModelSerializer):
    """
    Serializes basic book information with additional computed fields.

    Includes details about user-specific bookmark status and overall bookmark count.
    """
    bookmarked_by_user = serializers.SerializerMethodField()
    bookmark_count = serializers.SerializerMethodField()
    details_url = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'bookmarked_by_user',
            'bookmark_count',
            'details_url',
        )

    def get_bookmarked_by_user(self, obj):
        """
        Returns whether the current user has bookmarked this book.
        """
        try:
            user = self.context['request'].user
            if user.is_authenticated:
                return obj.bookmarks.filter(user=user).exists()
            return False
        except Exception as e:
            logger.error(f"Error in checking bookmark status for user: {str(e)}")
            return False

    def get_bookmark_count(self, obj):
        """
        Returns the total number of bookmarks for this book.
        """
        try:
            return obj.bookmarks.count()
        except Exception as e:
            logger.error(f"Error in counting bookmarks for book {obj.id}: {str(e)}")
            return 0

    def get_details_url(self, obj):
        """
        Returns the URL to the detailed view of this book.
        """
        try:
            request = self.context.get('request')
            return reverse('book-detail', kwargs={'pk': obj.pk}, request=request)
        except Exception as e:
            logger.error(f"Error in generating details URL for book {obj.id}: {str(e)}")
            return None

class BookDetailSerializer(serializers.ModelSerializer):
    """
    Serializes detailed book information, including reviews and rating statistics.

    Provides a comprehensive view of a book's reviews, ratings, and distribution of ratings.
    """
    reviews = ReviewSerializer(many=True, read_only=True)
    review_count = serializers.SerializerMethodField()
    rating_count = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()
    rating_distribution = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'summary',
            'review_count',
            'rating_count',
            'average_rating',
            'rating_distribution',
            'reviews',
        )

    def get_rating_distribution(self, obj):
        """
        Returns the distribution of ratings for this book.
        """
        try:
            distribution = Review.objects.filter(book=obj).values('rating').annotate(count=models.Count('rating'))
            return {item['rating']: item['count'] for item in distribution}
        except Exception as e:
            logger.error(f"Error in calculating rating distribution for book {obj.id}: {str(e)}")
            return {}

    def get_average_rating(self, obj):
        """
        Returns the average rating for this book.
        """
        try:
            return Review.objects.filter(book=obj).aggregate(models.Avg('rating'))['rating__avg']
        except Exception as e:
            logger.error(f"Error in calculating average rating for book {obj.id}: {str(e)}")
            return None

    def get_review_count(self, obj):
        """
        Returns the total number of reviews for this book.
        """
        try:
            return obj.reviews.count()
        except Exception as e:
            logger.error(f"Error in counting reviews for book {obj.id}: {str(e)}")
            return 0

    def get_rating_count(self, obj):
        """
        Returns the total number of ratings for this book.
        """
        try:
            return Review.objects.filter(book=obj).count()
        except Exception as e:
            logger.error(f"Error in counting ratings for book {obj.id}: {str(e)}")
            return 0
