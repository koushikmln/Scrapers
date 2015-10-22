

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
	

	
def homeshop18(homeshop18ProductURL):
	urlSourceCode = urllib2.urlopen(homeshop18ProductURL.strip())
	soup = BeautifulSoup(urlSourceCode)
	products=soup.find_all("div",attrs={"class":"box product_div product_div_last key_height"})
	#print products
	for eachProduct in products:
		title=findTagValueInSoup(eachProduct,'p',{"class":"product_title"})
		link=eachProduct.find('a',attrs={"class":"srch_rslt_img productTitle"})
		productURL="http://www.homeshop18.com"+link['href'].split('?')[0]
		price=findTagValueInSoup(eachProduct,'b',{})
		product=[productURL,title,price]
		#print product
		print >> f_out, '\t'.join(product)

	products=soup.find_all("div",attrs={"class":"box product_div key_height"})
	#print products
	for eachProduct in products:
		title=findTagValueInSoup(eachProduct,'p',{"class":"product_title"})
		link=eachProduct.find('a',attrs={"class":"srch_rslt_img productTitle"})
		productURL="http://www.homeshop18.com"+link['href'].split('?')[0]
		price=findTagValueInSoup(eachProduct,'b',{})
		product=[productURL,title,price]
		#print product
		print >> f_out, '\t'.join(product)		

f_out = open("mobileshomeshop18.csv",'w')
for i in range(67):
	try:
		url=('http://www.homeshop18.com/mobile-phones/category:14569/start:%d/')%(24*i)
		homeshop18(url)
		print i
	except:
		time.sleep(5)
		try:
			homeshop18(url)
		except:
			print url
			time.sleep(5)
			continue

