import jwt
from django.conf import settings
from rest_framework import authentication
from rest_framework import exceptions
from users.models import User


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.META["HTTP_AUTHORIZATION"]
        print(token)
        try:
            if token is None:
                return None
            # xjwt, jwt_token = token.split(" ")
            decoded = jwt.decode(token, "secret", algorithms=["HS256"])
            pk = decoded.get("pk")
            user = User.objects.get(pk=pk)

            return user

        except jwt.exceptions.DecodeError:
            return exceptions.AuthenticationFailed(detail="JWT Format Invalid")
