import scrapy


class AjaxprojectItem(scrapy.Item):
    # ********** Begin **********#
    jobName = scrapy.Field()
    jobMoney = scrapy.Field()
    jobNeed = scrapy.Field()
    jobCompany = scrapy.Field()
    jobType = scrapy.Field()
    jobSpesk = scrapy.Field()
    # ********** End **********#