'''
ONLY WORKS ON DESKTOP, NEED TO UPDATE EXE_PATH FOR LAPTOP INSTANCE.
'''

##https://www.youtube.com/watch?v=_AeudsbKYG8&t=1s
##Requires beautiful soup & selenium

##################################################################################

import csv
from bs4 import BeautifulSoup
from selenium import webdriver
import pprint as pp


######### Initialise web driver #########

##init webdriver - hard coded path to executable.
driver = webdriver.Chrome(executable_path='C:/Python38/Lib/site-packages/selenium/webdriver/chrome/chromedriver.exe')

##Def webpage to scrape
def get_url(search_term):
    template = 'https://www.amazon.co.uk/s?k={}&ref=nb_sb_noss'
    search_term = search_term.replace(' ', '+')
    return template.format(search_term)
url = get_url('wireless headphones')

##Pass url into webdriver
driver.get(url)

##parse data using BS
soup = BeautifulSoup(driver.page_source, 'html.parser')

##Locate all matched divs
## We go with the below div ID because this is the highest level div that fully contains a search result element.
results = soup.find_all('div',{'data-component-type': 's-search-result'})

##pp.pprint(results[0])

######### Output formating #########

##description tag
item = results[2]
atag = item.h2.a
description = atag.text.strip()

##item url
url = 'https://www.amazon.co.uk' + atag.get('href')


##Ratings & Price
price_parent = item.find('span', 'a-price')
price = price_parent.find('span', 'a-offscreen').text
rating = item.i.text

pp.pprint(price)