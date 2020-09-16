#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import call
def download(url, path):
    print(f"you-get -o '{path}' {url}")
    call(f"you-get -o '{path}' {url}", shell=True)

def playlist(url, path):
    print(f"you-get -o '{path}' --playlist {url}")
    call(f"you-get -o '{path}' --playlist {url}", shell=True)

if __name__ == '__main__':
    url='https://www.bilibili.com/video/BV1gs411a792'
    path = '/Volumes/我的文件/bilibili/默认收藏夹/【480P-DVDRip】Betty Boop_贝蒂小姐 16集全【彩版-生肉】'
    # download(url, path)
    playlist(url, path)