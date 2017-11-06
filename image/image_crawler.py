#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" image_crawler """

__author__ = 'shiyu.feng'

import re
import os
import common.http_util as http
from bs4 import BeautifulSoup
import urllib
import requests
import shutil

r = requests.get('http://s9tu.com/images/2017/10/24/TIM20171024093834287c8.jpg', stream=True)
if r.status_code == 200:
    with open('xxxxxxx.jpg', 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)

# def __get_href_and_title(line):
#     line_xml = BeautifulSoup(line, 'html.parser')
#     return line_xml.h3.a['href'], line_xml.h3.string
#
#
# def __get_content(html, title):
#     soup = BeautifulSoup(html, 'html.parser')
#     content = soup.find('div', class_='tpc_content do_not_catch').get_text(strip=True).encode('utf8')
#     if not os.path.exists('article'):
#         os.mkdir('article')
#     porn_article = open('article/' + title + '.txt', 'w+')
#     porn_article.write(content)
#     porn_article.close()
#
#
# def __get_image(line):
#     href, title = __get_href_and_title(line)
#     if 'htm_data' in href:
#         url = http.DOMAIN + href
#         html = http.fetch(url)
#         __get_content(html, title)
#
#
# tags = open('images.txt', 'r')
# for url_tag in tags.readlines():
#     __get_image(url_tag)
#
