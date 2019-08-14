from django.shortcuts import render
from rest_framework import viewsets, mixins, generics, permissions
from .models import User
from .models import UserProfile, Role
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login
from rest_framework_jwt.settings import api_settings
from .serializers import TokenSerializer, UserSerializer, ProfileSerializer, RoleSerializer
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class RegisterUsersView(generics.CreateAPIView):
    """
    POST auth/register/
    """
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        email = request.data.get("email", "")
        # role = request.data.get("role", 1)
        if not username and not password and not email:
            return Response(
                data={
                    "message": "username,password and email is required to register a user"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        new_user = User.objects.create_user(
            username=username, password=password, email=email,
        )
        querys = User.objects.filter(email=email).values()
        print(querys)
        return Response(data={
            "message": "Account created successfully",
            "user_details": querys[0]
        },
            status=status.HTTP_201_CREATED)


class LoginView(generics.CreateAPIView):
    """
    POST auth/login/
    """
    # This permission class will overide the global permission
    # class setting
    permission_classes = (permissions.AllowAny,)
    # serializer_class = SurveySerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        email = request.data.get("email", "")
        password = request.data.get("password", "")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            # login saves the user’s ID in the session,
            # using Django’s session framework.
            login(request, user)
            querys = User.objects.filter(email=email).values()
            print(querys[0])

            groups = serializers.serialize("json",
                                           (Group.objects.all().filter(user=querys[0]['id'])), fields=('fields'))
            serializer = TokenSerializer(data={
                # using drf jwt utility functions to generate a token
                "token": jwt_encode_handler(
                    jwt_payload_handler(user)
                )})
            serializer.is_valid()

            return Response(data={
                'message': 'Login successful',
                # 'groups': groups,
                'id': querys[0]['id'],
                'token': serializer.data['token'],
                'query': querys[0],
            }, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UsersProfileViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer


class RolesViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
