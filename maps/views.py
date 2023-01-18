import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.decorators import action
from rest_framework import status, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from django.db import IntegrityError
from .models import Category, Shop, Borough
from .serializers import ShopSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response(
            {
                "links": {"next": self.get_next_link(), "previous": self.get_previous_link()},
                "count": self.page.paginator.count,
                "results": data,
            }
        )


class MapViewSet(generics.ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    pagination_class = StandardResultsSetPagination

    def list(self, request, *args, **kwargs):
        # shop_queryset = self.filter_queryset(queryset)
        shop_queryset = Shop.objects.all()
        borough_queryset = Borough.objects.all()
        category_queryset = Category.objects.all()

        serializer = ShopSerializer(shop_queryset, many=True)
        page = self.paginate_queryset(shop_queryset)
        paginated_data = self.get_serializer(page, many=True)

        def b(queryset):
            bb = [queryset[i].borough for i in range(len(borough_queryset))]
            return bb

        print(paginated_data)
        """if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(shop_queryset, many=True)"""

        return Response(
            data={"borough": b(queryset=borough_queryset), "shop": paginated_data.data}
            # "shop": serializer.data,
            # "category": category_queryset,
        )

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    """def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, content={"성공입니다."})"""


class MapUpdate(APIView):

    permission_classes = [AllowAny]

    def get(self, request):
        def update_map():
            key = "f79ef2eeb2b947f9bf3510e0e848a2be"
            response = requests.get(
                f"https://map.seoul.go.kr/smgis/apps/theme.do?cmd=getContentsList&key={key}&page_size=999&page_no=1&coord_x=126.974695&coord_y=37.564150&distance=100000&search_type=0&search_name=&theme_id=11103395&content_id=&subcate_id="
            )
            results = response.json()
            update_count = 0

            def save_map_data(results):
                api_result = results["body"]
                borough_all = Borough.objects.all()
                shop_kwards = {}

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
                            return update_count + 1

                        except IntegrityError:
                            pass

                return save_map_data(results)

            return update_count

        return Response(data={"update_count": update_map()})
