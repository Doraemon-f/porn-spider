#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" a test module """

__author__ = 'shiyu.feng'

import re
import os
import common.http_util as http
from bs4 import BeautifulSoup


def __get_href_and_title(line):
    line_xml = BeautifulSoup(line, 'html.parser')
    return line_xml.h3.a['href'], line_xml.h3.string


def __get_content(html, title):
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.find('div', class_='tpc_content do_not_catch').get_text(strip=True).encode('utf8')
    if not os.path.exists('files'):
        os.mkdir('files')
    porn_article = open('files/' + title + '.txt', 'w+')
    porn_article.write(content)
    porn_article.close()


def __get_article(line):
    href, title = __get_href_and_title(line)
    if 'htm_data' in href:
        article_url = http.DOMAIN + href
        html = http.fetch(article_url)
        __get_content(html, title)


articles = open('articles.txt', 'r')
for url_tag in articles.readlines():
    __get_article(url_tag)
