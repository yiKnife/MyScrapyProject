# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    BookLink=scrapy.Field()			#书的链接
    paiming=scrapy.Field()			#书的排名
    BookName=scrapy.Field()         #书名
    BookPrice=scrapy.Field()		#价格
    BookComment=scrapy.Field()		#评论数
    TuijianPoint=scrapy.Field()		#推荐指数
    WriterMsg=scrapy.Field()		#作者信息
    PublishTime=scrapy.Field()		#出版时间
    PressName=scrapy.Field()		#出版社名称