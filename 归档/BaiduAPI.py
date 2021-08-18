# 导入包
import requests
import pandas as pd
import json

# 变量初始化
ak = "FWYMgKbGtLlVSutqWqRQPSOMRKQvAika"
url_traffic_around = "http://api.map.baidu.com/traffic/v1/around"
url_restrict = 'http://api.map.baidu.com/api_region_search/v1/?'
url_place = 'http://api.map.baidu.com/place/v2/search?'
url_traffic_bound = 'http://api.map.baidu.com/traffic/v1/bound'
file_path = "C:/Users/chenq/Desktop/新建文件夹/"

place_query = '道路'
place_region = 268
place_tag = '道路'
place_output = 'json'
place_num = 0

traffic_center = '34.73099,113.663766'
traffic_radius = 2000
traffic_bounds = "34.786852,113.671298;34.794272,113.680281"
traffic_road_grade = 0
traffic_coord_type_input = 'wgs84'
traffic_coord_type_output = 'wgs84'


# 变量初始化
params_restrict = {'keyword': '郑州市',
                   'ak': ak,
                   'sub_admin': 3}
params_traffic_around = {'ak': ak,
                         'center': traffic_center,
                         'radius': traffic_radius}
params_place = {'ak': ak,
                'query': place_query,
                'tag': place_tag,
                'region': place_region,
                'output': place_output,
                'scope': 2,
                'page_size': 20,
                'page_num': place_num
                }
params_traffic_bound = {'ak': ak,
                        'bounds': traffic_bounds,
                        'coord_type_input': traffic_coord_type_input
                        }

# 执行
# r_restrict = requests.get(url_restrict,params_restrict)
# r_place = requests.get(url_place,params_place)
# r_traffic_around = requests.get(url_traffic_around,params_traffic_around)
# r_traffic_bound = requests.get(url_traffic_bound,params_traffic_bound)


# print(r_restrict.text)
# print(r_place.text)
# print(r_traffic_bound.text)

file_read = file_path+'in-coordinate.txt'
file_write = file_path+'0-路况.txt'

# 读取经纬度
with open(file_read, 'r', encoding='utf-8') as f_read:
    lines = f_read.readlines()

#i = 0
with open(file_write, 'w') as f_write:
    for line in lines:
        #i = i+1
        params_traffic_bound['bounds'] = line.strip()
        r_traffic_bound = requests.get(url_traffic_bound, params_traffic_bound)
        f_write.write(r_traffic_bound.text+'\n')
        #if i > 5 : break

