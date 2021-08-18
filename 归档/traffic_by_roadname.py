import requests

ak = "FWYMgKbGtLlVSutqWqRQPSOMRKQvAika"
url_traffic_by_roadname= 'https://api.map.baidu.com/traffic/v1/road'
file_path = "C:/Users/chenq/Desktop/新建文件夹/"
input_roadname = ''
traffic_by_roadnames=[]
input_roadnames = []

params_roadname={'ak': ak,
                    'road_name': input_roadname,
                    'city': '郑州市'}

# 读取路名
with open(file_path+'9-全市范围路名.txt', 'r', encoding='utf-8') as f_read:
    input_roadnames = f_read.readlines()

# 用路段读取交通量，并写入文件
with open(file_path+'10-traffic-by-road.txt','w',encoding='utf-8') as f_write:
    for input_roadname in input_roadnames:
        params_roadname['road_name'] = input_roadname.strip()
        traffic_by_roadname = requests.get(url_traffic_by_roadname, params_roadname)
        f_write.write(traffic_by_roadname.text+'\n')
        traffic_by_roadnames.append(traffic_by_roadname)
    