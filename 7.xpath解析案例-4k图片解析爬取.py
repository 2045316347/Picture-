import requests
from lxml import etree
import os

if __name__ == "__mian__":

    url = 'https://pic.netbian.com/4kmeinv/'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
    }

    response = requests.get(url=url,headers=headers).text
    #response.encoding = 'utf-8'
    page_text = response.text

    #数据解析：src的属性值  alt属性值
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//div[@class="slist"]/ul/li')

    #创建一个文件夹
    if not os.path.exists('./picLib'):
        os.mkdir('./picLib')

    for li in li_list:
        img_url = 'https://pic.netbian.com'+li.xpath('./a/img/@src')[0]
        img_name = li.xpath('./a/img/@alt')[0]+'.jpg'

        #通用处理中文乱码的解决方法
        img_name = img_name.encode('iso-8859-1').decode('GBK')

        #print(img_name,img_src)
        #请求图片并进行持久话存储
        img_data = requests.get(url=img_url,headers=headers).content
        img_path = 'picLibs/'+img_name
        with open(img_path,'wb') as fp:
            fp.write(img_data)
            print(img_name,'下载成功！！！')


