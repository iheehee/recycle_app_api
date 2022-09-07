from django.contrib.auth import authenticate
from rest_framwork.viewsets import ModelViewSet
from rest_framwork.decorators import action
from rest_framwork.permissions import IsAdminUser, AllowAny
from rest_framwork import status

class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [IsAdminUser]
        else self.action == "retrieve":
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    @action(detail=False, method=["post"])
    def login(self, request):
        pass