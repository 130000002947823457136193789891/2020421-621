# -*- coding: utf-8 -*-
"""
@Author         :  Guan Xiangqing
@Version        :  
@Company        :  Hunan qidian chuangzhi data technology co. LTD
@File           :  chinese_cut_words.py
@Description    :
@CreateTime     :  2020/6/10 0010 17:52
@ModifyTime     :
 安装库：pip install jieba -i http://pypi.douban.com/simple  --trusted-host  pypi.douban.com
 参考网址：https://blog.csdn.net/weixin_42137700/article/details/85991890
"""
import jieba


class ChineseCutWords:

    @staticmethod
    def cut_by_accurate(text=None):
        """
        功能说明：结巴分词，精确模式
            jieba.cut参数解析
            参数1：需要分词的字符串;
        　　参数2：cut_all参数用来控制是否采用全模式，默认为精确模式；
                 cut_all=True 全模式
                 cut_all=false 精确（默认）模式
        　　参数3：HMM参数用来控制是否适用HMM模型
        :param text:  需要分词的字符串;
        :return:
        """
        return jieba.cut(text,cut_all=False) # 精确模式

    @staticmethod
    def cut_by_full(text=None):
        """
        功能说明：结巴分词，全模式
            jieba.cut参数解析
            参数1：需要分词的字符串;
        　　参数2：cut_all参数用来控制是否采用全模式，默认为精确模式；
                 cut_all=True 全模式
                 cut_all=false 精确（默认）模式
        　　参数3：HMM参数用来控制是否适用HMM模型
        :param text:  需要分词的字符串;
        :return:
        """
        return jieba.cut(text,cut_all=True) # 全模式

    @staticmethod
    def cut_by_search(text=None):
        """
        功能说明：该方法适用于搜索引擎构建倒排索引的分词，粒度比较细。
            jieba.cut_for_search参数解析
            参数1：需要分词的字符串；
        　　参数2：是否使用HMM模型，
        :param text:  需要分词的字符串;
        :return:
        """
        return jieba.cut_for_search(text,) # 搜索引擎模式 cut_for_search

    @staticmethod
    def cut_by_custom_dict(text=None):
        """
        功能说明：通过自定义词典进行分词
        :param text: 需要分词的字符串;
        :return:
        """
        jieba.load_userdict('../data/user_dict.txt')  # 加载用户自定义词典
        return jieba.lcut(text)  # 默认值配置， cut(self, sentence, cut_all=False, HMM=True):

if __name__ == '__main__':
    text_content = '赵丽颖主演的正午阳光剧,中华人民共和国知否知否应是绿肥红瘦'
    print(list(ChineseCutWords.cut_by_accurate(text_content)))
    print(list(ChineseCutWords.cut_by_full(text_content)))
    print(list(ChineseCutWords.cut_by_search(text_content)))
    print(ChineseCutWords.cut_by_custom_dict(text_content))
