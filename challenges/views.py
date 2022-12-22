from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework import status
from .permissions import IsSelf
from .serializers import (
    ChallengeSerializer,
    ChallengeCreateSerializer,
    ChallengeCertificationSerializer,
)
from .models import Challenge, ChallengeApply, ChallengeCertification
from users.models import User, Profile
from datetime import datetime, timedelta 

class ChallengeViewSet(ModelViewSet):

    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer

    def get_serializer_class(self):
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
        if self.action == "certification":
            return ChallengeCertificationSerializer
        return super().get_serializer_class()

    def get_permissions(self):

        if self.action in ["list", "create", "retrieve", "member", "certification"]:
            return [AllowAny()]
        if self.action in ["regist_member"]:
            return [IsAuthenticated()]
        if self.action in ["update", "destroy", "apply_challenge", "leave_challenge"]:
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
    def apply_challenge(self, request, pk):
        """챌린지 멤버 등록"""
        profile = Profile.objects.get(nickname=request.user)
        """트랜젝션으로 묶는다"""
        challenge_query = Challenge.objects.filter(id__exact=self.get_object().pk)
        challenge = challenge_query[0]
        if challenge.max_member > challenge.number_of_applied_member:
            ChallengeApply.objects.create(challenge_id=challenge, member_id=profile)
            number_of_applied_member_count_up = challenge.number_of_applied_member + 1
            challenge_query.update(
                number_of_applied_member=number_of_applied_member_count_up
            )
            #  커밋하기전 다시한번 challenge.number_of_applied_member 체크
            # 오버되면 커밋하지않고 롤백
            return Response(
                data={"result": "챌린지에 등록되었습니다."}, status=status.HTTP_201_CREATED
            )
        else:
            return Response(data={"result": "인원이 다 찼습니다."})

    @action(methods=["delete"], detail=True)
    def leave_challenge(self, request, pk):
        """챌린지 탈퇴"""
        profile = Profile.objects.get(nickname=request.user)
        challenge_query = Challenge.objects.filter(id__exact=self.get_object().pk)
        challenge = challenge_query[0]
        ChallengeApply.objects.filter(
            challenge_id__exact=challenge, member_id__exact=profile
        ).delete()
        number_of_applied_member_count_down = challenge.number_of_applied_member - 1
        challenge_query.update(
            number_of_applied_member=number_of_applied_member_count_down
        )
        return Response(data={"result": "챌린지를 탈퇴했습니다."})

    @action(methods=["post"], detail=True)
    def certification(self, request, pk):
        query = Challenge.objects.filter(id__exact=self.get_object().pk)[0]
        frequency = query.get_frequency_display()
        durations = query.get_duration_display()
        date = query.start_day
        #total = frequency * durations
        time = date + timedelta(days=6, hours=23, minutes=59, seconds=59)
        success_certification = ChallengeCertification.objects.filter(certification_date__range=[date, time], )
        if len(success_certification) <= frequency :
            serializer = ChallengeCertificationSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        else :
            return Response(data={"result" : "이번주 인증은 모두 완료했습니다."})        
        return Response(date={"인증 성공"})

