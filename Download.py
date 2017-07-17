from urllib.request import urlretrieve
from urllib.request import urlopen
import os
from bs4 import BeautifulSoup 

html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html)
image = bsObj.find('a', {'id': 'logo'}).find('img')['src']

path = 'C:\\Users\\SCoulY\\Desktop\\myPythonfile'
name = 'logo.jpg'
fullpath = os.path.join(path,name)
if not os.path.exists(path):
	os.makedirs(path)

urlretrieve(image,fullpath)
