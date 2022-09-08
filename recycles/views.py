from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.decorators import action
from .serializers import RecycleSerializer
from .models import Recycle


class RecycleViewSet(viewsets.ModelViewSet):

    queryset = Recycle.objects.all()
    serializer_class = RecycleSerializer

    def get_permissons(self):
        
        if self.action == "list" or self.action == "retrieve":
            permission_classes = [AllowAny]
        elif self.action == "create" or self.action == "update":
            permission_classes = [IsAdminUser]
        else:
            pass
        return [permission() for permission in permission_classes]

    @action(detail=False, permission_classes=[AllowAny])
    def search(self, request):

        recycle = request.GET.get("name", None)
        filter_kwarg = {}
        filter_kwarg["name"] = recycle
        recycles = Recycle.objects.filter(**filter_kwarg)
        if len(recycles) == 0:
            return Response({"dd": "값이 없습니다."})
        else:
            serializer = RecycleSerializer(recycles, many=True)
        return Response(serializer.data)
