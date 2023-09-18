from .models import Challenge, ChallengeApply, ChallengeCertification, CertificationExample

# from users.serializers import RelatedUserSerializer
from rest_framework import serializers


class CertificationExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificationExample
        fields = (
            "id",
            "certification_photo_example",
            "SuccessOrFail",
        )
        read_only_fields = ("id",)


class ChallengeSerializer(serializers.ModelSerializer):
    certification_photo_example = CertificationExampleSerializer(many=True, read_only=True)

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
            "certification_photo_example",
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
            "certification_photo_example",
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
            "applied_id",
            "participant_id",
            "certification_photo",
            "certification_date",
            "certification_comment",
        )

    def create(self, validated_data):
        certification = ChallengeCertification.objects.create(**validated_data)
        return certification
