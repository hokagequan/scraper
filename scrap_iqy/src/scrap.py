from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup
import time
import constants
import url_handler


def start_scrap(name):
	name = "肖生克的救赎"
	encode_name = quote(name)
	url = "{0}q_{1}?source=input&sr={2}".format(constants.iqiyi_so_url, encode_name, int(time.time()))
	html = urlopen(url)
	bs_obj = BeautifulSoup(html.read(), "html.parser")
	search_result = bs_obj.find("ul", {"class": "mod_result_list"})
	rel_list = search_result.find_all("li", {"class": "list_item"})
	if rel_list:
		first_ele = rel_list[0]
		try:
			url = first_ele.find("a", {"class": "info_play_btn"}).get("href")
		except Exception as e:
			raise e
		else:
			print(url)
