#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" a test module """

__author__ = 'shiyu.feng'

import urllib2
import urllib
import gzip
import StringIO
import re
from bs4 import BeautifulSoup

DOMAIN = 'http://cl.roka.pw/'
PORN_URL = DOMAIN + 'thread0806.php'
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'


def unzip(data):
    data = StringIO.StringIO(data)
    gz = gzip.GzipFile(fileobj=data)
    data = gz.read()
    gz.close()
    return data


def trans_code(response):
    return unzip(response.read()).decode('gbk').encode('utf-8')


def fetch(url):
    request = urllib2.Request(url)
    request.add_header('User-Agent', USER_AGENT)
    request.add_header('Accept-Encoding', 'gzip, deflate')
    return trans_code(urllib2.urlopen(request))


# url = PORN_URL + '?fid=20&search=&page=1'
# soup = BeautifulSoup(fetch(url), 'html.parser')
# page_button = soup.find(id='last').find_previous_sibling().find_previous_sibling()
# button_value = page_button.input['value']
# max_page_number = int(re.split('/', button_value)[1])
# articles = open('articles.txt', 'a')
# for index in range(1, max_page_number + 1):
#     print 'current page is %d' % index
#     url = PORN_URL + '?fid=20&search=&page=' + str(page_number)
#     soup = BeautifulSoup(fetch(url), 'html.parser')
#     items = soup.find_all('h3')
#     text = '\n'.join(str(tag) for tag in items)
#     articles.write(text)
#
# articles.close()

def get_href_and_title(line):
    line_xml = BeautifulSoup(line, 'html.parser')
    return line_xml.h3.a['href'], line_xml.h3.string


def get_article(line):
    href, title = get_href_and_title(line)
    article_url = DOMAIN + href
    html = fetch(article_url)
    get_content(html, title)


def get_content(html, title):
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.find('div', class_='tpc_content do_not_catch')
    print title
    #porn_article = open('article/' + title + '.txt', 'w')
    #porn_article.write(content)
    #porn_article.close()


porn_files = open('articles.txt', 'r')
for line in porn_files.readlines():
    get_article(line)
