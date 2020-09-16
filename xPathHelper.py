#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 作者的所有作品页：https://nhentai.net/artist/nagi-wataru/
artist = { 
	'data_tags' 	: '//*[@id="content"]/div[2]/div[*]/@data-tags' ,# 标签，表示语言，种类等信息： '29963 17249 33236 14283 21712 23895 33173 8368'
	'manga_link' 	: '//*[@id="content"]/div[2]/div[*]/a/@href' ,# 单个漫画链接： '/g/318814/'
	'thumb_pic'		: '//*[@id="content"]/div[2]/div[*]/a/img/@data-src' ,#封面小图
	'title' 		: '//*[@id="content"]/div[2]/div[*]/a/div/text()' ,# 漫画题目
	'name'			: '//*[@id="content"]/h1/a/span[1]/text()' , #作者姓名
	'num' 			: '//*[@id="content"]/h1/a/span[2]/text()' #作品数量
		}
# 用户个人的收藏夹中文件下载
favorite = {
	'BV_id'			: '//*[@class="fav-video-list clearfix content"]//*[@class="small-item"]/*[@class="title"]/@href',
	# BV 为所有有效的 //www.bilibili.com/video/BV19k4y1678w
	'title'			: '//*[@class="fav-video-list clearfix content"]//*[@class="small-item"]/*[@class="title"]/text()',
	'UP'		: '//*[@class="fav-video-list clearfix content"]//*[@class="small-item"]//*[@class="author"]/text()',
	# UP主：洛温阿特金森
	'owner'			: '//*[@class="fav-up-name"]/text()', 
	# 这个收藏夹的建立者的名称 创建者：希颜咸
	'fav_name'		:'//*[@class="favInfo-details"]//*[@class="fav-name"]/text()',
	# 收藏夹名称 音乐
	'num'			: '//*[@class="favInfo-details"]//*[@class="fav-meta"]/span/text()' ,
	# 收藏夹的作品总数 [创建者：希颜咸 播放数：0 54个内容 · 公开] 一个list，需要自己处理
	'favorite_pages': '//*[@class="be-pager-total"]/text()',
	# 共 3 页，
}


def html2info():
    data_tags 	= html.xpath(xh.manga['data_tags'])
    manga_id  	= html.xpath(xh.manga['manga_id'])[0]
    thumb_pic	= html.xpath(xh.manga['thumb_pic'])[0]
    h1_title 	= html.xpath(xh.manga['h1_title'])
    h2_title 	= html.xpath(xh.manga['h2_title'])
    pages 		= html.xpath(xh.manga['pages'])[0]
    pages_icon 	= html.xpath(xh.manga['pages_icon'])
    datetime 	= html.xpath(xh.manga['datetime'])[0]
    imgs 		= html.xpath(xh.manga['imgs'])
    return data_tags, manga_id ,thumb_pic,h1_title ,h2_title ,pages,pages_icon,datetime ,imgs 	





