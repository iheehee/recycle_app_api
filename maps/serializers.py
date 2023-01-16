from .models import Shop
from rest_framework import serializers


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = (
            "id",
            "name",
            "address",
            "tel",
            "lat",
            "lng",
            "image",
            "category_id",
            "borough_id",
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
            "certification_success_photo_example",
            "certification_fail_photo_example",
            "certification_notice",
            "max_member",
        )


class ChallengeApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = ChallengeApply
        fields = (
            "id",
            "challenge_name",
            "member_name",
        )
        read_only_fields = ("id",)


class ChallengeCertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChallengeCertification
        fields = (
            "challenge_id",
            "challenge_participant_id",
            "certification_date",
            "certification_photo",
            "certification_comment",
        )

    def create(self, validated_data):
        certification = ChallengeCertification.objects.create(**validated_data)
        return certification
