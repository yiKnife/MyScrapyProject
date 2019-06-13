# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonLinesItemExporter
from scrapy.exporters import CsvItemExporter
from scrapy import Request
from scrapy.exceptions import DropItem

class DangdangPipeline(object):
    def __init__(self):
        self.fp=open('DangDangProduct.json','wb')
        self.exporter=JsonLinesItemExporter(self.fp,ensure_ascii=False)
    def open_spider(self,spider):
        print('爬虫开始了')
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
    def close_spider(self,item,spider):
        print('爬虫结束了')
        self.fp.close()

class CsvDangDangPipeline(object):
	def __init__(self):
		self.fp=open('DangDangProD.csv','wb')
		self.exporter=CsvItemExporter(self.fp)
	def process_item(self,item,spider):
		self.exporter.export_item(item)
		return item
	def close_spider(self,spider):
		self.fp.close()
