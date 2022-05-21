# Preserving parentheses and grouping

import re

# text = "lat = 5, lon=72, a= 123, lon=7212, lat =\t4, lon=123"
#
# print(re.findall(r"(?:lat|lon)\s*=\s*(\d+)", text))
# print(re.findall(r"(?:lat|lon)\s*=\s*(\d*?)", text))
#
# res =re.findall(r"(lat|lon)\s*=\s*(\d+)", text)
# print(dict(res))
#
# text = "Картинка <img src='bg.jpg'> в тексте</p>"
#
# # print(re.findall(r"<img\s+.*src=[\'\"](.*)[\'\"]", text))
# # print(re.findall(r"<img\s+.*src=([\'\"])(.*?)\1", text))
#
# # (?P<name>…) ... (?P=name)
# print(re.findall(r"<img\s+.*src=(?P<name1>[\"\'])(.+?)(?P=name1)", text))


# task with .xml file

# variant-1
# with open("lesson-3.xml", "r") as f:
#     lon = []
#     lat = []
#     for i in f:
#         res = re.findall(r"<point\s+lon=([\"\'])(.+)\1\s+lat=([\"\'])(.+)\1/>", i)
#         print(res)

# variant-2
with open("lesson-3.xml", "r") as f:
    lon = []
    lat = []
    for i in f:
        res = re.search(r"<point\s+lon=([\"\'])(?P<lon>.*)\1\s+lat=([\"\'])(?P<lat>.*)\1", i)
        print(res)
        if res:
            v = res.groupdict()
            if "lon" in v and "lat" in v:
                lon.append(v["lon"])
                lat.append(v["lat"])
    print(lon, lat, sep="\n")
