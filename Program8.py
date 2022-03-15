#英文文章中的词频统计。使用input函数输入一篇英文文章，统计该文章中各单词出现的次数并输出。
Str=input("请输入一遍英文文章")
import re
# Str='a best man,a?good man,good good study.'
print(re.split("\s|;|,|\?", Str))
str1=re.split("\s|;|,|\?", Str)
i=0
List3={}
list1=[]
for S in range(len(str1)):
    # print(str1[S])
    i = 0
    for SS in range(len(str1)):
        # print(str1[SS])
        if str1[S]==str1[SS]:
            i=i+1
    print("词{}，频数{}".format(str1[S], i))
    list1.append(str1[S])
    # print(list1)
List3=list(set(list1))
# print(List3)
