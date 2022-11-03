from .models import Challenge
from users.serializers import RelatedUserSerializer
from rest_framework import serializers


class ChallengeSerializer(serializers.ModelSerializer):

    owner = RelatedUserSerializer()

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
            "member",
        )
        read_only_fields = ("id",)

class ChallengeMemberSerializer(serializers.ModelSerializer):


    class Meta:
        model = Challenge
        fields = (
            "member",
        )
        read_only_fields = ("id",)
