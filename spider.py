import requests
from lxml import etree
import datetime
import os

header = {'User-Agent':'Mozilla/5.0'}
url1 = 'https://s.weibo.com/top/summary?cate=realtimehot'
url2 = 'https://www.zhihu.com/billboard'

def fun1(filename):
    page = requests.get(url=url1,headers=header).text
    tree = etree.HTML(page)

    li_list = tree.xpath('//*[@id="pl_top_realtimehot"]/table/tbody/tr')

    fp = open(filename,'w',encoding='utf-8')
    for li in li_list:
        content = li.xpath('./td[2]/a/text()')[0]
        fp.write(f'{content}')
        fp.write('  \n')
      
    fp.close()

def fun2(filename):
    page = requests.get(url=url2,headers=header).text
    tree = etree.HTML(page)

    li_list = tree.xpath('/html/body/div[1]/div/main/div/a')

    fp = open(filename,'w',encoding='utf-8')
    for li in li_list:
        content = li.xpath('./div[2]/div[1]/text()')[0]
        fp.write(f'{content}')
        fp.write('  \n')
      
    fp.close()
if __name__ == '__main__':
    str =str(datetime.datetime.today())
    
    path1 = 'weibotop_content/'+str[:4]
    if not os.path.exists(path1):
        os.mkdir(path1)
    path2 = path1 + '/' +str[:7]
    if not os.path.exists(path2):
        os.mkdir(path2)
    path3 = path2 +'/'+ str[:10]
    if not os.path.exists(path3):
        os.mkdir(path3)
    filename = path3 +'/'+str[11:16]+'.md'
    fun1(filename)

    path1 = 'zhihutop_content/'+str[:4]
    if not os.path.exists(path1):
        os.mkdir(path1)
    path2 = path1 + '/' +str[:7]
    if not os.path.exists(path2):
        os.mkdir(path2)
    path3 = path2 +'/'+ str[:10]
    if not os.path.exists(path3):
        os.mkdir(path3)
    filename = path3 +'/'+str[11:16]+'.md'
    fun2(filename)
