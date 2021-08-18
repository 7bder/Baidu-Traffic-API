import mylib
import pandas as pd

# 建立一个百度实时路况的实例
test = mylib.get_traffic_BaiduAPI()

# 获取实时路况，bounds类型，
test.get_traffic(get_type='bounds',path='C:/Users/chenq/Desktop/test/',
                    file_read='新建文本文档.txt',file_write='traffic_bounds_500m.txt')

# # 以下为提取所有道路名称
# # 将获取得到的数据进行分列
# test.split_data(path='C:/Users/chenq/Desktop/test/',
#                 file_read='traffic_bounds.txt',file_write='road_name.xlsx',split_column='road_traffic')

# # 转为csv，后用正则计算匹配道路名称
# df = pd.read_excel('C:/Users/chenq/Desktop/test/road_name.xlsx',sheet_name='splited_road_traffic')
# df.to_csv('C:/Users/chenq/Desktop/test/road_name.csv',encoding='utf-8')

# # 正则计算提取道路名
# road_name = test.extract_content_2words(path='C:/Users/chenq/Desktop/test/',file_read='road_name.csv',
#                                         word_start="{'road_name': '",word_end="'")

# # 提取出的道路名写入文件
# with open('C:/Users/chenq/Desktop/test/road_name.txt','w',encoding='utf-8') as f:
#     for line in road_name:
#         f.writelines(line+'\n')