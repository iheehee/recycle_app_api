import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import IntegrityError
from .models import Category, Shop, Borough


class MapUpdate(APIView):
    def get(self, request):
        def map_request():
            key = "f79ef2eeb2b947f9bf3510e0e848a2be"
            response = requests.get(
                f"https://map.seoul.go.kr/smgis/apps/theme.do?cmd=getContentsList&key={key}&page_size=10&page_no=1&coord_x=126.974695&coord_y=37.564150&distance=100000&search_type=0&search_name=&theme_id=11103395&content_id=&subcate_id="
            )
            results = response.json()
            return save_map_data(results)

        def save_map_data(results):
            api_result = results["body"]
            borough_all = Borough.objects.all()
            shop_kwards = {}

            for i in range(len(api_result)):
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
                        **shop_kwards, category_id=fk_add_category(i), borough_id=fk_add_borough()
                    )
                except IntegrityError:
                    pass

            return shop_kwards

        return Response(data=map_request())
