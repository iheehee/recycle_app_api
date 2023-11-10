from .models import (
    Challenge,
    ChallengeApply,
    ChallengeCertification,
    SuccessPhotoExample,
)

# from users.serializers import RelatedUserSerializer
from rest_framework import serializers


class SuccessPhotoExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuccessPhotoExample
        fields = (
            "id",
            "success_photo_example",
        )
        read_only_fields = ("id",)


class ChallengeSerializer(serializers.ModelSerializer):
    success_photo_example = SuccessPhotoExampleSerializer(many=True, read_only=True)

    class Meta:
        model = Challenge
        fields = (
            "id",
            "title",
            "owner",
            "title_banner",
            "challenge_summery",
            "challenge_description",
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
    class Meta:
        model = Challenge
        fields = (
            "id",
            "title",
            "owner",
            "title_banner",
            "challenge_summery",
            "challenge_description",
            "start_day",
            "frequency",
            "duration",
            "certification_notice",
            "max_member",
        )


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
    class Meta:
        model = ChallengeCertification
        fields = (
            "certification_id",
            "challenge_id",
            "participant_id",
            "certification_date",
            "certification_photo",
            "certification_comment",
        )

    def create(self, validated_data):
        certification = ChallengeCertification.objects.create(**validated_data)
        return certification
