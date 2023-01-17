import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from django.db import IntegrityError
from .models import Category, Shop, Borough
from .serializers import ShopSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 1000


class MapViewSet(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    pagination_class = StandardResultsSetPagination

    def get_serializer_class(self):
        if self.action == "list":
            return ShopSerializer
        if self.action == "retrieve":
            return ShopSerializer
        return super().get_serializer_class()

    def get_permissions(self):

        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return super().get_permissions()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, content={"성공입니다."})

    def list(self, request, *args, **kwargs):
        queryset = Shop.objects.all()
        shop_queryset = self.filter_queryset(queryset)
        borough_queryset = Borough.objects.all()
        category_queryset = Category.objects.all()
        page = self.paginate_queryset(shop_queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(shop_queryset, many=True)
        return Response(
            data={
                "shop": serializer.data,
                "borough": borough_queryset,
                "category": category_queryset,
            }
        )


class MapUpdate(APIView):

    permission_classes = [AllowAny]

    def get(self, request):
        def update_map():
            key = "f79ef2eeb2b947f9bf3510e0e848a2be"
            response = requests.get(
                f"https://map.seoul.go.kr/smgis/apps/theme.do?cmd=getContentsList&key={key}&page_size=999&page_no=1&coord_x=126.974695&coord_y=37.564150&distance=100000&search_type=0&search_name=&theme_id=11103395&content_id=&subcate_id="
            )
            results = response.json()
            return save_map_data(results)

        def save_map_data(results):
            api_result = results["body"]
            borough_all = Borough.objects.all()
            shop_kwards = {}
            update_count = 0
            for i in range(len(api_result)):
                """부정확한 데이터(카페)를 제외하고 저장"""
                if api_result[i]["COT_THEME_SUB_ID"] != str(1):

                    shop_kwards["name"] = api_result[i]["COT_CONTS_NAME"]
                    shop_kwards["address"] = api_result[i]["COT_ADDR_FULL_NEW"]
                    shop_kwards["tel"] = api_result[i]["COT_TEL_NO"]
                    shop_kwards["lat"] = api_result[i]["COT_COORD_Y"]
                    shop_kwards["lng"] = api_result[i]["COT_COORD_X"]
                    shop_kwards["image"] = api_result[i]["COT_IMG_MAIN_URL"]

                    def fk_add_category(i):
                        category_id = api_result[i]["COT_THEME_SUB_ID"]
                        category = Category.objects.filter(id__exact=category_id)[0]
                        return category

                    def fk_add_borough():
                        address = shop_kwards["address"]

                        for i in borough_all:
                            if str(i) in address:
                                return i

                    try:
                        Shop.objects.create(
                            **shop_kwards,
                            category_id=fk_add_category(i),
                            borough_id=fk_add_borough(),
                        )
                        update_count += 1
                    except IntegrityError:
                        pass

            return update_count

        return Response(data={"update_count": update_map()})
