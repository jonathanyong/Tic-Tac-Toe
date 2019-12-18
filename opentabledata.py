from bs4 import BeautifulSoup
import requests

# Use requests headless browser to retrieve website content
url = "https://www.opentable.com/new-york-restaurant-listings"
html = requests.get(url)
html.text[:]

# Use BeautifulSoup to parse HTML data and find name and price range of all restaurants in page
soup = BeautifulSoup(html.text,'html.parser')
for entry in soup.find_all(name='span',attrs={'class':'rest-row-name-text'}):
    print(entry.text)
for entry in soup.find_all('div',{'class':'rest-row-pricing'}):
    price = entry.find('i').text
    print(price)

# Use selenium to get number of bookings as BeautifulSoup is unable to read JavaScript files
from selenium import webdriver
import time, re
driver = webdriver.Firefox(executable_path = '/Users/jonat/downloads/geckodriver')
driver.get(url)
time.sleep(1)
html = driver.page_source
html = BeautifulSoup(html, "lxml")
for booking in html.find_all('div',{'class':'booking'}):
    match = re.search(r'\d+',booking.text)
    if match:
        print(match.group())

# Define function to parse html of website according to categories
def parse_html(html):
    data, item = pd.DataFrame(),{}
    soup = BeautifulSoup(html,'lxml')
    for i, resto in enumerate(soup.find_all('div',class_='rest-row-info')):
        item['name']=resto.find('span',class_='rest-row-name-text').text
    
        booking = resto.find('div',class_='booking')
        item['bookings']=re.search('\d+',booking.text).group()if booking else 'NA'
        
        rating = resto.select('div.all-stars.filled')
        item['rating'] = int(re.search('\d+',rating[0].get('style')).group()) if rating else 'NA'
        
        reviews = resto.find('span',class_='star-rating-text--review-text')
        
        item['reviews'] = int(re.search('\d+',reviews.text).group()) if reviews else 'NA'
      
        item['price'] = int(resto.find('div', class_='rest-row-pricing').find('i').text.count('$'))

        item['cuisine'] = resto.find('span', class_='rest-row-meta--cuisine').text

        item['location'] = resto.find('span',class_='rest-row-meta--location').text

        data[i] = pd.Series(item)
    return data.T

# Use selenium to follow links to next pages and parse every page using def parse_html
import pandas as pd
restaurants = pd.DataFrame()
driver = webdriver.Firefox(executable_path = '/Users/jonat/downloads/geckodriver')
url = "https://www.opentable.com/new-york-restaurant-listings"
driver.get(url)
while True:
    sleep(1)
    new_data = parse_html(driver.page_source)
    if new_data.empty:
        break
    restaurants = pd.concat([restaurants, new_data], ifnore_index=True)
    print(len(restaurants))
    driver.find_element_by_link_text('Next').click()
driver.close()

# Alternative to selenium & BeautifulSoup, we can use scrapy and splash to retrieve content, parse and store result structuredly
# This portion here is retrieved directly from Stefan Jansen's repo at https://github.com/PacktPublishing/Hands-On-Machine-Learning-for-Algorithmic-Trading/blob/master/Chapter03/01_opentable/opentable/spiders/table_spider.py
from opentable.items import OpentableItem
from scrapy import Spider
from scrapy_splash import SplashRequest

class OpenTableSpider(Spider):
    name = 'opentable'
    start_urls = ['https://www.opentable.com/new-york-restaurant-listings']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url,
                                callback=self.parse,
                                endpoint='render.html',
                                args={'wait': 1},)

    def parse(self, response):
        item = OpentableItem()
        for resto in response.css('div.rest-row-info'):
            item['name'] = resto.css('span.rest-row-name-text::text').extract()
            item['bookings'] = resto.css('div.booking::text').re(r'\d+')
            item['rating'] = resto.css('div.all-stars::attr(style)').re_first('\d+')
            item['reviews'] = resto.css('span.star-rating-text--review-text::text').re_first(r'\d+')
            item['price'] = len(resto.css('div.rest-row-pricing > i::text').re('\$'))
            item['cuisine'] = resto.css('span.rest-row-meta--cuisine::text').extract()
            item['location'] = resto.css('span.rest-row-meta--location::text').extract()
            yield item

# Reference websites to understanding how to read html data: https://medium.com/@rob3hr/how-to-web-scrape-with-python-simplified-670d59fbf510