'''  Author- FGV587   '''

from bs4 import BeautifulSoup
import requests
import time

def get_link(url):

    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'lxml')

    titles  = soup.select('strong.number ')
    numbers = soup.select('a.t')
    for i in numbers:
        print(i.get('href'))

get_link('http://bj.58.com/shoujihao/')
