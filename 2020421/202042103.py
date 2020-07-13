

import re
import urllib
import math
import time
import random

my_num=input()				#从测试集获取浮点型数字
my_n=input()				#从测试集获要保留的位n

my_num_float=float(my_num)				#使用float函数将my_num转换为小数
my_n_int=	int(my_n)				#使用int函数将my_n转换为整数
my_num_float1=round(my_num_float,my_n_int)				#采用round函数四舍五入取整
my_num_float2=int(my_num_float*100)	/100			#巧妙采用将小数放大后取整再缩小的方式可以获取直接截取
print(my_num_float1)		#输出结果1
print(my_num_float2)		#输出结果2
