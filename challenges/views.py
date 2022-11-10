from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework import status
from .permissions import IsSelf
from .serializers import (
    ChallengeSerializer,
    ChallengeCreateSerializer,
    ChallengeApplySerializer,
)
from .models import Challenge, ChallengeApply
from users.models import User, Profile


class ChallengeViewSet(ModelViewSet):

    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    
    def get_serializer_class(self):
        print(self.action)
        if self.action == "list":
            return ChallengeSerializer
        if self.action == "retrieve":
            return ChallengeSerializer
        if self.action == "create":
            return ChallengeCreateSerializer
        if self.action == "update":
            return ChallengeCreateSerializer
        if self.action == "delete":
            return ChallengeCreateSerializer
        if self.action == "challenge_apply":
            return ChallengeApplySerializer

        return super().get_serializer_class()

    def get_permissions(self):

        if self.action in ["list", "create", "retrieve", "member"]:
            return [AllowAny()]
        if self.action in ["regist_member"]:
            return [IsAuthenticated()]
        if self.action in ["update", "destroy", "challenge_apply"]:
            return [AllowAny()]

        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        """챌린지 생성"""
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """챌린지 정보 수정"""
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """챌린지 삭제"""
        return super().destroy(request, *args, **kwargs)

    @action(methods=["post"], detail=True)
    def challenge_apply(self, request, pk):
        """챌린지 멤버 등록"""
        challenge = self.get_object()
        profile = Profile.objects.get(nickname=request.user)
        applied_challenge = ChallengeApply.objects.filter(challenge_name__exact=challenge.pk)
        if challenge.max_member > applied_challenge.count():
            ChallengeApply.objects.create(challenge_name = challenge, member_name = profile)
            return Response(data={"result": "챌린지에 등록되었습니다."}, status=status.HTTP_201_CREATED)
        else:
            return Response(data={"result": "인원이 다 찼습니다."})

    @action(methods=["put"], detail=True)
    def member_remove(self, request, pk):
        """챌린지 탈퇴"""
        user = request.user
        challenge = self.get_object()
        print(challenge)
        # challenge_member = challenge.member.all()
        serializer = ChallengeCreateSerializer(data=challenge, many=True)
        serializer.is_valid()
        print(serializer.data)

        if challenge_member in [user.pk]:
            challenge_member.remove(user)
            return Response(data={"result": "챌린지를 탈퇴했습니다."})
        else:
            return Response(data={"result": "챌린지를 했습니다."})
