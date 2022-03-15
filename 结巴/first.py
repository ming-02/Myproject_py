#结巴分词初次尝试
import  random
checkcode = ''
for i in range(4):#循环4次输出四个字符
    index = random.randrange(0,4)
    if index != i and index+1 != i:
        checkcode += chr(random.randint(97,122))#小写字母ASCII值为：97~122
    elif index+1 == i:
        checkcode += chr(random.randint(65,90))#大写字母ASCII值为：65~90
    else:
        checkcode += str(random.randint(0,9))#随机输出数字0~9中的1个
print("当前验证码为：",checkcode)
