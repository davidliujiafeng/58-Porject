'''  Author- FGV587   '''

from bs4 import BeautifulSoup
import requests
import time
import pymongo
import re


client = pymongo.MongoClient('localhost',27017)
ceshi = client['ceshi']
url_list = ceshi['url_list4']
item_info= ceshi['item_info4']
# spider 1

def get_links_from(channel,pages,who_sells=0):

    list_view = '{}{}/pn{}/'.format(channel,str(who_sells),str(pages))
    web_data = requests.get(list_view)
    time.sleep(0.5)
    soup = BeautifulSoup(web_data.text,'lxml')
    p = re.compile('http://bj.58.com/')

    if soup.find('td','t'):

        for link in soup.select('td.t a.t'):

            item_link = link.get('href').split('?')[0]
            if p.search(item_link) == None:
                pass
            else:
                url_list.insert_one({'url':item_link})
                print(item_link)
    else:
        pass


def get_item_info(url):
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'lxml')
    no_longer_exist = '404' in soup.find('script', type="text/javascript").get('src').split('/')
    if no_longer_exist:
        pass
    else:
        title = soup.title.text
        price = soup.select('span.price.c_f50',)[0].text
        date  = soup.select('.time')[0].text
        area  = list(soup.select('.c_25d a'))[1].stripped_strings if soup.find_all('span','c_25d') else None
        item_info.insert_one({'title': title, 'price': price, 'date': date, 'area': area, 'url': url})
        print({'title': title, 'price': price, 'date': date, 'area': area, 'url': url})




