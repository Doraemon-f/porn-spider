#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" a test module """

__author__ = 'shiyu.feng'

import urllib2
import urllib
import gzip
import StringIO

DOMAIN = 'http://cl.roka.pw/'
__USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'


def __trans_code(response):
    return __unzip(response.read()).decode('gbk').encode('utf-8')


def __unzip(data):
    data = StringIO.StringIO(data)
    gz = gzip.GzipFile(fileobj=data)
    data = gz.read()
    gz.close()
    return data


def fetch(url):
    request = urllib2.Request(url)
    request.add_header('User-Agent', __USER_AGENT)
    request.add_header('Accept-Encoding', 'gzip, deflate')
    return __trans_code(urllib2.urlopen(request))
