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


def __get_picture(url):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(url, 'wb+') as f:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, f)


def __get_content(html, title):
    if not os.path.exists('pictures'):
        os.mkdir('pictures')
    if not os.path.exists('pictures/' + title):
        os.mkdir('pictures/' + title)
    soup = BeautifulSoup(html, 'html.parser')
    images = soup.find_all('input', type='image')
    for image in images:
        print image['src']
        __get_picture(image['src'])


def __get_href_and_title(line):
    line_xml = BeautifulSoup(line, 'html.parser')
    return line_xml.h3.a['href'], line_xml.h3.string


def __get_image(line):
    href, title = __get_href_and_title(line)
    if 'htm_data' in href:
        url = http.DOMAIN + href
        html = http.fetch(url)
        __get_content(html, title)


tags = open('images.txt', 'r')
for url_tag in tags.readlines():
    __get_image(url_tag)
