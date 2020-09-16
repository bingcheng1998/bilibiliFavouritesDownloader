#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import xPathHelper as xh
import sys
from bs4 import BeautifulSoup
import brotli
from requests.exceptions import RequestException
from threading import Thread
from lxml import etree
import os
import time

FAVORATE_INFO = {
    'url' : "https://api.bilibili.com/x/v3/fav/resource/list",
    'params' : {
        "media_id": "1030308760",
        "pn": "1",
        "ps": "20",
        "keyword": "",
        "order": "mtime",
        "type": "0",
        "tid": "0",
        "jsonp": "jsonp",
    },
    'headers' : {
        "pragma": "no-cache",
        "accept": "application/json, text/plain, */*",
        "sec-fetch-site": "same-site",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "cache-control": "no-cache",
        "sec-fetch-mode": "cors",
        "origin": "https://space.bilibili.com",
        "referer": "https://space.bilibili.com/57626460/favlist?fid=57789760&ftype=create",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
        "dnt": "1",
        "cookie": None,
        "sec-fetch-dest": "empty",
    }
}

LIST_PART_INFO = {
    'url':"https://api.bilibili.com/x/player/pagelist",
    'params':{
        "bvid": "BV1NJ411H7JH",
        "jsonp": "jsonp",
    },
    'headers':{
        "pragma": "no-cache",
        "accept": "*/*",
        "sec-fetch-site": "same-site",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "cache-control": "no-cache",
        "sec-fetch-mode": "cors",
        "origin": "https://www.bilibili.com",
        "referer": "https://www.bilibili.com/video/BV1NJ411H7JH/?spm_id_from=333.788.videocard.0",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
        "dnt": "1",
        "cookie":None,
        "sec-fetch-dest": "empty",
    },
}

def gen_fav_info(INFO, cookie):
    url = INFO['url']
    params = INFO['params']
    headers = INFO['headers']
    headers['cookie'] = cookie
    return url, params, headers

def send_request(url, headers, params, IGNORE404 = False):
    try:
        response = requests.get(
            url=url,
            params=params,
            headers=headers,
        )
        if response.status_code != 200 and not IGNORE404: print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        return response
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

def decode(response):
    key = 'Content-Encoding'
    if(key in response.headers and response.headers['Content-Encoding'] == 'br'):
        try:
            decoded = brotli.decompress(response.content)
        except:
            print('brotli decode error')
            return response.text
        decoded = decoded.decode('utf-8')
        return decoded
    return response.text


def getHTML(url, headers, params, IGNORE404 = False):
	response = send_request(url, headers, params, IGNORE404)
	pre_html = decode(response)
	html = etree.HTML(pre_html)
	return html
