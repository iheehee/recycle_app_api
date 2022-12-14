from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate

# from .authenticate import EmailAuthenticate
from django.contrib.auth.password_validation import validate_password
from .models import User, Profile
from challenges.serializers import ChallengeApplySerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
        )
        exclude = (
            "password",
            "groups",
            "user_permissions",
        )
        read_only_fields = ("id",)


class RelatedUserSerializer(serializers.ModelSerializer):

    nickname = serializers.CharField()

    class Meta:
        model = User
        fields = (
            "id",
            "nickname",
        )


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    password = serializers.CharField(write_only=True, validators=[validate_password])

    class Meta:
        model = User
        field = ("password", "email")
        exclude = ("username", "is_superuser", "is_staff", "groups", "user_permissions")

    def create(self, validated_data):
        user = User.objects.create(**validated_data, is_active=False)
        return user


class LoginSerializer(serializers.Serializer):
    """로그인"""

    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, obj):
        username = obj.get("email")
        password = obj.get("password")
        if not (username and password):
            raise serializers.ValidationError()
        user = authenticate(username=username, password=password)
        try:
            obj["user"] = user.id
            return obj
        except AttributeError:
            obj["user"] = None
            return obj


class UserInfoUpdateSerializer(serializers.ModelSerializer):
    """회원정보 수정"""

    nickname = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        field = ("nickname",)
        exclude = (
            "username",
            "is_superuser",
            "is_staff",
            "groups",
            "user_permissions",
            "password",
            "last_login",
            "is_active",
            "date_joined",
        )
        read_only_fields = ("id", "email")

    def update(self, instance, validated_data):
        instance.nickname = validated_data.get("nickname", instance.nickname)
        instance.save()
        return instance


class ProfileSerializer(serializers.ModelSerializer):

#    my_challenges = ChallengeApplySerializer(many=True)    
    
    class Meta:
        model = Profile
        field = (
            "nickname",
            "avatar",
            "my_challenges",
        )

        read_only_fields = ("id",)
        exclude = ()
        