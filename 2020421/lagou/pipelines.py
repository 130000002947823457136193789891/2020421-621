import pymysql


class AjaxprojectPipeline(object):
    def process_item(self, item, spider):
        # ********** Begin **********#
        # 1.连接数据库
        # connection = pymysql.connect(
        #     host='localhost',  # 连接的是本地数据库
        #     port=3306,  # 数据库端口名
        #     user='root',  # 自己的mysql用户名
        #     passwd='123123',  # 自己的密码
        #     db='mydb',  # 数据库的名字
        #     charset='utf8',  # 默认的编码方式
        # )
        # # 2.建表，插入数据，完毕后关闭数据库连接，并return item
        # jobName = item['jobName']
        # jobMoney = item['jobMoney']
        # jobNeed = item['jobNeed']
        # jobCompany = item['jobCompany']
        # jobType = item['jobType']
        # jobSpesk = item['jobSpesk']
        # try:
        #     with connection.cursor() as cursor:
        #         sql1 = 'Create Table If Not Exists lgjobs(jobName varchar(20) CHARACTER SET utf8 NOT NULL,jobMoney varchar(10),jobNeed varchar(20) CHARACTER SET utf8 ,jobCompany varchar(20) CHARACTER SET utf8 ,jobType varchar(20) CHARACTER SET utf8 ,jobSpesk varchar(20) CHARACTER SET utf8 ,PRIMARY KEY(jobName))'
        #         sql2 = 'Insert into lgjobs values (\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')' % (
        #         jobName, jobMoney, jobNeed, jobCompany, jobType, jobSpesk)
        #         cursor.execute(sql1)
        #         cursor.execute(sql2)
        #     # 提交本次插入的记录
        #     connection.commit()
        # finally:
        #     # 关闭连接
        #     connection.close()
        #     return item
        # ********** End **********#
        return item