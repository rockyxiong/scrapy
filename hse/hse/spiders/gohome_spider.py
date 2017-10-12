# -*- coding:utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import json
import re
import time
from hse.items import GohomeItem
class gohomeSpider(scrapy.Spider):
    name = "gohome"
    allowed_domains = ["gohome.com.hk"]
    start_urls = [
        "https://search.gohome.com.hk/?page=1",
        "https://search.gohome.com.hk/?searchType=2&page=1"
    ]

    def parse(self, response):
        type = 1 if "searchType=2" in str(response.url) else 2
        selector = Selector(response)
        gohomeList = selector.xpath('//div[@class="ListDiv"]/@onclick').extract()
        for gohome in gohomeList:
            link = gohome.split("'")[1].replace("//","https://")
            yield Request(link,meta={'link': link,'type':type}, callback=self.parse_contents)
        #獲取下一頁(當獲取不到鏈接的時候，說明爬蟲已經跑完了)
        if gohomeList == []:
            exit()
        urlArr = response.url.split('page=')
        num = int(urlArr[1]) + 1
        next_page = str(urlArr[0]) + str('page=') + str(num)
        if next_page:
            yield Request(next_page, callback=self.parse)

    def parse_contents(self, response):
        item = GohomeItem()
        selector = Selector(response)
        ProCorner = selector.xpath('//*[@id="PropertyPage"]').extract()[0]
        # #0普通1星级2特选
        if 'ProCorner1' in str(ProCorner):
            scale = 1
        elif 'ProCorner2' in str(ProCorner):
            scale = 2
        else:
            scale = 0
        link = response.meta['link']
        type = response.meta['type']
        #放盤時間
        baseInfo = selector.xpath('//*[@class="expandable"]').extract()[0]
        m = re.search(r"<td>\d{4}年\d{1,2}月\d{1,2}日<\/td>", str(baseInfo))
        updatetime = m.group(0) if m != None else ''
        dr = re.compile(r'<[^>]+>', re.S)
        dd = dr.sub('', updatetime)
        updatetime = dd.replace('年', '-').replace('月', '-').replace('日', '')
        arr = updatetime.split('-')
        if (len(str(arr[1])) == 1):
            arr[1] = str('0') + str(arr[1])
        if (len(str(arr[2])) == 1):
            arr[2] = str('0') + str(arr[2])
        updatetime = '-'.join(arr)
        #盤源
        roleDiv = selector.xpath('//div[@class="RDiv"]').extract()[0]
        AgentLicense = selector.xpath('//div[@class="AgentLicense"]/text()').extract()
        role = 3 if ('<img' in str(roleDiv) or AgentLicense!=[]) else 2
        #地區
        address = selector.xpath('//div[@class="name"]/h1/text()').extract()[0]
        district = address.split('-')[0].replace(" ","")
        item = {'date': updatetime,
                'scale': scale,
                'link': link,
                'district': district,
                'role': role,
                'type': type,
                'posttime':time.strftime('%Y-%m-%d %H:%M:%S')
        }
        #print json.dumps(areaArr, encoding="UTF-8", ensure_ascii=False)
        if(updatetime):
            yield item















