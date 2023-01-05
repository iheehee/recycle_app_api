
key = "f79ef2eeb2b947f9bf3510e0e848a2be"
dd = []
response = requests.get(
"https://map.seoul.go.kr/smgis/apps/theme.do?cmd=getContentsList&key=f79ef2eeb2b947f9bf3510e0e848a2be&page_size=50&page_no=1&coord_x=126.974695&coord_y=37.564150&distance=2000&search_type=0&search_name=&theme_id=11103395&content_id=&subcate_id=")
result=dd.append(response.json())
print(result)