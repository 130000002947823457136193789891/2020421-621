import urllib.request as req
import os
import hashlib

#超星作业查看
url='https://mooc1-1.chaoxing.com/work/viewWork?id=9452578&courseId=207960096&classId=16074073&workId=1756106c2eaa4b6d8f879473a34023c2&isdisplaytable=2&ut=s&mooc=1&enc=5a4d53aeb5984011e2191fee647d1620&workSystem=0&cpi=44390480'

def step1():
    f=req.urlopen(url)
    data = []
    path = 'cx14.txt'
    outfile = open("cx14.txt", 'wb')
    outfile.writelines(data)
    outfile.close()