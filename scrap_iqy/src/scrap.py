from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup
import time
import constants


def goto_search_result_page(keyword):
	pass

def start_scrap(name):
	encode_name = quote(name)
	encode_name = quote("肖生克的救赎")
	url = "{0}q_{1}?source=input&sr={2}".format(constants.iqiyi_so_url, encode_name, int(time.time()))
	html = urlopen(url)
	bs_obj = BeautifulSoup(html.read(), "html.parser")
	print(html.read())
