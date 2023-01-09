import requests
from rest_framework.views import APIView
from rest_framework.response import Response


class SearchShop(APIView):
    def map_data(self, page):
        "서울시 맵데이터 api 호출"
        key = "f79ef2eeb2b947f9bf3510e0e848a2be"
        response = requests.get(
            f"https://map.seoul.go.kr/smgis/apps/theme.do?cmd=getContentsList&key={key}&page_size=10&page_no={page}&coord_x=126.974695&coord_y=37.564150&distance=100000&search_type=0&search_name=&theme_id=11103395&content_id=&subcate_id="
        )
        results = response.json()

        return results


    def get(self, request):
        page= 1
        return Response(data=self.map_data(page))

