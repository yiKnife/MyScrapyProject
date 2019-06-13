# -*- coding: utf-8 -*-
import scrapy

from DangDang.items import DangdangItem
class DdspiderSpider(scrapy.Spider):
    name = 'DDspider'
    allowed_domains = ['www.dangdang.com']
    start_urls = [
    	'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-24hours-0-0-1-'
    			]
    def start_requests(self):
         for i in range(1,26):
             yield scrapy.Request(url=self.start_urls[0]+str(i),meta={'key':str(i)},callback=self.parse)
    def parse(self, response):
        print('$'*50)
        print('第'+str(response.meta['key'])+'页')
        print('&'*50)
        res=response.xpath('//div[@class="bang_list_box"]/ul[@class="bang_list clearfix bang_list_mode"]/li')
        item=DangdangItem()
        for msg in res:
            paiming=msg.xpath('./div[1]/text()').extract()
            paiming="".join(paiming)
            item['paiming']=paiming.strip('.')
            BookLink=msg.xpath('./div[@class="name"]/a/@href').extract()
            BookLink="".join(BookLink)
            item['BookLink']=BookLink.strip()
            BookName=msg.xpath('./div[@class="name"]/a/text()').extract()
            BookName="".join(BookName)
            item['BookName']=BookName.strip()
            BookPrice=msg.xpath('./div[@class="price"]/p[1]/span[1]/text()').extract()
            BookPrice="".join(BookPrice)
            item['BookPrice']=BookPrice.strip()
            BookComment=msg.xpath('./div[@class="star"]//a/text()').extract()
            BookComment="".join(BookComment)
            item['BookComment']=BookComment.strip()
            TuijianPoint=msg.xpath('./div[@class="star"]//span[@class="tuijian"]/text()').extract()
            TuijianPoint="".join(TuijianPoint)
            item['TuijianPoint']=TuijianPoint.strip()
            WriterMsg=msg.xpath('./div[5]/a[1]/@title').extract()
            WriterMsg="".join(WriterMsg)
            item['WriterMsg']=WriterMsg.strip()
            PublishTime=msg.xpath('./div[6]/span/text()').extract()
            PublishTime="".join(PublishTime)
            item['PublishTime']=PublishTime.strip()
            PressName=msg.xpath('./div[6]/a/text()').extract()
            PressName="".join(PressName)
            item['PressName']=PressName.strip()
            yield item
