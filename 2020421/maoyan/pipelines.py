# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import pymysql
import settings


class MaoyanPipeline(object):
    def process_item(self, item, spider):
        # ********** Begin **********#
        # 1.连接数据库
        # connection = pymysql.connection(
        #     host='localhost',
        #     port=3306,
        #     user='root',
        #     passwd='123123',
        #     db='mydb',
        #     charset='utf8',
        # )

        # 2.建表、给表插入数据，完成后关闭数据库连接，return返回item
        # name = item['name']
        # starts = item['starts']
        # releasetime = item['releasetime']
        # score = item['score']
        # try:
        #     with connection.cursor() as cursor:
        #         sql1 = 'Create Table If Not Exists mymovies(name varchar(50) CHARACTER SET utf8 NOT NULL,starts text CHARACTER SET utf8 NOT NULL,releasetime varchar(50) CHARACTER SET utf8 DEFAULT NULL,score varchar(20) CHARACTER SET utf8 NOT NULL,PRIMARY KEY(name)'
        #         sql2 = 'Insert into mymovies values(\'%s\',\'%s\',\'%s\',\'%s\')' % (
        #             name, starts, releasetime, score
        #         )
        #         cursor.excute(sql1)
        #         cursor.excute(sql2)
        #     connection.commit()
        # finally:
        #     connection.close()

        return item

        # ********** End **********#


