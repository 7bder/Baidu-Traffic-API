# 定义匹配字符的类，3个参数(路径,start字符,end字符)
import requests
import pandas as pd
import json
import re

# 正则表达式提取字符
class extract_content_2words(object):
    lines = 0

    def __init__(self, path, word1, word2):
        self.path = path
        self.word1 = word1
        self.word2 = word2

    def key_match(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            buffer = f.read()
            # 定义正则表达式规则pattern
            pattern = re.compile(self.word1+'(.+?)'+self.word2)
            result = pattern.findall(buffer)
        if result != []:
            return result
        else:
            print('没有找到')
            return None

# 百度实时路况类
class get_traffic_BaiduAPI(object):
    def __init__(self):
        self.ak="FWYMgKbGtLlVSutqWqRQPSOMRKQvAika"
        self.path = 'd:/test/'
        self.traffic_list = []
        self.get_type_list = {'center': 'http://api.map.baidu.com/traffic/v1/around',
                              'road_name': 'https://api.map.baidu.com/traffic/v1/road',
                              'bounds': 'http://api.map.baidu.com/traffic/v1/bound'}

        # 不同类型实时路况的参数表定义
        self.params = {'center': {'ak': self.ak,
                                  'center': '',
                                  'radius': 500},
                       'bounds': {'ak': self.ak,
                                  'bounds': '',
                                  'coord_type_input': 'wgs84'},
                       'road_name': {'ak': self.ak,
                                     'road_name': '',
                                     'city': '郑州市'}}

    # 获取实时路况的方法
    def get_traffic(self, get_type: str, path: str, file_read: str, file_write: str = 'export', around_radius: int = 2000,
                    ak: str = "FWYMgKbGtLlVSutqWqRQPSOMRKQvAika", city: str = '郑州市') -> list:
        if path != None: self.path = path
        if ak != None: self.ak = ak
        # 不同类型实时路况的参数表更新
        self.params[get_type]['ak'] = self.ak
        self.params[get_type]['radius'] = around_radius
        self.params[get_type]['city'] = city
        # 变量初始化

        # Web API调用url
        get_ulr = self.get_type_list[get_type]
        # 文件操作
        file_read = self.path + file_read
        file_write = self.path + file_write
        # 读取坐标/路名list
        with open(file_read, 'r', encoding='utf-8') as f_read:
            lines = f_read.readlines()
        # 读取并写入路况
        with open(file_write, 'w',encoding='utf-8') as f_write:
            for line in lines:
                # 删掉'\n'，空格等
                self.params[get_type][get_type] = line.strip()
                # 更新参数表中的坐标，并获取实时路况
                traffic = requests.get(get_ulr, self.params[get_type])
                f_write.write(traffic.text+'\n')
                self.traffic_list.append(traffic)
        # 返回一个列表
        return self.traffic_list

    # 提取爬取返回的json中特定内容，截取两个指定字符串之间的字符串
    def extract_content_2words(self, path: str, file_read: str, word_start: str, word_end: str) -> list:
        if path != None: self.path = path
        with open(self.path+file_read, 'r', encoding='utf-8') as f:
            data = f.read()
            # 定义正则表达式规则pattern
            pattern = re.compile(word_start+'(.+?)'+word_end)
            result = pattern.findall(data)
        if result != []:
            return result
        else:
            print('没有找到')
            return None

    def split_data(self,path: str,file_read:str,file_write:str,split_column:str,
                    encoding:str='utf-8'):
        if path != None: self.path = path
        # 转为DataFrame,写入新的excel
        with open(self.path+file_read,'r',encoding=encoding) as f:
            df = pd.DataFrame([json.loads(line) for line in f.readlines()])
        # 重新写入和读取excel
        df.to_excel(path+file_write)
        df = pd.read_excel(path+file_write)

        # 新建一个writer，以写入同一个excel的两个sheet
        with pd.ExcelWriter(self.path+file_write) as writer:
            # 写入sheet1
            df.to_excel(writer,sheet_name=split_column)
            # 拆分列，需要重新从excel读取，否则无法正常拆分
            data_split = df[split_column].str.split(',', expand=True).stack().reset_index()
            # 重建表头
            data_split.columns = ['index','sub_level',split_column]
            # 写入sheet2
            data_split.to_excel(writer,sheet_name='splited_'+split_column)
        return data_split



# 参数列表示例，全部txt文件
# around: 34.73099,113.663766
# bounds: 34.8016727538665,113.509601745876;34.8090927538665,113.518584745876
            # 左下坐标，右上坐标
# road_name: 中州大道


# 调用示例：获取实时路况
# test = get_traffic_BaiduAPI()
# test.get_traffic(get_type='bounds', path='C:/Users/chenq/Desktop/新建文件夹/',
#                  file_read='10-traffic-by-bounds.txt')
# test.extract_content_2words(file_read='1-road_name.txt',word_start=":'",word_end="'")


# 调用示例：正则表达式提取字符
# file_path = 'C:/Users/chenq/Desktop/新建文件夹/'
# word1 = ":'"
# word2 = "'"
# matchWords = extract_content_2words(file_path+'1-road_name.txt', word1, word2)
# data = matchWords.key_match()

