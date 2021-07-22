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
        detail_url = detail_url.split('&')[0]
        list = detail_url.split('%')
        detail_url = list[0]+'%'+list[1]+'%'+str(content)+'%'+list[-1]
        fp.write(f'[{content}]({detail_url})')
        fp.write('  \n')
      
    fp.close()

if __name__ == '__main__':
    localtime = time.localtime(time.time())
    nowyear = localtime.tm_year
    nowmonth = localtime.tm_mon
    nowday = localtime.tm_mday
    nowhour = localtime.tm_hour
    nowminites = localtime.tm_min
    
    path1 = 'weibotop_content/'+str(nowyear)
    if not os.path.exists(path1):
        os.mkdir(path1)
    path2 = path1 + '/' +str(nowyear)+'-'+str(nowmonth)
    if not os.path.exists(path2):
        os.mkdir(path2)
    path3 = path2 +'/'+ str(nowyear)+'-'+str(nowmonth)+'-' + str(nowday)
    if not os.path.exists(path3):
        os.mkdir(path3)
    filename = path3 +'/'+str(nowhour)+':'+str(nowminites)+'.md'

    fun(filename)
