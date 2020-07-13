# a=(1,2,3,[4,5,6,7],8)
# print(a[2])  #3

# a=(1,2,3,[4,5,6,7],8)
# print(a[3][0])  #4

# def strappend(num):
#     str1='first'
#     for i in range(num):
#         str1+=str(i)
#     return str1  #不要定义叫str的变量，系统的
# print(strappend(4))

# with open('./2020510.py','rb') as py:
#     data=py.read()
# print(data) #减少打开文件后面要关闭文件，还要检测文件打开是否出错的步骤。
# with通常处理打开资源后对资源的释放工作，是对上下文管理器的调用。

# class A(object):
#     bar=1
#     def foo(self):
#         print('foo')
#     @staticmethod
#     def static_foo():
#         print('static_foo')
#         print(A.bar)
#     @classmethod
#     def class_foo(cls):
#         print('class_foo')
#         print(cls.bar)
# A.static_foo()
# A.class_foo()
# 静态方法不需要cls和self参数而类方法需要cls参数，
# 需要实例化一个对象再调用方法。

# import re
# txt="<t><a><br/><html><h1>www.baidu.com</html><html></html>"
# res=re.findall(r'\<html\>\<h1\>www\.baidu\.com\<\/html\>',txt)
# print(res)

# a=" hehheh  "
# print(a)
# print(a.strip())

# txt="hello world"
# print(txt.capitalize())

# l=[[1,2],[3,4],[5,6]]
# print(sum(l,[]))

#lambda函数是匿名函数不需要声明，方便快捷,减少代码的冗余
# f=lambda x,y: x*y
# print(f(1,2))

# txt="<html><h1>www.itcast.cn</h1></html><li></li><li></li>"
# import re
# ans=re.findall(r'\<html\>\<h1\>www\.itcast\.cn\<\/h1\>\<\/html\>',txt)
# print(ans)

# a= {1:[1,2,3]}
# b=a.copy()
# print(a)
# print(b)
# a[1].append(4)
# print(a)
# print(b)  #浅拷贝

# 深拷贝
# a={1:[1,2,3,4]}
# import copy
# b=copy.deepcopy(a)
# a[1].append(5)
# print(a)
# print(b)

# 赋值给对象增加一个标签

# .*匹配任一字符0次或多次,贪婪匹配 .*?尽可能匹配少的字符 匹配任一字符0次或多次

# a=5
# def func():
#     global a
#     a=6
#
# func()
# print(a  # 6

# import turtle, scrapy, copy, cv2, re

# 严格的缩进，不需要”；“结尾，有很多强大的库，更加简洁，功能强大，语法有一点差别。

# class d():
#     pass
# def fun():
#     pass

# global a

# 单引号定义字符串嵌套双引号，双引号定义字符串和嵌套单引号，三引号保持原样输出和嵌套单双引号
# a="'nihao'"
# print(a) # 'nihao'
#
# b='"nihao"'
# print(b) # "nihao"
#
# c=''' "nihao"  'nihao ' '''
# print(c) #  "nihao"  'nihao '

# txt='<div class="nam">中国</div>'
# import re
# res=re.findall(r'\<div class=\".*\"\>(.*?)\<\/div\>', txt)
# print(res)

# __init__是初始化函数，一创建对象就默认调用了，可以带参数
# 1、__new__至少要有一个参数cls，代表当前类，此参数在实例化时由python解释器自动识别
# 2、__new__必须有返回值，返回实例化出来的实例，这点在自己实现__new__时要特别注意，
# 可以return父类__new__出来的实例，或者直接是object的__new__出来的实例
# 3、__init__有一个参数self，就是这个__new__返回的实例，__init__在__new__的基础
# 上可以完成一些其它初始化动作，__init__不需要返回值
# 4、如果__new__创建的是当前类的实例，会自动调用__init__函数，通过return语句里面
# 调用__new__创建函数的第一个参数是cls来保证是当前实例，如果是其它类名，那么实际
# 创建返回的就是其它类的实例，其实就不会调用当前类的__init__函数，也不会调用其它类
# 的__init__函数

# a=[1,5,7,9]; b=[2,2,6,8]
# ll=a+b
# ll.sort()
# print(ll) # [1, 2, 2, 5, 6, 7, 8, 9]

# join()括号里面的是可迭代对象，x插入可迭代对象中间，形成字符串，结果一致
# x="abc"
# y="def"
# z=["d","e","f"]
# x_y=x.join(y)
# x_z=x.join(z)
# print(x_y) # dabceabcf
# print(x_z) # dabceabcf

# list=[2,3,5,4,9,6]
# new_list=[]
# def get_min(list):
#     a=min(list)
#     new_list.append(a)
#     list.remove(a)
#     if(len(list)>0):
#         get_min(list)
#     return new_list
# print(get_min(list))

# Alist=[1,2,3,1,2]
# Blist=set(Alist)
# Clist=list(Blist)
# print(Clist)

# dic={"name":"zs","age":18}
# # dic.pop("name")
# # print(dic) # {'age': 18}
# del(dic["name"])
# print(dic) # {'age': 18}

# a=(i for i in range(3))
# print(a) # <generator object <genexpr> at 0x00A13DF0>

# a="1,2,3"
# b=a.split(",")
# print(b) # ['1', '2', '3']

# listA=[1,2,3,7,8,9]
# listB=[4,5,6,7,8,9]
# listC=set(listA)&set(listB)
# listD=set(listA)-set(listB)
# listE= set(listB)-set(listA)
# listF=list(listD)+list(listE)
# print(list(listC))  # [8, 9, 7]
# print(listF)   # [1, 2, 3, 4, 5, 6]

# d1 = [
#     {'name':'alice','age':38},
#     {'name':'bob','age':18},
#     {'name':'Carl','age':28}
# ]
# res=sorted(d1,key=lambda x : x["age"],reverse=False)
# print(res)
# [{'name': 'bob', 'age': 18}, {'name': 'Carl', 'age': 28}, {'name': 'alice', 'age': 38}]

# from datetime import datetime
# from datetime import timedelta
# def datetime_operate(n:int):
#     now=datetime.now()
#     _new_date=now+timedelta(days=n)
#     new_date=_new_date.strftime("%Y%m%d")
#     return new_date
# res=datetime_operate(2)
# print(res) # 20200702

# import re
# print(re.findall(r'[\w]{1,20}\@163\.com$',"huyayuan@163.com"))

# import re
# res=re.findall(r"[1-9]\d{4,}@qq.com","1677080339@qq.com")
# res=re.findall(r"[a-zA-Z][a-zA-Z0-9-_]{2,20}@qq\.com","huyayuan@qq.com")
# print(res)

# import requests
# url='https://home.firefoxchina.cn/'
# response=requests.get(url)
# html=response.content
# from bs4 import BeautifulSoup
# html_doc=str(html,'utf-8')
# bf=BeautifulSoup(html_doc,'html.parser')
# content=bf.find_all(class_="cont-mod cont-main")
# print(content)

