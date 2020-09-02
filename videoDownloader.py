import sys
from you_get import common as you_get

def download(url, path):
	sys.argv = ['you-get', '-o', path, url]
	you_get.main()

if __name__ == '__main__':
	url='https://www.bilibili.com/video/BV1qt411j7fV'
	path = '../bilibili视频/'
	download(url, path)