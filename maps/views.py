import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.decorators import action
from rest_framework import status, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from django.db import IntegrityError
from django.db.models import Q
from .models import Category, Shop, Borough
from .serializers import ShopSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 1000

    def get_paginated_response(self, data):
        results = {
            "links": {"next": self.get_next_link(), "previous": self.get_previous_link()},
            "count": self.page.paginator.count,
            "results": data,
        }

        return results


class MapViewSet(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    pagination_class = StandardResultsSetPagination

    def get_permissions(self):
        if self.action in ["list", "create", "retrieve", "search"]:
            return [AllowAny()]

        return super().get_permissions()

    def list(self, request, *args, **kwargs):
        shop_queryset = Shop.objects.all()
        borough_queryset = Borough.objects.all()
        category_queryset = Category.objects.all()

        def paginated_list(queryset):
            page = self.paginate_queryset(queryset)
            paginated_data = self.get_serializer(page, many=True).data
            paginated_response = self.get_paginated_response(data=paginated_data)
            return paginated_response

        def orderly_list(queryset):
            list = []
            for i in range(len(queryset)):
                if queryset == borough_queryset:
                    list.append(queryset[i].borough)
                elif queryset == category_queryset:
                    list.append(queryset[i].category)
            return list

        return Response(
            data={
                "borough": orderly_list(borough_queryset),
                "category": orderly_list(category_queryset),
                "shop": paginated_list(queryset=shop_queryset),
            }
        )

    @action(methods=["get"], detail=False)
    def search(self, request):
        name = request.GET.get("name", None)
        borough = request.GET.get("borough", None)
        category = request.GET.get("category", None)

        try:
            """filter_kwargs = {}
            if name is not None:
                filter_kwargs["name"] = name
            if borough is not None:
                filter_kwargs["borough"] = borough
            if category is not None:
                filter_kwargs["category"] = category
            shops = Shop.objects.filter(**filter_kwargs)"""

            # shops = Shop.objects.filter(
            #    name__icontains=name, borough_id=borough, category_id=category
            # )
            if borough is not None:
                shops = Shop.objects.filter(
                    Q(name__icontains=name) & Q(borough_id=borough) & Q(category_id=category)
                )

        except ValueError:
            shops = Shop.objects.all()
        # results = paginator.paginate_queryset(rooms, request)
        serializer = ShopSerializer(shops, many=True)
        return Response(data=serializer.data)


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

                    print(shop_kwards)
                    try:
                        Shop.objects.create(
                            **shop_kwards,
                            category_id=fk_add_category(i),
                            borough_id=fk_add_borough(),
                        )
                        update_count += 1
                    except IntegrityError:
                        update_count += 0

            return update_count
            # return save_map_data(results)

        return Response(data={"update_count": update_map()})
