# 请在下面填入定义Book类的代码
########## Begin ##########
class Book(object):
    ########## End ##########
    '书籍类'

    def __init__(self, name, author, data, version):
        self.name = name
        self.author = author
        self.data = data
        self.version = version

    def sell(self, bookName, price):
        print("%s的销售价格为%d" % (bookName, price))

import re
text = input()
#********** Begin *********#
#1.匹配字符单词 Love
print(re.findall(r'Love',text))
#2.匹配以 w 开头的完整单词
print(re.findall(r'\bw\w*?\b',text))
#3.查找三个字母长的单词（提示：可以使用{m,n}方式）
print(re.findall(r'\b\w{3}\b',text))
#********** End **********#

import re
text = input()
#********** Begin *********#
#1.用compile方法，匹配所有含字母i的单词
rr = re.compile(r'\w*i\w*')
print(rr.findall(text))

#2.在字符串起始位置匹配字符The是否存在，并返回被正则匹配的字符串
print(re.match('The',text).group())

#3.在整个字符串查看字符is是否存在，并返回被正则匹配的字符串
print(re.search('is',text).group())

#********** End **********#

import re
text = input()
#********** Begin *********#
#1.匹配以t开头的所有单词并显示
itext = re.finditer( r'\bt\w*',text )
for i in itext:
    print(i.group())
#2.用空格分割句子
print(re.split(r'\s+', text ))
#3.用‘-’代替句子中的空格
print(re.sub(r' ','-',text ))
#4.用‘-’代替句子中的空格，并返回替换次数
print(re.subn(r' ','-',text ))
#********** End **********#