import jwt
from django.conf import settings
from rest_framework import authentication
from rest_framework import exceptions
from users.models import User


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        print("난 작동하고 있어")
        token = request.META.get("HTTP_AUTHORIZATION")
        try:
            if token is None:
                return None
            xjwt, jwt_token = token.split(" ")
            decoded = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=["HS256"])
            pk = decoded.get("pk")
            user = User.objects.get(pk=pk)

            return (user, None)

        except jwt.exceptions.DecodeError:
            return exceptions.AuthenticationFailed(detail="JWT Format Invalid")
