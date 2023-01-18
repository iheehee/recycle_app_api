from .models import Borough, Shop
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


class BoroughSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borough
        fields = ("borough",)
        read_only_fields = ("id",)
