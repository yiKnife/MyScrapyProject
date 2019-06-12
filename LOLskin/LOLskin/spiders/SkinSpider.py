# -*- coding: utf-8 -*-
import scrapy
from LOLskin.items import LolskinItem
import json
import re


class SkinspiderSpider(scrapy.Spider):
    name = 'SkinSpider'
    allowed_domains = ['lol.qq.com']
    start_urls = ['https://lol.qq.com/biz/hero/champion.js']

    def parse(self, response):
        All_Hero2=json.loads(response.text[50:-1])
        #for key,value in All_Hero2["keys"].items():
        #	yield scrapy.Request(url='https://lol.qq.com/biz/hero/'+value+'.js',meta={'key':len(value),'filename':},callback=self.Hero_Parse)
        for s,v in All_Hero2["data"].items():
        	print(s)
        	print(v["name"])
        	yield scrapy.Request(url='https://lol.qq.com/biz/hero/'+s+'.js',meta={'key':len(s),'filename':v["name"]},callback=self.Hero_Parse)
        	# #print(type(s[1])
        	# for i in s[1]:
        	# 	print(i["name"])
        	# 	#print(i[1])

    def Hero_Parse(self,response):
    	items=LolskinItem()
    	SkinId=json.loads(response.text[62+response.meta['key']:-1])
    	#items["FileName"]=SkinId["data"]["name"]
    	for i in SkinId["data"]["skins"]:
    		# print('#'*50)
    		# print(i["id"])
    		items["FileName"]=response.meta['filename']
    		items["HeroSkinUrl"]=i["id"]
    		items["PicsName"]=i["name"]
    		yield items

