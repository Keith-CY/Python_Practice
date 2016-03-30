import urllib.request
import re
from bs4 import BeautifulSoup


url = "http://movie.douban.com/top250?start=0"

html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser', from_encoding = 'utf-8')
links = soup.find_all('a')

titles = soup.find_all('span', class_='title')
for title in titles:
	title = title.get_text()
	if title.find('/') == -1:
		print(title)