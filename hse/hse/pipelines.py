# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
import datetime
from scrapy.utils.project import get_project_settings

class HsePipeline(object):
    def __init__(self):
        settings = get_project_settings()
        self.conn = MySQLdb.connect(user=settings['MYSQL_USER'], passwd=settings['MYSQL_PASSWD'], db=settings['MYSQL_DBNAME'], host=settings['MYSQL_HOST'], charset="utf8",use_unicode=True)
        self.conn.ping(True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            if spider.name == 'hse':
                yesterday = datetime.date.today() - datetime.timedelta(days=1)
                yesterday = str(yesterday).replace('-','')
                sql1 = 'select browsenum from hk591_data.28hse_browse where day = "' + str(yesterday) + '" AND house_id = "' + str(item['house_id']) + '" AND type = "' + str(item['type']) + '" LIMIT 1'
                self.cursor.execute(sql1)
                data = self.cursor.fetchone()
                old_browse  = data[0] if data!=None else 0
                # 获取每天的浏览数增量
                differenceNum = (int(item['browsenum']) - int(old_browse)) if old_browse > 0 else 0
                self.cursor.execute("INSERT INTO hk591_data.28hse_browse(day,role,type,house_id,datetime,browsenum,differenceNum,alreadyNum,overdueNum,isVip,district,posttime) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                    (item['day'],item['role'],item['type'],item['house_id'],item['datetime'],item['browsenum'],differenceNum,item['alreadyNum'],item['overdueNum'],item['isVip'],item['district'],item['posttime']))
            elif spider.name == 'gohome':
                self.cursor.execute("INSERT INTO hk591_data.new_gohome_data(date,scale,link,role,type,district,posttime) VALUES(%s,%s,%s,%s,%s,%s,%s)",
                                    (item['date'],item['scale'],item['link'],item['role'],item['type'],item['district'],item['posttime']))
            elif spider.name == 'hkreaga':
                self.cursor.execute(
                    "INSERT INTO hk591_data.hk_agency(company_id,company_name,company_eng,company_num,mobile,url,fax,address,company_link,email,posttime) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (item['company_id'], item['company_name'], item['company_eng'], item['company_num'], item['mobile'], item['url'], item['fax'],
                    item['address'],item['company_link'],item['email'],item['posttime']))
            elif spider.name == 'licence':
                self.cursor.execute(
                    "INSERT INTO hk591_data.agency_eaa_info(num,name,name_eng,company_name,company_eng,area,company_address,effective_date,expiry_date,posttime) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (item['num'], item['name'], item['name_eng'], item['company_name'], item['company_eng'],
                     item['area'],
                     item['company_address'], item['effective_date'],
                     item['expiry_date'], item['posttime']))
            self.conn.commit()

        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
        return item

