from crypt import methods
from urllib import request
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework import status
from .serializers import LoginSerializer, UserSerializer, UserRegisterSerializer
from .models import User




class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):

        if self.action in ["list", "create","login", "retrieve"]:
            return [AllowAny()]

        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == "login":
            return LoginSerializer
        if self.action == "list":
            return UserSerializer
        if self.action == "create":
            return UserRegisterSerializer
        
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        """회원가입"""
        return super().create(request, *args, **kwargs)

    @action(detail=False, methods=['post'], url_path='login', url_name='login')
    def login(self, request,  *args, **kwargs):
        """로그인"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validation_data['user']
        print(user)
        return Response(data=user)


       

