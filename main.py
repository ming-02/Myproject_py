#-*- coding = utf-8 -*-
#@Time：2020-08-15 22:41
#@Author：来瓶安慕嘻
#@File：全国各省数据爬取.py
#@开始美好的一天吧 @Q_Q@

import json
import requests
import xlwt
import re
import os
from collections import Counter

if __name__ == "__main__":
    if not os.path.exists('./全国各地疫情数据'):
        os.mkdir('./全国各地疫情数据')

    # 全国省份
    # province_name = ['北京', '上海', '江苏', '广东', '浙江', '陕西', '山西','河北','河南','湖北','湖南','安徽','山东','重庆','四川','辽宁',
    #                  '吉林','黑龙江','天津','福建','云南','贵州','青海','海南','西藏','广西','宁夏','甘肃','新疆','内蒙古','江西']
    province_name = ['美国',]

    for item in range(len(province_name)):
        province = province_name[item]
        url = 'https://api.inews.qq.com/newsqa/v1/query/pubished/daily/list?province='
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
        }#头部
        data = {
            'province': province
        }
        page_text = requests.post(url=url, data=data, headers=headers).json()
        # fileName = province+'.json'
        # fp = open(fileName,'w',encoding='utf-8')
        # json.dump(page_text,fp=fp,ensure_ascii=False)
        data = page_text['data']
        # print(data)
        date_num = len(data)  # 计算总共的天数

        book = xlwt.Workbook(encoding='utf-8')
        sheet = book.add_sheet('疫情数据', cell_overwrite_ok=True)
        col_name = ['省份', '日期', '累计确诊', '累计死亡', '累计治愈', '境外输入']
        for i in range(0, 6):
            sheet.write(0, i, col_name[i])

        for i in range(date_num):
            sheet.write(i + 1, 0, province)
            y = data[i]['date'].split('.')[0]
            m = data[i]['date'].split('.')[1]
            p = str(data[i]['year'])
            sheet.write(i + 1, 1, p+'年'+y+'月'+m+'日')
            sheet.write(i + 1, 2, data[i]['confirm'])
            sheet.write(i + 1, 3, data[i]['dead'])
            sheet.write(i + 1, 4, data[i]['heal'])
            sheet.write(i + 1, 5, 0)

            # 提取境外输入病例
            ex = '确诊病例(.*?)例|新增(.*?)例|输入病例(.*?)例'
            match = re.findall(ex, data[i]['description'])
            if len(match) == 0:
                sheet.write(i + 1, 5, 0)
            elif match[0][0].isalnum():
                sheet.write(i + 1, 5, float(match[0][0]))
                # print(match[0])


        print('%s   爬取结束'%province)

        book.save('./全国各地疫情数据/'+province + '疫情数据' + '.xls')

    print('爬取结束----')
