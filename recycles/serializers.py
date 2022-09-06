from .models import Recycle
from rest_framework import serializers


class RecycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recycle
        fields = (
            "name",
            "how_to_recyle",
            "tip",
            "category",
            "category_photo",
        )
