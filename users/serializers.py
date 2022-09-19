from dataclasses import field
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
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
        exclude = ('password',)
        read_only_fields = ("id", "favs")


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        field = ('username', 'password','email')
        exclude = ()
    
    def create(self, validated_data):
        user = User.objects.create(**validated_data, is_active=False)
        return user

class LoginSerializer(serializers.Serializer):
    """로그인"""
    #email = serializers.EmailField()
    password = serializers.CharField()
    username = serializers.CharField(style={'input_type': 'password'})

    def validate(self, obj):
        username = obj.get('username')
        #email = obj.get('email')
        password = obj.get('password')
        if not (username and password) :
            raise serializers.ValidationError()
        user = authenticate(username=username, password=password)
        obj['user'] = user
        return obj

    







