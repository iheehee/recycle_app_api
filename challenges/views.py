from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework import status
from .permissions import IsSelf
from .serializers import ChallengeSerializer, ChallengeMemberSerializer
from .models import Challenge, ChallengeMember
from users.models import User


class ChallengeViewSet(ModelViewSet):

    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return ChallengeSerializer
        if self.action == "retrieve":
            return ChallengeSerializer
        if self.action == "create":
            return ChallengeSerializer
        if self.action == "member":
            return ChallengeSerializer


        return super().get_serializer_class()

    def get_permissions(self):

        if self.action in ["list", "create", "retrieve", "regist_member", "member"]:
            return [AllowAny()]
        if self.action in ["update"]:
            return [IsSelf()]

        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        """챌린지 생성"""
        return super().create(request, *args, **kwargs)


    @action(detail=True)
    def member(self, request, pk):
        challenge = self.get_object()
        user = request.user
        challenge_join = ChallengeMember(challenge_name=challenge, member=user)
        challenge_join.save()
        challenge.member.add(User.objects.get(pk=user.pk))

        


        

        


        