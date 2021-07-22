import requests
from lxml import etree
import time
import os

header = {'User-Agent':'Mozilla/5.0'}
url = 'https://s.weibo.com/top/summary?cate=realtimehot'

def fun(filename):
    page = requests.get(url=url,headers=header).text
    tree = etree.HTML(page)

    li_list = tree.xpath('//*[@id="pl_top_realtimehot"]/table/tbody/tr')

    fp = open(filename,'w',encoding='utf-8')
    for li in li_list:
        content = li.xpath('./td[2]/a/text()')[0]
        detail_url ='http:/'+ li.xpath('./td[2]/a/@href')[0]
        fp.write(f'[{content}]({detail_url})'+' \n')
      
    fp.close()

if __name__ == '__main__':
    localtime = time.localtime(time.time())
    nowyear = localtime.tm_year
    nowmonth = localtime.tm_mon
    nowday = localtime.tm_mday
    nowhour = localtime.tm_hour
    nowminites = localtime.tm_min

    path = 'weibotop_content/'+str(nowyear)+'-'+str(nowmonth)+'-'+str(nowday)
    if not os.path.exists(path):
        os.mkdir(path)
    
    filename = path +'/'+str(nowhour)+':'+str(nowminites)+'.md'

    fun(filename)
