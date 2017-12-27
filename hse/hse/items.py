# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class NewsItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    link = scrapy.Field()
    cover = scrapy.Field()
    posttime = scrapy.Field()
    source = scrapy.Field()
    author = scrapy.Field()
	
class HseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    role = scrapy.Field()
    day = scrapy.Field()
    type = scrapy.Field()
    house_id = scrapy.Field()
    datetime = scrapy.Field()
    browsenum = scrapy.Field()
    alreadyNum = scrapy.Field()
    overdueNum = scrapy.Field()
    isVip = scrapy.Field()
    posttime = scrapy.Field()
    district = scrapy.Field()

class GohomeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    role = scrapy.Field()
    date = scrapy.Field()
    scale = scrapy.Field()
    link = scrapy.Field()
    type = scrapy.Field()
    role = scrapy.Field()
    posttime = scrapy.Field()
    district = scrapy.Field()

class HkreagaItem(scrapy.Item):
    company_id = scrapy.Field()
    company_name = scrapy.Field()
    company_eng = scrapy.Field()
    company_num = scrapy.Field()
    url = scrapy.Field()
    mobile = scrapy.Field()
    fax = scrapy.Field()
    area = scrapy.Field()
    address = scrapy.Field()
    company_link = scrapy.Field()
    email = scrapy.Field()
    posttime = scrapy.Field()

class licenceItem(scrapy.Item):
    num = scrapy.Field()
    name = scrapy.Field()
    name_eng = scrapy.Field()
    company_name = scrapy.Field()
    company_eng = scrapy.Field()
    area = scrapy.Field()
    company_address = scrapy.Field()
    effective_date = scrapy.Field()
    expiry_date = scrapy.Field()
    posttime = scrapy.Field()

