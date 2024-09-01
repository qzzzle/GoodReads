"""
Handles user registration and login functionality.

This module supports registering new users and logging in existing users based on email and password.
"""

import logging
from django.contrib.auth import authenticate, get_user_model, login
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import UserSerializer

logger = logging.getLogger(__name__)
User = get_user_model()

class RegisterLoginAPIView(APIView):
    """
    Manages user registration and login.

    """
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        """
        Handle user registration or login.

        Scenario:
        - Registers a new user if the email doesn't exist.
        - Logs in the user if email and password are correct.
        - Returns errors for missing fields or incorrect credentials.

        Returns:
        - 201 Created for successful registration.
        - 200 OK for successful login.
        - 400 Bad Request for validation or authentication failures.
        """
        try:
            email = request.data.get('email')
            password = request.data.get('password')
            
            if not email or not password:
                logger.warning("Email or password not provided.")
                return Response(
                    {'error': 'Email and password are required.'},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            user = authenticate(request, username=email, password=password)
            
            if user is not None:
                login(request, user)
                logger.info(f"User {user.id} logged in successfully.")
                return Response(
                    {'message': 'Login successful',
                    'user': UserSerializer(user).data},
                )
            
            if User.objects.filter(email=email).exists():
                logger.warning(f"Login attempt failed for email: {email}")
                return Response(
                    {'error': 'Incorrect email or password'},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            
            user = User.objects.create_user(username=email, email=email, password=password)
            login(request, user)
            logger.info(f"New user {user.id} registered and logged in successfully.")
            return Response(
                {'message': 'Registration successful',
                'user': UserSerializer(user).data},
                status=status.HTTP_201_CREATED,
            )

        except Exception as e:
            logger.error(f"Error during registration/login: {str(e)}")
            return Response(
                {'error': 'An error occurred during registration/login.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
