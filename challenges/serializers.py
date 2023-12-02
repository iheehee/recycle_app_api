from .models import (
    Challenge,
    ChallengeApply,
    ChallengeCertification,
    SuccessPhotoExample,
    FailPhotoExample,
)

# from users.serializers import RelatedUserSerializer
from rest_framework import serializers
from core.authentication import JWTAuthentication


class SuccessPhotoExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuccessPhotoExample
        fields = (
            "id",
            "challenge_name",
            "success_photo",
            "owner",
        )
        read_only_fields = ("id",)


class ChallengeSerializer(serializers.ModelSerializer):
    # success_photo_example = SuccessPhotoExampleSerializer(many=True, read_only=True)

    class Meta:
        model = Challenge
        fields = (
            "id",
            "title",
            "owner",
            "title_banner",
            "summery",
            "description",
            "start_day",
            "frequency",
            "duration",
            "success_photo_example",
            "fail_photo_example",
            "certification_notice",
            "member",
            "max_member",
            "number_of_applied_member",
        )
        read_only_fields = ("id",)


class ChallengeCreateSerializer(serializers.ModelSerializer):
    # success_photo_example = SuccessPhotoExampleSerializer(many=True)
    # member = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Challenge
        fields = (
            "id",
            "title",
            "title_banner",
            "summery",
            "description",
            "summery",
            "description",
            "start_day",
            "frequency",
            "duration",
            "certification_notice",
            "certifications_start_time",
            "certifications_end_time",
            "member",
            "max_member",
            "owner",
        )
        read_only_fields = ("id",)

    def create(self, validated_data):
        user = self.context["user"]
        profile = user.profile.first()
        title_banner = self.context["request"].data.get("title_banner", None)
        challenge = Challenge.objects.create(
            **validated_data, owner=user, title_banner=title_banner
        )
        ChallengeApply.objects.create(challenge_id=challenge, member_id=profile)
        # challenge.member.add(user.id)
        success_photo = self.context["request"].data.get("success_photo", None)
        fail_photo = self.context["request"].data.get("fail_photo", None)
        data = {
            "challenge_name": challenge.id,
            "owner": user.id,
        }

        if success_photo != None:
            data["success_photo"] = success_photo
            serializer = SuccessPhotoExampleSerializer(data=data)
            if serializer.is_valid():
                create_success_photo = serializer.save()
                challenge.success_photo_example.add(create_success_photo)
            data.pop("success_photo")
        if fail_photo != None:
            data["fail_photo"] = fail_photo
            serializer = FailPhotoExampleSerializer(data=data)
            if serializer.is_valid():
                create_fail_photo = serializer.save()
                challenge.fail_photo_example.add(create_fail_photo)

        return challenge


class ChallengeApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = ChallengeApply
        fields = (
            "id",
            "challenge_id",
            "member_id",
        )
        read_only_fields = ("id",)


class ChallengeCertificationSerializer(serializers.ModelSerializer):
    participant_id = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ChallengeCertification
        fields = (
            "certification_id",
            "challenge_id",
            "certification_date",
            "certification_photo",
            "certification_comment",
            "participant_id",
        )

    def create(self, validated_data):
        user = self.context["user"]
        profile = user.profile.first()
        certification = ChallengeCertification.objects.create(
            **validated_data, participant_id=profile
        )
        return certification


class SuccessPhotoExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuccessPhotoExample
        fields = (
            "id",
            "challenge_name",
            "success_photo",
            "owner",
        )
        read_only_fields = ("id",)

    def create(self, validated_data):
        success_photo = SuccessPhotoExample.objects.create(**validated_data)
        return success_photo


class FailPhotoExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = FailPhotoExample
        fields = (
            "id",
            "challenge_name",
            "fail_photo",
            "owner",
        )
        read_only_fields = ("id",)

    def create(self, validated_data):
        fail_photo = FailPhotoExample.objects.create(**validated_data)
        return fail_photo
