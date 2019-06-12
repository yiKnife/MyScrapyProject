# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.exporters import JsonLinesItemExporter
from scrapy.exporters import CsvItemExporter
from scrapy import Request
from scrapy.exceptions import DropItem
import pymysql
#保存到json文件
class ZhipinPipeline(object):
	def __init__(self):
		self.fp=open('zhipin.json','wb')
		self.exporter=JsonLinesItemExporter(self.fp,ensure_ascii=False)
	def open_spider(self,spider):
		print('爬虫开始了')
	def process_item(self, item, spider):
		self.exporter.export_item(item)
		return item
	def close_spider(self,spider):
		print('爬虫结束了')
#保存到csv文件
class CsvZhipinPipeline(object):
	def __init__(self):
		self.fp=open('zhipin.csv','wb')
		self.exporter=CsvItemExporter(self.fp,encoding='ANSI')
	def open_spider(self,spider):
		print('保存开始')
	def process_item(self,item,spider):
		self.exporter.export_item(item)
		return item
	def close_spider(self,spider):
		print('保存成功')
#保存到mysql
"""
class MysqlZhipinPipline(object):
	def __init__(self,host,database,user,password,port):
		self.host=host
		self.database=database
		self.user=user
		self.password=password
		self.port=port
	@classmethod
	def from_crawler(cls,crawler):
		return cls(
			host=crawler.settings.get('MYSQL_HOST'),
			database=crawler.settings.get('MYSQL_DATABASE'),
			user=crawler.settings.get('MYSQL_USER'),
			password=crawler.settings.get('MYSQL_PASSWORD'),
			port=crawler.settings.get('MYSQL_PORT'),
			)
	def open_spider(self,spider):
		self.db=pymysql.connect(self.host,self.user,self.password,self.database,port=self.port,charset='utf8MB4')
		self.cursor=self.db.cursor()
	def close_spider(self,spider):
		self.db.close()

	def process_item(self,item,spider):
		data=dict(item)
		keys=', '.join(data.keys())
		values=', '.join(['%s']*len(data))
		sql='insert into %s (%s) values (%s)' % (item.table,keys,values)
		self.cursor.execute(sql,tuple(data.values()))
		self.db.commit()
		return item
"""







