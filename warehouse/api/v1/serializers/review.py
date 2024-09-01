"""
Handles review creation and validation.
"""

import logging
from rest_framework import serializers
from warehouse.models import Review

logger = logging.getLogger(__name__)

class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializes and validates Review model data.
    
    Ensures that either a rating or a comment is provided, with a valid rating between 1 and 5.
    """
    class Meta:
        model = Review
        fields = ['id', 'book', 'user', 'rating', 'comment', 'created']

    def validate_rating(self, value):
        """
        Ensures rating is between 1 and 5.
        """
        if value is not None and (value < 1 or value > 5):
            logger.warning(f"Invalid rating value: {value} by user {self.initial_data.get('user')}")
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value

    def validate(self, data):
        """
        Validates that either rating or comment is present and rating is within range.
        """
        rating = data.get('rating')
        comment = data.get('comment')
        
        if rating is None and not comment:
            raise serializers.ValidationError("Either rating or comment must be provided.")

        return data
