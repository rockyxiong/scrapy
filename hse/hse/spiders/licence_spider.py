import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from hse.items import licenceItem
import time
import telnetlib
class licenceSpider(scrapy.Spider):
    name = "licence"
    allowed_domains = ["eaa.org.hk"]
    start_urls = [
        "https://www.eaa.org.hk/zh-hk/licence-search"
    ]
    def start_requests(self):
        typeArr = ["C"]
        for type in typeArr:
            for j in range(3,5):
                if j == 3:
                    start = 1287
                else:
                    start = 0
                for i in range(start,100000):
                    if(len(str(i)) == 1):
                        num = '00000'+str(i)
                    elif(len(str(i)) == 2):
                        num = '0000' + str(i)
                    elif (len(str(i)) == 3):
                        num = '000' + str(i)
                    elif (len(str(i)) == 4):
                        num = '00' + str(i)
                    elif (len(str(i)) == 5):
                        num = '0' + str(i)
                    elif (len(str(i)) == 6):
                        num = str(i)
                    licence = str(type)+'-'+str(num)+'-A00'+str(j)
                    print(licence)
                    postdata = {
                        'StylesheetManager_TSSM': '',
                        'ScriptManager_TSM': '',
                        '__EVENTTARGET': '',
                        '__EVENTARGUMENT': '',
                        '__VIEWSTATEGENERATOR': '',
                        '__EVENTVALIDATION': '',
                        '__RequestVerificationToken': '',
                        '__VIEWSTATE': '/wEPDwUKLTU1MDYzMDgwNw9kFgICBg9kFgICAQ9kFgICBw9kFgJmD2QWEGYPZBYCZg8PFgIeB1Zpc2libGVoZBYCAgEPDxYEHgtOYXZpZ2F0ZVVybAXaAS9EZXNrdG9wTW9kdWxlcy9ETk5Hb194UGx1Z2luL0luZGV4X01hbmFnZXIuYXNweD9Qb3J0YWxJZD0wJlRhYklkPTEzMzEmTW9kdWxlSWQ9MjQ3OSZsYW5ndWFnZT16aC1ISyZUb2tlbj1Ta2luX09wdGlvbnMmU2tpbkZpbGVOYW1lPUVBQUlubmVyTGVmdCZTa2luUGF0aD0lMmZQb3J0YWxzJTJmX2RlZmF1bHQlMmZTa2lucyUyZjIwMDY4LVVubGltaXRlZENvbG9yc1BhY2stMDUwJTJmHwBoZGQCBg9kFgICAg8QDxYCHwBoZA8WDGYCAQICAgMCBAIFAgYCBwIIAgkCCgILFgwQBRdFbmdsaXNoIChVbml0ZWQgU3RhdGVzKQUFZW4tVVNnEAUd5Lit5paHKOmmmea4r+eJueWIpeihjOaUv+WNgCkFBXpoLUhLZxAFHeS4reaWhyjkuK3ljY7kurrmsJHlhbHlkozlm70pBQV6aC1DTmcQBRdFbmdsaXNoIChVbml0ZWQgU3RhdGVzKQUFZW4tVVNnEAUd5Lit5paHKOmmmea4r+eJueWIpeihjOaUv+WNgCkFBXpoLUhLZxAFHeS4reaWhyjkuK3ljY7kurrmsJHlhbHlkozlm70pBQV6aC1DTmcQBRdFbmdsaXNoIChVbml0ZWQgU3RhdGVzKQUFZW4tVVNnEAUd5Lit5paHKOmmmea4r+eJueWIpeihjOaUv+WNgCkFBXpoLUhLZxAFHeS4reaWhyjkuK3ljY7kurrmsJHlhbHlkozlm70pBQV6aC1DTmcQBRdFbmdsaXNoIChVbml0ZWQgU3RhdGVzKQUFZW4tVVNnEAUd5Lit5paHKOmmmea4r+eJueWIpeihjOaUv+WNgCkFBXpoLUhLZxAFHeS4reaWhyjkuK3ljY7kurrmsJHlhbHlkozlm70pBQV6aC1DTmcWAWZkAgcPFQEG5pCc5bCLZAILDxUBDOmbu+WtkOacjeWLmWQCEQ8VCBkvemgtSEsvZXZlbnRjYWxlbmRhci5hc3B4DOa0u+WLleaciOabhhUvemgtSEsvbGljZW5zZWVzLmFzcHgJ5oyB54mM5Lq6Gi96aC1ISy9jb25zdW1lcmNvcm5lci5hc3B4D+a2iOiyu+iAheWwiOWNgCAvemgtSEsvcHJvc3BlY3RpdmVsaWNlbnNlZXMuYXNweAzmupblgpnogIPoqaZkAhMPZBYCZg8WAh4EVGV4dAW4Fzx1bCAgaWQ9ImdvbWVudTBlZjY1NjFhMGMiIGNsYXNzPSJkcm9wZG93biAiPjxsaSBjbGFzcz0iIEl0ZW0tMSAiPjxhIGhyZWY9Imh0dHBzOi8vd3d3LmVhYS5vcmcuaGsvemgtaGsvTGljZW5zaW5nL0xpY2Vuc2luZyIgY2xhc3M9Im1lbnVpdGVtICIgdGl0bGU9IkxpY2Vuc2luZyIgPjxzcGFuPkxpY2Vuc2luZzwvc3Bhbj48L2E+PC9saT48bGkgY2xhc3M9IiBJdGVtLTIgIj48YSBocmVmPSJodHRwczovL3d3dy5lYWEub3JnLmhrL3poLWhrL0xpY2Vuc2luZy9UeXBlcy1vZi1saWNlbmNlcyIgY2xhc3M9Im1lbnVpdGVtICIgdGl0bGU9IlR5cGVzIG9mIGxpY2VuY2VzIiA+PHNwYW4+VHlwZXMgb2YgbGljZW5jZXM8L3NwYW4+PC9hPjwvbGk+PGxpIGNsYXNzPSIgSXRlbS0zICI+PGEgaHJlZj0iaHR0cHM6Ly93d3cuZWFhLm9yZy5oay96aC1oay9MaWNlbnNpbmcvU1BPQiIgY2xhc3M9Im1lbnVpdGVtICIgdGl0bGU9IlNQT0IiID48c3Bhbj5TUE9CPC9zcGFuPjwvYT48L2xpPjxsaSBjbGFzcz0iIEl0ZW0tNCAiPjxhIGhyZWY9Imh0dHBzOi8vd3d3LmVhYS5vcmcuaGsvemgtaGsvTGljZW5zaW5nL0xpY2Vuc2luZy1yZXF1aXJlbWVudHMiIGNsYXNzPSJtZW51aXRlbSAiIHRpdGxlPSJMaWNlbnNpbmcgcmVxdWlyZW1lbnRzIiA+PHNwYW4+TGljZW5zaW5nIHJlcXVpcmVtZW50czwvc3Bhbj48L2E+PC9saT48bGkgY2xhc3M9IiBJdGVtLTUgIj48YSBocmVmPSJodHRwczovL3d3dy5lYWEub3JnLmhrL3poLWhrL0xpY2Vuc2luZy9Fc3RhdGUtYWdlbnQtY2FyZCIgY2xhc3M9Im1lbnVpdGVtICIgdGl0bGU9IkVzdGF0ZSBhZ2VudCBjYXJkIiA+PHNwYW4+RXN0YXRlIGFnZW50IGNhcmQ8L3NwYW4+PC9hPjwvbGk+PGxpIGNsYXNzPSIgSXRlbS02ICI+PGEgaHJlZj0iaHR0cHM6Ly93d3cuZWFhLm9yZy5oay96aC1oay9MaWNlbnNpbmcvTGljZW5jZS1mZWVzIiBjbGFzcz0ibWVudWl0ZW0gIiB0aXRsZT0iTGljZW5jZSBmZWVzIiA+PHNwYW4+TGljZW5jZSBmZWVzPC9zcGFuPjwvYT48L2xpPjxsaSBjbGFzcz0iIEl0ZW0tNyAiPjxhIGhyZWY9Imh0dHBzOi8vd3d3LmVhYS5vcmcuaGsvemgtaGsvTGljZW5zaW5nL0FwcGxpY2F0aW9uLXByb2NlZHVyZSIgY2xhc3M9Im1lbnVpdGVtICIgdGl0bGU9IkFwcGxpY2F0aW9uIHByb2NlZHVyZSIgPjxzcGFuPkFwcGxpY2F0aW9uIHByb2NlZHVyZTwvc3Bhbj48L2E+PC9saT48bGkgY2xhc3M9IiBJdGVtLTggIj48YSBocmVmPSJodHRwczovL3d3dy5lYWEub3JnLmhrL3poLWhrL0xpY2Vuc2luZy9MaWNlbmNlLWV4cGlyeS1hbmQtcmVuZXdhbCIgY2xhc3M9Im1lbnVpdGVtICIgdGl0bGU9IkxpY2VuY2UgZXhwaXJ5IGFuZCByZW5ld2FsIiA+PHNwYW4+TGljZW5jZSBleHBpcnkgYW5kIHJlbmV3YWw8L3NwYW4+PC9hPjwvbGk+PGxpIGNsYXNzPSIgSXRlbS05ICI+PGEgaHJlZj0iaHR0cHM6Ly93d3cuZWFhLm9yZy5oay96aC1oay9MaWNlbnNpbmcvR3VpZGUtdG8tY29tcGxldGluZy1saWNlbmNlLWFwcGxpY2F0aW9uLWZvcm0iIGNsYXNzPSJtZW51aXRlbSAiIHRpdGxlPSJHdWlkZSB0byBjb21wbGV0aW5nIGxpY2VuY2UgYXBwbGljYXRpb24gZm9ybSIgPjxzcGFuPkd1aWRlIHRvIGNvbXBsZXRpbmcgbGljZW5jZSBhcHBsaWNhdGlvbiBmb3JtPC9zcGFuPjwvYT48L2xpPjxsaSBjbGFzcz0iIEl0ZW0tMTAgIj48YSBocmVmPSJodHRwczovL3d3dy5lYWEub3JnLmhrL3poLWhrL2Rpc2NpcGxpbmFyeS1zZWFyY2giIGNsYXNzPSJtZW51aXRlbSAiIHRpdGxlPSJBY3Rpb25zIFRha2VuIEFnYWluc3QgTGljZW5zZWVzIG9yIEV4LWxpY2Vuc2VlcyIgPjxzcGFuPkFjdGlvbnMgVGFrZW4gQWdhaW5zdCBMaWNlbnNlZXMgb3IgRXgtbGljZW5zZWVzPC9zcGFuPjwvYT48L2xpPjxsaSBjbGFzcz0iIEl0ZW0tMTEgIj48YSBocmVmPSJodHRwczovL3d3dy5lYWEub3JnLmhrL3poLWhrL0xpY2Vuc2luZy9Eb3dubG9hZC1mb3JtcyIgY2xhc3M9Im1lbnVpdGVtICIgdGl0bGU9IkRvd25sb2FkIGZvcm1zIiA+PHNwYW4+RG93bmxvYWQgZm9ybXM8L3NwYW4+PC9hPjwvbGk+PGxpIGNsYXNzPSJjdXJyZW50IEl0ZW0tMTIgIj48YSBocmVmPSJodHRwczovL3d3dy5lYWEub3JnLmhrL3poLWhrL2xpY2VuY2Utc2VhcmNoIiBjbGFzcz0ibWVudWl0ZW0gYWN0aXZlIiB0aXRsZT0iTGljZW5jZSBsaXN0IiA+PHNwYW4+TGljZW5jZSBsaXN0PC9zcGFuPjwvYT48L2xpPjxsaSBjbGFzcz0iIEl0ZW0tMTMgIj48YSBocmVmPSJodHRwczovL3d3dy5lYWEub3JnLmhrL3poLWhrL0xpY2Vuc2luZy9MaWNlbmNlLXJlZ2lzdGVyIiBjbGFzcz0ibWVudWl0ZW0gIiB0aXRsZT0iTGljZW5jZSByZWdpc3RlciIgPjxzcGFuPkxpY2VuY2UgcmVnaXN0ZXI8L3NwYW4+PC9hPjwvbGk+PGxpIGNsYXNzPSIgSXRlbS0xNCAiPjxhIGhyZWY9Imh0dHBzOi8vd3d3LmVhYS5vcmcuaGsvemgtaGsvTGljZW5zaW5nL011dHVhbC1yZWNvZ25pdGlvbiIgY2xhc3M9Im1lbnVpdGVtICIgdGl0bGU9Ik11dHVhbCByZWNvZ25pdGlvbiIgPjxzcGFuPk11dHVhbCByZWNvZ25pdGlvbjwvc3Bhbj48L2E+PC9saT48bGkgY2xhc3M9IiBJdGVtLTE1ICI+PGEgaHJlZj0iaHR0cHM6Ly93d3cuZWFhLm9yZy5oay96aC1oay9MaWNlbnNpbmcvZS1TZXJ2aWNlcyIgY2xhc3M9Im1lbnVpdGVtICIgdGl0bGU9ImUtU2VydmljZXMiID48c3Bhbj5lLVNlcnZpY2VzPC9zcGFuPjwvYT48L2xpPjxsaSBjbGFzcz0iIEl0ZW0tMTYgIj48YSBocmVmPSJodHRwczovL3d3dy5lYWEub3JnLmhrL3poLWhrL0xpY2Vuc2luZy9FLWFwcGxpY2F0aW9uIiBjbGFzcz0ibWVudWl0ZW0gIiB0aXRsZT0iRS1hcHBsaWNhdGlvbiIgPjxzcGFuPkUtYXBwbGljYXRpb248L3NwYW4+PC9hPjwvbGk+PGxpIGNsYXNzPSIgSXRlbS0xNyAiPjxhIGhyZWY9Imh0dHBzOi8vd3d3LmVhYS5vcmcuaGsvemgtaGsvTGljZW5zaW5nL0ZBUXMiIGNsYXNzPSJtZW51aXRlbSAiIHRpdGxlPSJGQVFzIiA+PHNwYW4+RkFRczwvc3Bhbj48L2E+PC9saT48L3VsPmQCFQ9kFgJmDxQrAAIPFggeEkNvbGxhcHNlZE5vZGVJbWFnZWUeEFN5c3RlbUltYWdlc1BhdGgFCC9pbWFnZXMvHhFFeHBhbmRlZE5vZGVJbWFnZWUeG0RlZmF1bHROb2RlQ3NzQ2xhc3NTZWxlY3RlZAUHc2lkZXNlbGRkZAIwD2QWAgIBD2QWAgIBD2QWAmYPZBYCAgEPZBYCAgEPZBYKAgIPFgIfAgUSKOS+i+WmgjogRS0xMjM0NTYpZAIMDxYCHglpbm5lcmh0bWxkZAINDw9kDxAWBGYCAQICAgMWBBYCHg5QYXJhbWV0ZXJWYWx1ZQUIUy0xOTcxNDEWAh8IaBYCHwhlFgIfCGUWBGZmZmZkZAIODzwrABEDAA8WBB4LXyFEYXRhQm91bmRnHgtfIUl0ZW1Db3VudAIDZAEQFgAWABYADBQrAAAWAmYPZBYMZg9kFhBmDw8WAh8CBSjniYznhafomZ/norwv54ef5qWt6Kmz5oOF6Kqq5piO5pu46Jmf56K8ZGQCAQ8PFgIfAgUP5oyB54mM5Lq65ZCN56ixZGQCAg8PFgIfAgUb54ef5qWt5ZCN56ixICjnh5/mpa3lnLDpu54pZGQCAw8PFgIfAgUM55Sf5pWI5pel5pyfZGQCBA8PFgIfAgUM5bGG5ru/5pel5pyfZGQCBQ8PFgIfAgUM55u46Zec54mM54WnZGQCBg8PFgIfAgUP5L2c5Ye655qE6KGM5YuVZGQCBw9kFgICAQ8PFgIfAQUxaHR0cHM6Ly93d3cuZWFhLm9yZy5oay96aC1oay9MaWNlbnNpbmcvQ29uZGl0aW9uc2QWAmYPFQEM6ZmE5Yqg5qKd5Lu2ZAIBD2QWEGYPZBYCZg8VAQhTLTE5NzE0MWQCAQ9kFgJmDxUBF0xFRSBXQUkgVEFLICjmnY7lgYnlvrcpZAICD2QWAmYPFQEAZAIDD2QWAmYPFQEKMzAvMDkvMjAxNGQCBA9kFgJmDxUBCjI5LzA5LzIwMTVkAgUPZBYEAgEPFgIfCmZkAgIPFQEAZAIGD2QWAmYPFQEAZAIHD2QWAmYPFQEAZAICD2QWEGYPZBYCZg8VAQhTLTE5NzE0MWQCAQ9kFgJmDxUBF0xFRSBXQUkgVEFLICjmnY7lgYnlvrcpZAICD2QWAmYPFQEAZAIDD2QWAmYPFQEKMzAvMDkvMjAxNWQCBA9kFgJmDxUBCjI5LzA5LzIwMTZkAgUPZBYEAgEPFgIfCmZkAgIPFQEAZAIGD2QWAmYPFQEAZAIHD2QWAmYPFQEAZAIDD2QWEGYPZBYCZg8VAQhTLTE5NzE0MWQCAQ9kFgJmDxUBF0xFRSBXQUkgVEFLICjmnY7lgYnlvrcpZAICD2QWAmYPFQEAZAIDD2QWAmYPFQEKMzAvMDkvMjAxNmQCBA9kFgJmDxUBCjI5LzA5LzIwMTdkAgUPZBYEAgEPFgIfCmZkAgIPFQEAZAIGD2QWAmYPFQEAZAIHD2QWAmYPFQEAZAIEDw8WAh8AaGRkAgUPDxYCHwBoZGQCDw8PFgQfAgUV56ysIDEg6aCB77yM5YWoIDEg6aCBHwBnZGQYAgUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgUFFmRubiRkbm5OQVYyJGN0bGRubk5BVjIFFGRubiRkbm5OQVYkY3RsZG5uTkFWBRhkbm4kc2lkZU1lbnUkY3Rsc2lkZU1lbnUFGmRubiRzaWRlTWVudTIkY3Rsc2lkZU1lbnUyBS1kbm4kY3RyMjQ5NiRMaWNlbmNlU2VhcmNoJGNiQ3VycmVudFBlcmlvZE9ubHkFMWRubiRjdHIyNDk2JExpY2VuY2VTZWFyY2gkZ2R2TGljZW5jZUFuZFNQT0JSZXN1bHQPPCsADAEIAgFkPh+3eCPENwiz/ZwQiAYqlroIeYc=',
                        '__VIEWSTATEGENERATOR': 'CA0B0334',
                        '__EVENTVALIDATION': '/wEdAA12iEF+fJjKZectC8ECxIENYABt7kPpyNkCbg5KgFBbh6GlYIhy1B6TSgNoSzJAvPgnPt+9KOYqcznXKTPjv1cz3o6QUin6YzMbgP76ZtC0obacFNb5Gej7uRAk8hSyMV3iSH7blcylZo0ndN2JcqvzrB+GVL1kymkqpLBTTkGaQKjUph22lt2ov68I8ZV2ybFCjvn0Ii6Q2OFGOVD8SZ54DJngdv0FvnCS7b4ux4i8iVfJ82cLYuNHga3Vmj3QvawglYTgmyD61+C5CtBsuVtAllNyGwnpGT3zi0wZ1dAoJ9Sf4V4=',
                        'dnn$txtSearch': '',
                        'dnn$ctr2496$LicenceSearch$cbCurrentPeriodOnly': '1',
                        'dnn$ctr2496$LicenceSearch$txtLicNo': licence,
                        'dnn$ctr2496$LicenceSearch$txtLicName': '',
                        'dnn$ctr2496$LicenceSearch$txtBusinName': '',
                        'dnn$ctr2496$LicenceSearch$btnLicenceSearch': '',
                        'ScrollTop': '150'
                    }
                    yield scrapy.FormRequest(url='https://www.eaa.org.hk/zh-hk/licence-search',formdata=postdata,callback=self.post_page)

    def post_page(self, response):
        selector = Selector(response)
        item = licenceItem()
        num = selector.xpath('//*[@id="dnn_ctr2496_LicenceSearch_gdvLicenceAndSPOBResult"]/tr[2]/td[1]/text()').extract()
        try:
            num = num[0].strip().replace("\r\n","")
            company = selector.xpath('//*[@id="dnn_ctr2496_LicenceSearch_gdvLicenceAndSPOBResult"]/tr[2]/td[2]/text()').extract()[0]
            company = company.strip().replace("\r\n","")
            name = company.split('(')[0]
            name_eng = company.split('(')[1].replace(')','')
            companyArr = selector.xpath('//*[@id="dnn_ctr2496_LicenceSearch_gdvLicenceAndSPOBResult"]/tr[2]/td[3]/text()').extract()
            company_name = companyArr[1].strip().replace("\r\n","")
            company_eng = companyArr[0].strip().replace("\r\n","")
            company_address = companyArr[2].strip().replace("\r\n", "")
            effective_date = selector.xpath('//*[@id="dnn_ctr2496_LicenceSearch_gdvLicenceAndSPOBResult"]/tr[2]/td[4]/text()').extract()[0]
            effective_date = effective_date.strip().replace("\r\n","")
            expiry_date = selector.xpath('//*[@id="dnn_ctr2496_LicenceSearch_gdvLicenceAndSPOBResult"]/tr[2]/td[5]/text()').extract()[0]
            expiry_date = expiry_date.strip().replace("\r\n", "")
            #companyArr = company_name.split("<br/>")
            item = {
                'num':num,
                'name':name,
                'name_eng':name_eng,
                'company_name':company_name,
                'company_eng':company_eng,
                'company_address':company_address,
                'area':'',
                'effective_date':effective_date,
                'expiry_date':expiry_date,
                'posttime':time.strftime('%Y-%m-%d %H:%M:%S')
            }
            print(item)
            yield (item)
        except Exception as e:
            print(e, '-----')




