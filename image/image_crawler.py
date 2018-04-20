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
import urllib3
import urllib2

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def __get_picture(url, title, index):
    try:
        response = requests.get(url, stream=True, timeout=2, verify=False)
        if response.status_code == 200:
            with open('pictures/' + title + '/' + str(index) + '.jpg', 'wb') as f:
                response.raw.decode_content = True
                shutil.copyfileobj(response.raw, f)
    except requests.exceptions.ConnectTimeout as e:
        print 'connect time out'
    except requests.exceptions.ReadTimeout as e:
        print 'read time out'
    except requests.exceptions.SSLError as e:
        print 'ssl error'
    except urllib3.exceptions.ReadTimeoutError as e:
        print 'read time out'
    except urllib2.HTTPError as e:
        print '404: not found'
    except requests.exceptions.ConnectionError as e:
        print 'connect error'


def __get_content(html, title):
    if not os.path.exists('pictures'):
        os.mkdir('pictures')
    if not os.path.exists('pictures/' + title):
        os.mkdir('pictures/' + title)
    soup = BeautifulSoup(html, 'html.parser')
    images = soup.find_all('input', type='image')
    for index, image in enumerate(images):
        print image['src']
        __get_picture(image['src'], title, index)


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
