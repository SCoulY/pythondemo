from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
def getTag(url):
	try:
		html = urlopen(url)
	except (HTTPError, URLError) as e:
		return None
	try:
		bsObj = BeautifulSoup(html.read())
	except AttributeError as e:
		return None
	return bsObj
url = 'http://www.pythonscraping.com/pages/pages3.html'
namelist = getTag(url).find('table',{'id':'giftList'}).children()
for child in namelist:
	print (child.get_text())
# title = getTag('http://www.baidu.com')
# if title == None:
# 	print('title not found')
# else:
# 	print(title)