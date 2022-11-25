from urllib import request
import jwt
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework import status
from .permissions import IsSelf
from .serializers import (
    LoginSerializer,
    UserSerializer,
    UserRegisterSerializer,
    UserInfoUpdateSerializer,
    ProfileSerializer
)
from .models import User
from challenges.models import ChallengeApply, Challenge
from challenges.serializers import ChallengeSerializer


class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == "login":
            return LoginSerializer
        if self.action == "list":
            return UserSerializer
        if self.action == "retrieve":
            return UserSerializer
        if self.action == "create":
            return UserRegisterSerializer
        if self.action == "partial_update":
            return UserInfoUpdateSerializer

        return super().get_serializer_class()

    def get_permissions(self):

        if self.action in ["list", "create", "login", "retrieve", "my_challenge"]:
            return [AllowAny()]
        if self.action in ["update"]:
            return [IsSelf()]

        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        """회원가입"""
        return super().create(request, *args, **kwargs)

    @action(detail=False, methods=["post"], url_path="login", url_name="login")
    def login(self, request, *args, **kwargs):
        """로그인"""
        email = request.data.get("email")
        password = request.data.get("password")
        if not (email and password):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        if user is not None:
            encoded_jwt = jwt.encode({"user": user}, "secret", algorithm="HS256")
            return Response(data=encoded_jwt)
        else:
            return Response(
                data={"아이디와 비빌번호를 다시 확인해주세요."}, status=status.HTTP_401_UNAUTHORIZED
            )

    def partial_update(self, request, *args, **kwargs):
        """유저정보 수정"""
        return super().update(request, *args, **kwargs)

    #@action(detail=True, methods=["get"])
    #def profile(self, request. pk):
    #    """프로필 조회"""

    @action(detail=True, methods=["get"])
    def my_challenge(self, request, pk):
        user = request.user
        my_challenge = ChallengeApply.objects.filter(member_id__exact=user.pk).select_related('challenge_id')
        my_challenge_info = [challenge.challenge_id for challenge in my_challenge ]
        my_challenge_list = []
        for s in my_challenge_info:
            serializer = ChallengeSerializer(s).data
            my_challenge_list.append(serializer)
        return Response(data=my_challenge_list)



