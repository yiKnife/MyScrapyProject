# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhipinItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    collection=table='info'
    jobname=scrapy.Field()
    companyName=scrapy.Field()
    salary=scrapy.Field()
    HRname=scrapy.Field()
    workRequire=scrapy.Field()
    expirence=scrapy.Field()
    education=scrapy.Field()
    companyInfo=scrapy.Field()
    workAddress=scrapy.Field()
    info_url=scrapy.Field()

