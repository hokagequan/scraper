from urllib.request import urlopen
from bs4 import BeautifulSoup

def start_scrap(name):
	print(name)
	html = urlopen("http://www.iqiyi.com/")
	bs_obj = BeautifulSoup(html.read(), "html.parser")
	print(bs_obj.h2)