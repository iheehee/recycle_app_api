from rest_framework import serializers
from rest_fremework.validators import UniqueValidator
from 
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "favs",
        )
        exclude = ()
        read_only_fields = ("id", "favs")

class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        field = ('username', 'password','email')

    def create(self, validated_data):





