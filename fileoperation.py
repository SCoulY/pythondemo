from urllib.request import urlopen
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import csv
from zipfile import ZipFile
from io import BytesIO
from bs4 import BeautifulSoup

def csvdecoder():
	text = urlopen('http://pythonscraping.com/files/MontyPythonAlbums.csv').read().decode('ascii','ignore')
	datafile = StringIO(text)
	csv = csv.reader(datafile)
	for row in csv:
		print(row)

# pdffile = urlopen('http://pythonscraping.com/pages/warandpeace/chapter1.pdf')
def pdfdecoder(pdffile):
	rsrcmgr = PDFResourceManager()
	retestr = StringIO()
	laparams = LAParams()
	device = TextConverter(rsrcmgr,retestr,laparams=laparams)
	process_pdf(rsrcmgr,device,pdffile)
	device.close()
	content = retestr.getvalue()
	retestr.close()
	return content


# output = pdfdecoder(pdffile)
# print(output)
# pdffile.close()

# wordfile = urlopen('http://pythonscraping.com/pages/AwordDocument.docx').read()
# wordfile = open(r'C:\Users\SCoulY\Desktop\English report.docx','rb').read()
def worddecoder(wordfile):
	wordfile = BytesIO(wordfile)
	document = ZipFile(wordfile)
	xml_content = document.read('word/document.xml')
	wordobj = BeautifulSoup(xml_content.decode('utf-8'),'xml')
	textString = wordobj.findAll('w:t')
	for text in textString:
		print(text.text)

# worddecoder(wordfile)

