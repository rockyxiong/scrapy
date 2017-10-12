# -*- coding:utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from hse.items import HkreagaItem
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import json
import re
import time
import math
class hseSpider(scrapy.Spider):
    name = "hkreaga"
    allowed_domains = ["hkreaga.org"]
    start_urls = [
        "http://hkreaga.org/a_info.php"
    ]
    def parse(self, response):
        selector = Selector(response)
        urlArr = response.xpath('/html/body/map/area/@href').extract()
        for link in urlArr:
            url = "http://hkreaga.org/"+ link
            yield Request(url, callback=self.parse_list_contents)

    def parse_list_contents(self, response):
        selector = Selector(response)
        listUrl = selector.xpath('//a[@class="font_black12px"]/@href').extract()
        for href in listUrl:
            href_url = "http://hkreaga.org/"+ href
            yield Request(href_url,meta={'url': href_url}, callback=self.parse_detail_contents)
        BPbar = selector.xpath('//div[@class="BPbar"]/a[@class="BPside"]/@onclick').extract()
        if BPbar != []:
            total = BPbar[0].split("total=")[1].split("&")[0]
            key = BPbar[0].split("total=")[1].split("&")[1]
            page_num = int(int(total)/15)
            for i in range(1,page_num):
                list_url = "http://hkreaga.org/member_list.php?total="+str(total)+"&"+str(key)+"&page="+str(i)
                yield Request(list_url, callback=self.parse_list_contents)

    def parse_detail_contents(self,response):
        item = HkreagaItem()
        selector = Selector(response)
        item['company_id'] = selector.xpath('//table[@width="80%"]/tr[1]/td[2]/text()').extract()[0]
        item['company_name'] = selector.xpath('//table[@width="80%"]/tr[2]/td[2]/text()').extract()[0]
        item['company_eng'] = selector.xpath('//table[@width="80%"]/tr[3]/td[2]/text()').extract()[0]
        item['company_num'] = selector.xpath('//table[@width="80%"]/tr[4]/td[2]/text()').extract()[0]
        item['mobile'] = selector.xpath('//table[@width="80%"]/tr[5]/td[2]/text()').extract()[0]
        item['fax'] = selector.xpath('//table[@width="80%"]/tr[6]/td[2]/text()').extract()[0]
        item['address'] = selector.xpath('//table[@width="80%"]/tr[7]/td[2]/text()').extract()[0]
        company_link = selector.xpath('//table[@width="80%"]/tr[8]/td[2]/a/@href').extract()[0]
        item['company_link'] = '' if (company_link == 'http://') else company_link
        email = selector.xpath('//table[@width="80%"]/tr[9]/td[2]/a/@href').extract()[0]
        item['email'] = '' if (email == 'mailto:' ) else email
        item['url'] = response.meta['url']
        item['posttime'] = time.strftime('%Y-%m-%d %H:%M:%S')
        yield item


















