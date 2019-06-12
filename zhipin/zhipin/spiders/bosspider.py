# -*- coding: utf-8 -*-
import scrapy
from zhipin.items import ZhipinItem
num = 1
url_dir=[]
class BosspiderSpider(scrapy.Spider):
	name = 'bosspider'
	allowed_domains = ['zhipin.com']
	start_urls = ['https://www.zhipin.com']
	#url_list=[]s
	"""
	def start_request(self):   #重写start_request
		pass
		"""
	def parse(self, response):
		global url_dir
		all_urls1=response.xpath('//div[@class="job-menu"]//div[@class="menu-sub"]')
		for urls in all_urls1:
			url_dir=urls.xpath('//div[@class="text"]/a/@href').extract()
		#print(len(url_dir))
		#print(url_dir)
		for atv in url_dir:
			#print(atv)
			yield scrapy.Request(url='https://www.zhipin.com'+atv,callback=self.get_urls)
		#for atv in url_dir:
		#	print(atv)
			#yield scrapy.Request(url='https://www.zhipin.com'+atv,callback=self.get_urls)
			

	def get_urls(self,response):	
		all_urls2=response.xpath('//div[@class="job-box"]//div[@class="job-list"]/ul')
		for urls in all_urls2:
			url=urls.xpath('./li//div[@class="info-primary"]//a/@href').extract()
		#print(url)
			for at in url:
				#print(at)
				yield scrapy.Request(url='https://www.zhipin.com'+at,callback=self.get_job_info)
		#print('*'*45)
		next_url=response.xpath('//div[@class="job-list"]/div[@class="page"]/a[@class="next"]/@href').extract()
		next_url="".join(next_url)
		yield scrapy.Request(url='https://www.zhipin.com'+next_url,callback=self.get_urls)
	
	def get_job_info(self,response):
		item=ZhipinItem()
		all_info=response.xpath('//div[@id="wrap"]')
		for info in all_info:
			jobname=info.xpath('.//div[@class="job-banner"]//div[@class="info-primary"]/div[@class="name"]/h1/text()').extract()
			jobname="".join(jobname)
			item['jobname']=jobname.strip()
			salary=info.xpath('.//div[@class="job-banner"]//div[@class="info-primary"]/div[@class="name"]/span/text()').extract()
			salary="".join(salary)
			item['salary']=salary.strip()
			companyName=info.xpath('.//div[@class="job-box"]//a[@ka="job-detail-company"]/text()').extract()
			companyName="".join(companyName)
			item['companyName']=companyName.strip()
			HRname=info.xpath('.//div[@class="job-box"]//div[@class="detail-op"]/h2/text()').extract()
			HRname="".join(HRname)
			item['HRname']=HRname.strip()
			expirence=info.xpath('.//div[@class="job-banner"]//div[@class="info-primary"]/p/text()[2]').extract()
			expirence="".join(expirence)
			item['expirence']=expirence.strip()
			education=info.xpath('.//div[@class="job-banner"]//div[@class="info-primary"]/p/text()[3]').extract()
			education="".join(education)
			item['education']=education.strip()
			workRequire=info.xpath('.//div[@class="job-box"]//div[@class="detail-content"]//div[@class="text"]/text()').extract()
			workRequire="".join(workRequire)
			item['workRequire']=workRequire.strip()
			companyInfo=info.xpath('.//div[@class="job-box"]//div[@class="detail-content"]//div[@class="job-sec company-info"]/div[@class="text"]/text()[1]').extract()
			companyInfo="".join(companyInfo)
			item['companyInfo']=companyInfo.strip()
			workAddress=info.xpath('.//div[@class="job-box"]//div[@class="detail-content"]//div[@class="job-location"]/div/text()').extract()
			workAddress="".join(workAddress)
			item['workAddress']=workAddress.strip()
			item['info_url']=response.url#职位的url
			yield item
		global num
		print('第%d条信息'%num)
		num+=1



