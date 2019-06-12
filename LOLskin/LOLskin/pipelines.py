# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
#//ossweb-img.qq.com/images/lol/web201310/skin/big266000.jpg
class LolskinPipeline(ImagesPipeline):

	def get_media_requests(self,item,info):

		k=item['HeroSkinUrl']
		yield Request('http://ossweb-img.qq.com/images/lol/web201310/skin/big'+k+'.jpg',meta={"name":item["PicsName"],'filename':item["FileName"]})

	def file_path(self, request, response=None, info=None):
		image_name=request.meta["name"]
		first=request.meta["filename"]
		filename=u'/{0}/{1}'.format(first,image_name+'.jpg')
		return filename