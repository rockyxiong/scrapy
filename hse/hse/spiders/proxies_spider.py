import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
class xiciSpider(scrapy.Spider):
    name = "proxies"
    allowed_domains = ["xicidaili.com"]
    start_urls = [
        "http://www.xicidaili.com/",
    ]
    def parse(self, response):
        selector = Selector(response)
        host_list = selector.xpath("//*[@id='ip_list']/tr/td[2]").extract()
        port_list = selector.xpath("//*[@id='ip_list']/tr/td[3]").extract()
        http_prx  = selector.xpath("//*[@id='ip_list']/tr/td[6]").extract()
        filename = 'hse/proxies.txt'
        # if  os.path.exists(filename):
        #    os.remove(filename)
        for i in range(len(host_list)):
            ip = host_list[i].replace('<td>','').replace('</td>','')
            port = port_list[i].replace('<td>','').replace('</td>','')
            http = http_prx[i].replace('<td>','').replace('</td>','')
            if http == 'HTTPS':
                daili = "https://" + str(ip) + ":" + str(port)
                http_prx = "https"
            else:
                daili = "http://" + str(ip) + ":" + str(port)
                http_prx = "http"
            try:
                requests.get('https://www.baidu.com/', proxies={http_prx: daili})
            except:
                print 'connect failed'
            else:
                print 'success'

                with open(filename, 'a') as f:
                        f.write(daili + '\n')



