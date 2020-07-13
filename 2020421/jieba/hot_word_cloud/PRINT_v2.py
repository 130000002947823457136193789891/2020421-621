import jieba  # 分词包
import numpy  # numpy计算包
import re
import pandas as pd
import matplotlib.pyplot as plt
from urllib import request

import requests
from bs4 import BeautifulSoup as bs
from wordcloud import WordCloud
from urllib.request import urlopen, Request
proxyUser = "HPDZ245J4J0265DP"
proxyPass = "FE713FB8F5E24990"

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": "http-dyn.abuyun.com",
    "port": '9010',
    "user": proxyUser,
    "pass": proxyPass,
}

proxies = {
    "http": proxyMeta,
    "https": proxyMeta,
}

# 分析网页函数
def getNowPlayingMovie_list():
    # resp = request.urlopen('https://movie.douban.com/nowplaying/hangzhou/')
    url = 'https://movie.douban.com/nowplaying/hangzhou/'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/71.0.3578.80 Safari/537.36'}
    ret = requests.get(url, headers=headers, proxies=proxies)
    # ret = Request(url)

    # res = urlopen(ret)
    # html_data = res.read().decode('utf-8')
    html_data = ret.content.decode()
    soup = bs(html_data, 'html.parser')
    nowplaying_movie = soup.find_all('div', id='nowplaying')
    nowplaying_movie_list = nowplaying_movie[0].find_all('li', class_='list-item')
    nowplaying_list = []
    for item in nowplaying_movie_list:
        nowplaying_dict = {}
        nowplaying_dict['id'] = item['data-subject']
        for tag_img_item in item.find_all('img'):
            nowplaying_dict['name'] = tag_img_item['alt']
            nowplaying_list.append(nowplaying_dict)
    return nowplaying_list


# 爬取评论函数
def getCommentsById(movieId, pageNum):
    eachCommentList = []
    if pageNum > 0:
        start = (pageNum - 1) * 20
    else:
        return False
    requrl = 'https://movie.douban.com/subject/' + movieId + '/comments' + '?' + 'start=' + str(start) + '&limit=20'
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    # headers = {'User-Agent': 'Mozilla/5.0 3578.98 Safari/537.36'}
    # headers = {
    #     'User-Agent': 'mozilla/5.0 (windows nt 6.1; wow64) applewebkit/537.36 (khtml, like gecko) chrome/27.0.1453.94 safari/537.36'}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'}
    ret = requests.get(requrl, headers=headers, proxies=proxies)
    # ret = Request(requrl)
    # res = urlopen(ret)
    # html_data = res.read().decode('utf-8')
    html_data = ret.content.decode()
    print(requrl)
    soup = bs(html_data, 'html.parser')
    comment_div_lits = soup.find_all('div', class_='comment')
    for item in comment_div_lits:
        if item.find_all('p')[0].contents is not None:
            eachCommentList.append(item.find_all('p')[0].contents)
    return eachCommentList


def main():
    # 循环获取第一个电影的前10页评论
    commentList = []
    NowPlayingMovie_list = getNowPlayingMovie_list()
    for i in range(10):
        num = i + 1
        commentList_temp = getCommentsById(NowPlayingMovie_list[0]['id'], num)
        commentList.append(commentList_temp)
    # 将列表中的数据转换为字符串
    comments = ''
    for k in range(len(commentList)):
        comments = comments + (str(commentList[k])).strip()
    # 使用正则表达式去除标点符号
    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    filterdata = re.findall(pattern, comments)
    cleaned_comments = ''.join(filterdata)
    # 使用结巴分词进行中文分词
    segment = jieba.lcut(cleaned_comments)
    words_df = pd.DataFrame({'segment': segment})
    # 去掉停用词
    stopwords = pd.read_csv("data/stopwords.txt", index_col=False, quoting=3, sep='\s+', names=['stopword'],
                            encoding='utf-8')  # quoting=3全不引用
    # 参考网址：https://pandas.pydata.org/pandas-docs/stable/user_guide/
    words_df = words_df[~words_df.segment.isin(stopwords.stopword)]
    # 统计词频
    words_stat = words_df.groupby(by=['segment'])['segment'].agg({"计数": numpy.size})
    words_stat = words_stat.reset_index().sort_values(by=["计数"], ascending=False)
    print(words_stat)

    # 用词云进行显示
    # wordcloud = WordCloud(font_path="simhei.ttf", background_color="white", max_font_size=80, width=1000, height=600)
    wordcloud = WordCloud(font_path="simhei.ttf", background_color="white", max_font_size=80, width=500, height=300)
    # word_cloud = WordCloud(font_path="simhei.ttf",
    #                        background_color="white", max_words=1000, mask=color_mask,
    #                        max_font_size=40, random_state=42)
    word_frequence = {x[0]: x[1] for x in words_stat.head(1000).values}  # '{吴京': '8','主旋律': '6'}word_frequence
    wordcloud = wordcloud.fit_words(word_frequence)
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()


# 主函数
if __name__ == '__main__':
    main()