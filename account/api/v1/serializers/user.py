"""
Serializer for User model.

This module serializes User instances for use in API responses.
"""

import logging

from django.contrib.auth import get_user_model

from rest_framework import serializers


logger = logging.getLogger(__name__)
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    Serializes User model data for API responses.
    """

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "date_joined",
        )
