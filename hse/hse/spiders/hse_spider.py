# -*- coding:utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from hse.items import HseItem
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import json
import re
import time
class hseSpider(scrapy.Spider):
    name = "hse"
    allowed_domains = ["28hse.com"]
    start_urls = [
        "https://www.28hse.com/buy",
        "https://www.28hse.com/rent"
    ]

    # start_urls = ['https://www.28hse.com/buy/list-{}'.format(i) for i in range(1, 2)]
    def parse(self, response):
        selector = Selector(response)
        buys = selector.xpath('//div[@class="right content_me_div"]/p/a/@href').extract()
        for link in buys:
            yield Request(link, callback=self.parse_dir_contents)
        # 下一頁page_url
        nextlinks = selector.xpath('//*[@id="search_result_div"]/div[3]/table/tr/td[last()]/a/@href').extract()
        if nextlinks:
            next_links = nextlinks[0]
            yield Request(next_links, callback=self.parse)

    def parse_dir_contents(self, response):
        item = HseItem()
        selector = Selector(response)
        #獲取樓盤基礎信息模塊
        table = selector.xpath('//*[@id="bA"]/div[2]/div[2]/ul/li[1]/div/div[1]/table/tr').extract()
        tableStr = ''
        for tr in table:
            tableStr+=tr.replace(' ', '') #去掉空格
        m = re.search(r"<th>樓盤編號</th><td>(.*?)</td>", str(tableStr))
        item['house_id'] = m.group(1) if m != None else 0
        #判斷是否是黃金置頂盤
        if "黃金置頂盤" in str(tableStr):
            item['isVip'] = 1
        elif "置頂盤" in str(tableStr):
            item['isVip'] = 2
        else:
            item['isVip'] = 0
        #判斷是否是已售
        if ("已售" in str(tableStr) or "已租" in str(tableStr)):
            item['alreadyNum'] = 1
        else:
            item['alreadyNum'] = 0
        # 刊登时间
        m = re.search(r"<th>刊登或續期日<\/th><td>(.*?)<\/td>", str(tableStr))
        item['datetime'] = m.group(1) if m != None else ''
        # 浏览数
        m = re.search(r"<th>瀏覽人次<\/th><td>(\d+)<\/td>", str(tableStr))
        item['browsenum'] = m.group(1) if m != None else ''
        # 身份盘
        if "地產代理盤" in str(tableStr):
            item['role'] = 3
        elif "業主自讓盤" in str(tableStr):
            item['role'] = 2
        # 判断是否已过期
        if "放盤已過期" in str(tableStr):
            item['overdueNum'] = 1
        else:
            item['overdueNum'] = 0
        # 租售类型
        typeStr = selector.xpath('//div[@class="clearfix header_linkage_28hse"]/div/a[3]/text()').extract()[0]
        if "租" in str(typeStr):
            item['type'] = 1
        else:
            item['type'] = 2
        # 当前日期
        item['day'] = time.strftime("%Y%m%d", time.localtime())
        # 抓取时间
        item['posttime'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        agentInfo = selector.xpath("//*[@id='bA']/div[2]/div[2]/ul/li[1]/div/div[1]/div[6]").extract()
        # 身份盘
        if "地產代理盤" in str(agentInfo[0]):
            item['role'] = 3
        elif "業主自讓盤" in str(agentInfo[0]):
            item['role'] = 2
        else:
            item['role'] = 0

        #獲取地區
        district = selector.xpath("//*[@class='feature_div_cat']/span[1]/text()").extract()[0]
        if '海外' == district:
            district = selector.xpath("//*[@class='feature_div_cat']/span[2]/text()").extract()[0]
        item['district'] = district
        print json.dumps(typeStr, encoding="UTF-8", ensure_ascii=False)
        #print(item)
        yield item









