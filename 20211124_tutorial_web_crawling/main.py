# File encoding: utf8

import requests
from bs4 import BeautifulSoup
import re
import os
import urllib
import numpy
import pandas
from tabulate import tabulate
import matplotlib.pyplot as plt

url = 'https://search.musinsa.com/search/musinsa/goods?q=%ED%8B%B0%EC%85%94%EC%B8%A0&list_kind=small&sortCode=pop&sub_sort=&page=1&display_cnt=0&saleGoods=&includeSoldOut=&setupGoods=&popular=&category1DepthCode=&category2DepthCodes=&category3DepthCodes=&selectedFilters=&category1DepthName=&category2DepthName=&brandIds=&price=&colorCodes=&contentType=&styleTypes=&includeKeywords=&excludeKeywords=&originalYn=N&tags=&campaignId=&serviceType=&eventType=&type=&season=&measure=&openFilterLayout=N&selectedOrderMeasure=&shoeSizeOption=&groupSale=&d_cat_cd='
res = requests.get(url)
print(res.raise_for_status)
soup = BeautifulSoup(res.text, 'lxml')

section_item = soup.find('li', attrs={'class': 'li_box'})
section_img = section_item.find('img')
url_img = section_img['data-original']

url_img

url_img = 'https://image.msscdn.net/images/goods_img/20200928/1628385/1628385_2_220.jpg'
urllib.request.urlretrieve(url_img)



dir_project = r'/content/gdrive/MyDrive/20211124_textile_big_data'
if os.path.isdir(dir_project):
    pass
else:
    os.mkdir(dir_project)

for ii in range(1, 1443):
    url = 'https://search.musinsa.com/search/musinsa/goods?q=%ED%8B%B0%EC%85%94%EC%B8%A0&list_kind=small&sortCode=pop&sub_sort=&page={}&display_cnt=0&saleGoods=&includeSoldOut=&setupGoods=&popular=&category1DepthCode=&category2DepthCodes=&category3DepthCodes=&selectedFilters=&category1DepthName=&category2DepthName=&brandIds=&price=&colorCodes=&contentType=&styleTypes=&includeKeywords=&excludeKeywords=&originalYn=N&tags=&campaignId=&serviceType=&eventType=&type=&season=&measure=&openFilterLayout=N&selectedOrderMeasure=&shoeSizeOption=&groupSale=&d_cat_cd='.format(
        ii)
    res = requests.get(url)
    print(res.raise_for_status)
    soup = BeautifulSoup(res.text, 'lxml')

    section_item = soup.find_all('li', attrs={'class': 'li_box'})
    count = 0
    df = pandas.DataFrame()
    for i in section_item:
        print('for i/total: {}/{}'.format(count + 1, len(section_item)))
        count += 1

        # image
        section_img = i.find('img')
        url_img = section_img['data-original']

        file_name = dir_project + '/' + str(count) + '.jpg'
        # urllib.request.urlretrieve(url_img, file_name)

        # name
        name = section_img['alt']

        # detail
        section_detail = i.find('a', attrs={'class': 'img-block'})
        url_detail = section_detail['href']

        # price
        section_price = i.find('p', attrs={'class': 'price'})
        a = section_price.get_text()
        p = re.compile('[0-9,]+원')
        list_price = p.findall(section_price.get_text())
        if len(list_price) == 2:
            price_before = list_price[0]
            price_after = list_price[1]

        elif len(list_price) == 1:
            price_before = numpy.nan
            price_after = list_price[0]

        # brand
        section_brand = i.find('p', attrs={'class': 'item_title'})
        brand = section_brand.get_text()

        # tag
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
        url = url_detail
        res = requests.get(url, headers=headers)
        print(res.raise_for_status)
        soup = BeautifulSoup(res.text, 'lxml')
        section_info = soup.find('div', attrs={'class': 'explan_product product_info_section'})
        section_tag = section_info.find('li', attrs={'class': 'article-tag-list list'})
        if section_tag == None:
            tag = ''
        else:
            tag = section_tag.get_text()

        df_new = pandas.DataFrame(
            [
                [
                    name,
                    brand,
                    price_before,
                    price_after,
                    tag,
                    url_img,
                    url_detail,
                ]
            ],
            columns=[
                'name',
                'brand',
                'price_before',
                'price_after',
                'tag',
                'url_img',
                'url_detail',
            ]
        )

        df = df.append(df_new)

# pandas.options.display.max_columns = None
df = df.reset_index(drop=True)
print(tabulate(df, headers='keys', tablefmt='psql', showindex=True))

path_or_buf = dir_project + '/' + 'musinsa_20211124' + '.csv'
df.to_csv(path_or_buf=path_or_buf, index=True, encoding='UTF-8')
