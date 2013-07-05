#!/usr/bin/python3

import os
import sys
from bs4 import BeautifulSoup
import urllib.request
import time

def wget(savefile = '', url = '', url_encoding = 'utf8'):
	user_agent = 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36'
	
	if url == '' or savefile == '':
		return
	
	try:
		if url[0:4] == 'http':
			url = url.replace("http://", '')
			
	except NameError as e:
		sys.stderr.write(e)
		return
		
	url = urllib.request.quote(url, safe = '\/|\&|\?|\=', encoding = url_encoding)
	url = 'http://' + url


	try:
		req = urllib.request.Request(url)
		req.add_header('user-agent', user_agent)
		req.add_header('referer', url)
		
		data = urllib.request.urlopen(req).read()
		with open(savefile, 'wb') as f:
			f.write(data)
		
	except Exception as e:
		sys.stderr.error(e)
		
def get_page(url, encoding = 'utf8'):
	user_agent = 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36'
	
	if url == '':
		return
	
	try:
		if url[0:4] == 'http':
			url = url.replace("http://", '')
			
	except NameError as e:
		sys.stderr.write(e)
		return
		
	url = urllib.request.quote(url, safe = '\/|\&|\?|\=', encoding = encoding)
	url = 'http://' + url
	
	
if __name__ == '__main__':
	url = sys.argv[1]
	filename = str(time.time())
	
	wget(filename, url)
	
