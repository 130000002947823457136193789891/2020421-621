# -*- coding: utf-8 -*-
"""
@Author         :  Guan Xiangqing
@Version        :  
@Company        :  Hunan qidian chuangzhi data technology co. LTD
@File           :  re_tools.py
@Description    :  
@CreateTime     :  2020/6/10 0010 17:52
@ModifyTime     :  
"""

import re


class ReTools:
    @staticmethod
    def process_re_rule(re_rule=None, text_content=None):
        """
        功能说明：处理re的规则
        :param re_rule:  re的正则表达式
        :param text_content:  要匹配的内容
        :return:
        """
        return re.findall(re_rule, text_content)

    @staticmethod
    def test_process_re_rule(re_rule=None, text_content=None):
        return ReTools.process_re_rule(re_rule, text_content)


if __name__ == '__main__':
    # 使用正则表达式去除标点符号
    # 注解正则表达式的使用，可以参考网上资料：https://www.cnblogs.com/shenjianping/p/11647473.html
    # 参考我整理的文档：F:\NLP_deeplearning\hot_word_cloud\docs\Python正则表达式高级语法实战-v1.pdf
    # text_content = "4.5；这个年代还能看到一部不故弄玄虚的侦探片真是一本满足！复古味满溢，光感质感一流；剧本简直太棒，散落的零碎线头最终都不落痕迹地嵌入，万有引力之虹滑过的轨迹最终让真相落地。以中段“事先张扬的真相”为分水岭，前半部貌似常规阿婆式封闭空间+各怀鬼胎的大宅门群像（想及《高斯福庄园》），各色人物乍看较脸谱化然实则往往反套路——浪子+暗中观察的老太+上流社会家庭模式（并不遵循观众已有观影经验），因而在悬疑之余生成另一层反差幽默；后半程剧本功力全开，接连不断的“反转”抛出（通过顺应事件内部的逻辑合理性的反转），突破古典范式窠臼，毫不客气摆出政治立场+堂而皇之花式吐槽，然而最终解谜依旧建立于人心的善恶之上，在类型片领域纵横自如。"
    # re_rule = r'[\u4e00-\u9fa5]+'
    # filterdata = ReTools.test_process_re_rule(re_rule, text_content)
    # print(filterdata)
    # cleaned_comments = ''.join(filterdata)
    # print(cleaned_comments)

    # 正则表达式高级用法
    # re_rule = r'.*?应收账款[^,，;；:：。？！?!]*?(增长|增|升|增加|涨).{0,3}([0-9]+)(%|成|倍).*?'
    # text_content = "应收账款增长300倍"
    # print(ReTools.test_process_re_rule(re_rule, text_content))

    # 正则贪婪方法的列举
    re_rule_01 = r"a(.*?)b"
    re_rule_02 = r"a(.*)b"
    text_content = "a123b456b"
    print(ReTools.process_re_rule(re_rule_01, text_content))
    print(ReTools.process_re_rule(re_rule_02, text_content))

    re_rule_03 = r'\s+'
    text_content = "6月9日  教育部发布2020年第1号留学预警  提醒谨慎选择赴澳或返澳学习 "
    print(ReTools.process_re_rule(re_rule_03, text_content))

    re_rule_04 = r'^,'
    text_content = "6月9日,教育部发布2020年第1号留学预警,提醒谨慎选择赴澳或返澳学习 "
    print(ReTools.process_re_rule(re_rule_04, text_content))



