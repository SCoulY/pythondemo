from urllib.request import urlopen,Request
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import time
import datetime
import random
import re
import os
import pymysql


def getScrap(url):
	try:
		html = urlopen(url)
	except (HTTPError, URLError) as e:
		return e
	try:
		bsObj = BeautifulSoup(html.read(),"html.parser")
	except AttributeError as e:
		return e
	return bsObj

def addheader(link):
	headers = { 
	        # 'Connection':'keep-alive',
	        # 'Cache-Control':'max-age=0',
	        # 'Accept': 'text/html, */*; q=0.01',
	        # 'X-Requested-With': 'XMLHttpRequest',
	        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36',
	        'DNT':'1',
	        'Referer': 'https://translate.google.cn/m/translate#en/zh-CN/',
	        # 'Accept-Encoding': 'gzip, deflate, sdch',
	        # 'Accept-Language': 'zh-CN,zh;q=0.8,ja;q=0.6'
	  		 }
	data = None
	link = Request(link,data,headers)
	return link

link = 'https://translate.google.cn/m/translate#en/zh-CN/'
text = input('请输入待翻译的内容:')
text = text.replace(' ','+')
link = link+text
driver = webdriver.PhantomJS(executable_path=r'D:\CHROME DOWNLOAD\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver.set_page_load_timeout(3)  
driver.set_script_timeout(3)
try:
	driver.get(link)
except Exception as e:
	print('time out')
	try:
		# element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME,'translation')))
		print('译文为:' + driver.find_element(By.CLASS_NAME,'translation').text)
	finally:
		driver.quit()
finally:
	print('finished')
	wait = input()


