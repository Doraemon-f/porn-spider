#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" article list crawler """

__author__ = 'shiyu.feng'

import common.http_util as http
from bs4 import BeautifulSoup
import re

PORN_HOME_PAGE_URL = http.DOMAIN + 'index.php'

url = PORN_HOME_PAGE_URL + '?fid=16&search=&page=1'
soup = BeautifulSoup(http.fetch(url), 'html.parser')
page_button = soup.find(id='last').find_previous_sibling().find_previous_sibling()
button_value = page_button.input['value']
max_page_number = int(re.split('/', button_value)[1])

articles = open('images.txt', 'a+')
for index in range(1, max_page_number + 1):
    print 'current page is %d' % index
    url = PORN_HOME_PAGE_URL + '?fid=16&search=&page=' + str(index)
    soup = BeautifulSoup(http.fetch(url), 'html.parser')
    items = soup.find_all('h3')
    text = '\n'.join(str(tag) for tag in items)
    articles.write(text)

articles.close()
