# from users.serializers import RelatedUserSerializer

from users.serializers import ProfileSerializer
from .serializers import ChallengeCertificationSerializer


class NestedCertificationSerializer(ChallengeCertificationSerializer):
    participant_id = ProfileSerializer()
