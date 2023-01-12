import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Shop


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
            lists = results["body"]
            maps_kwards = {}
            for i in range(len(lists)):
                maps_kwards["name"] = lists[i]["COT_CONTS_NAME"]
                maps_kwards["address"] = lists[i]["COT_ADDR_FULL_NEW"]
                maps_kwards["tel"] = lists[i]["COT_TEL_NO"]
                maps_kwards["lat"] = lists[i]["COT_COORD_Y"]
                maps_kwards["lng"] = lists[i]["COT_COORD_X"]
                maps_kwards["image"] = lists[i]["COT_IMG_MAIN_URL"]
                maps_kwards["category_id"] = lists[i]["COT_THEME_SUB_ID"]

            """try:
                Shops.objects.create(**maps_kwards)
            except:
                pass"""
            return maps_kwards

        return Response(data=map_request())
