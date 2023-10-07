from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from core.authentication import JWTAuthentication
from .permissions import IsAuth
from .serializers import (
    ChallengeSerializer,
    ChallengeCreateSerializer,
    ChallengeCertificationSerializer,
    CertificationExampleSerializer,
)
from .models import Challenge, ChallengeApply, ChallengeCertification
from users.models import User, Profile
from datetime import timedelta, datetime
from pytz import timezone
from django.conf import settings


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
        if self.action in [
            "list",
            "create",
            "retrieve",
            "member",
            "certification",
            "certification_status",
        ]:
            return [AllowAny()]
        if self.action in ["regist_member"]:
            return [IsAuthenticated()]
        if self.action in [
            "update",
            "destroy",
            "apply_challenge",
            "leave_challenge",
            "my_certifications",
        ]:
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
        challenge = Challenge.objects.get(id=self.get_object().pk)
        decoded = JWTAuthentication.authenticate(self, request)
        user = User.objects.get(id=decoded.id)
        profile = Profile.objects.filter(nickname_id=user)[0]

        """트랜젝션으로 묶는다"""
        if challenge.number_of_applied_member < challenge.max_member:
            ChallengeApply.objects.create(challenge_id=challenge, member_id=profile)
            """challenge.member.add(profile)
            profile.my_challenges.add(challenge)"""
            # number_of_applied_member_count_up = challenge.number_of_applied_member + 1
            challenge.number_of_applied_member += 1
            challenge.save()
            #  커밋하기전 다시한번 challenge.number_of_applied_member 체크
            # 오버되면 커밋하지않고 롤백
            return Response(data={"result": "챌린지에 등록되었습니다."}, status=status.HTTP_201_CREATED)
        else:
            return Response(data={"result": "인원이 다 찼습니다."})

    @action(methods=["delete"], detail=True)
    def leave_challenge(self, request, pk):
        """챌린지 탈퇴"""

        challenge_id = request.GET.get("id", None)
        decoded = JWTAuthentication.authenticate(self, request)
        profile = decoded.profile.first()
        challenge = Challenge.objects.filter(id=challenge_id).first()
        applied_challenge = challenge.challenge_name.filter(member_id=profile)
        applied_challenge.delete()
        number_of_applied_member_count_down = challenge.number_of_applied_member - 1
        challenge.number_of_applied_member = number_of_applied_member_count_down
        challenge.save()

        return Response(data={"result": "챌린지를 탈퇴했습니다."})

    @action(methods=["get"], detail=True)
    def certification_status(self, request, pk):
        challenge = self.get_object()
        profile = request.user
        frequency = challenge.get_frequency_display()
        durations = challenge.get_duration_display()

        def success_number():
            success_certification_search_query = ChallengeCertification.objects.filter(
                challenge_id__exact=challenge,
                challenge_participant_id__exact=profile.pk,
            )
            success_number = len(success_certification_search_query)

            return success_number

        def achievement_rate():
            total = frequency * durations
            achievement_rate = round(success_number() / total * 100)
            return achievement_rate

        def fail_number():
            fail_number = 0
            system_currnet_time = datetime.now().replace(tzinfo=timezone("Asia/Seoul"))
            start_day = challenge.start_day
            end_day = start_day + timedelta(days=7)
            for _ in range(durations):
                if system_currnet_time < end_day:
                    success_certification = ChallengeCertification.objects.filter(
                        certification_date__range=[start_day, end_day],
                        challenge_participant_id__exact=profile.pk,
                    )
                    fail_number = frequency - len(success_certification)

                elif system_currnet_time > end_day:
                    start_day = start_day + timedelta(days=7)
                    end_day = start_day + timedelta(days=7)
                    success_certification = ChallengeCertification.objects.filter(
                        certification_date__range=[start_day, end_day],
                        challenge_participant_id__exact=profile.pk,
                    )
                    fail_number = frequency - len(success_certification)

            return fail_number

        def certification_photo():
            qs = ChallengeCertification.objects.filter(
                challenge_participant_id__exact=profile.pk,
                challenge_id__exact=challenge,
            )
            ww = []
            for i in qs:
                serializer = ChallengeCertificationSerializer(i)
                ww.append(serializer.data)

            return ww

        def challenge_query():
            queryset = self.get_object()
            serializer = self.serializer_class(queryset).data
            return serializer

        return Response(
            data={
                "challenge": challenge_query(),
                "achievement_rate": achievement_rate(),
                "success_number": success_number(),
                "fail_number": fail_number(),
                "qs": certification_photo(),
            }
        )

    @action(methods=["post", "get", "delete"], detail=True)
    def certification(self, request, pk):
        if request.method == "POST":
            decoded = JWTAuthentication.authenticate(self, request)
            challenge = Challenge.objects.filter(id=self.get_object().pk)[0]
            user = User.objects.get(id=decoded.id)
            profile = Profile.objects.filter(nickname_id=user)[0]
            image = request.data.get("file", default=None)
            ChallengeCertification.objects.create(
                challenge_id=challenge, participant_id=profile, certification_photo=image
            )

            return Response(
                data={
                    "result": "인증 성공",
                }
            )

        if request.method == "GET":
            decoded = JWTAuthentication.authenticate(self, request)
            user = User.objects.get(id=decoded.id)
            profile = Profile.objects.filter(nickname_id=user)[0]
            challenge = ChallengeApply.objects.filter(challenge_id=self.get_object().pk)
            certification_data = ChallengeApply.objects.filter(member_id=profile)[
                0
            ].certification_challenge.all()

            serializer = ChallengeCertificationSerializer(certification_data, many=True)
            return Response(data=serializer.data)

        if request.method == "DELETE":
            certification_id = request.GET.get("certification_id", None)
            print(certification_id)
            # decoded = JWTAuthentication.authenticate(self, request)
            search_certification = ChallengeCertification.objects.filter(
                certification_id=certification_id
            )
            search_certification.delete()
            return Response(data={"result": "인증을 삭제했습니다."})

        def certification_feed_save(success_certification):
            if len(success_certification) < frequency:
                serializer = ChallengeCertificationSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
            else:
                return Response(data={"result": "이번주 인증은 모두 완료했습니다."})
            return Response(data={"인증 성공"})

    @action(methods=["get"], detail=False)
    def my_certifications(self, request):
        decoded = JWTAuthentication.authenticate(self, request)
        # challenge_id = request.GET.get("challenge_id")
        certifications = ChallengeCertification.objects.filter(participant_id_id=decoded.id)
        serializer = ChallengeCertificationSerializer(certifications, many=True)
        """ applied_challenges = Challenge.objects.filter(member_id_id=decoded.id).prefetch_related(
            "challenge_id", "certification_challenge"
        )[0]
        certifications = applied_challenges.certification_challenge.all() """
        serializer = ChallengeCertificationSerializer(certifications, many=True)
        return Response(serializer.data)

    """ @action(methods=["get"], detail=True)
    def my_certification_detail(self, request, pk):
        decoded = JWTAuthentication.authenticate(self, request)
        # challenge_id = request.GET.get("challenge_id")
        applied_challenges = Challenge.objects.filter(member_id_id=decoded.id).prefetch_related(
            "challenge_id", "certification_challenge"
        )[0]
        profile = Profile.objects.filter(nickname_id_id=decoded.id)
        my_certification

        serializer = ChallengeCertificationSerializer(certifications, many=True)
        return Response(serializer.data) """

    """     
        system_currnet_time = datetime.now().replace(tzinfo=timezone("Asia/Seoul"))
        start_day = challenge.start_day
        end_day = start_day + timedelta(days=7)
        for _ in range(durations + 1):
            if system_currnet_time < end_day:
                success_certification = ChallengeCertification.objects.filter(
                    certification_date__range=[start_day, end_day],
                    challenge_participant_id__exact=user,
                )
            elif system_currnet_time > end_day:
                start_day = start_day + timedelta(days=7)
                end_day = start_day + timedelta(days=7)
        return certification_feed_save(success_certification)
        """
