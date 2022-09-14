from crypt import methods
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework import status
from .serializers import UserSerializer, UserRegisterSerializer
from .models import User


class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):

        if self.action in ["list", "create"]:
            return [AllowAny()]

        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == "list":
            return UserSerializer
        if self.action == "create":
            return UserRegisterSerializer

        return super().get_serializer_class()


    def create(self, request, *args, **kwargs):
        """회원가입"""
        return super().create(request, *args, **kwargs)
