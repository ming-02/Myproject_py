#爬取纺大新闻网上的一条新闻，提取该新闻中的高频词和关键字
import requests
from bs4 import  BeautifulSoup
import jieba
import jieba.analyse
head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
hc=requests.get(url="https://news.wtu.edu.cn/info/1004/28166.htm",headers=head)#获取网页请求
hc.encoding='utf-8'#编码格式
soup=BeautifulSoup(hc.text,"html.parser")#创建包含网页内容的字符串创建beautifulSoup对象
cont=soup.find('div',{'id':'vsb_content_2'}).text#定位内容
wordlist=jieba.lcut(cont)#jieba 精确模式分词
wd={}
for w in wordlist:
    wd[w]=wd.get(w,0)+1
wd=list(wd.items())
wd=sorted(wd,key=lambda  x:x[1],reverse=True)
print(wd[:100])
wk=jieba.analyse.extract_tags(cont,10)
print(wk)

