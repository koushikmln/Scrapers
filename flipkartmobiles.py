

import sys
import urllib2
from bs4 import BeautifulSoup
import time


def findTagValueInSoup(soup, tagName, attrsDict):
	element = soup.find(tagName, attrsDict)
	if element:
		try:
			elementValue = element.get_text().decode('utf8').encode("ascii","ignore").strip()
		except:
			elementValue = element.get_text().encode("ascii","ignore").strip()
	else:
		elementValue = "NA"
	
	return elementValue
	

	
def flipkart(flipkartProductURL):
	urlSourceCode = urllib2.urlopen(flipkartProductURL.strip())
	soup = BeautifulSoup(urlSourceCode)
	products=soup.find_all('div',attrs={"class":"pu-details lastUnit"})
	for eachProduct in products:
		title=findTagValueInSoup(eachProduct,'div',{"class":"pu-title fk-font-13"})
		#print title.strip()
		link=eachProduct.find('a')
		link="http://www.flipkart.com"+link['href'].strip().split('&')[0]
		#print link['href']
		price=findTagValueInSoup(eachProduct,'div',{"class":"pu-final"})
		product=[link,title,price]
		#print product
		print >> f_out, '\t'.join(product)
		

f_out = open("mobilesflipkart.csv",'a')
for i in [88,104]:
	try:
		url=('http://www.flipkart.com/mobiles/pr?p[]=sort=price_asc&sid=tyy,4io&&start=%d')%(20*i)
		flipkart(url)
	except:
		time.sleep(5)
		try:
			flipkart(url)
		except:
			print url
			time.sleep(5)
			continue