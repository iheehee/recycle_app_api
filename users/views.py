from crypt import methods
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework import status
from .serializers import UserSerializer
from .models import User


class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):

        global permission_classes

        if self.action == "list":
            permission_classes = [AllowAny]
        elif self.action == "retrieve":
            permission_classes = [AllowAny]
        else:
            pass
        return [permission() for permission in permission_classes]

class UserRegisterViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer



    def login(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            return Response()
        user = authenticate(username=username, password=password)
        
        
