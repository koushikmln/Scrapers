

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
	

	
def amazon(amazonProductURL):
	urlSourceCode = urllib2.urlopen(amazonProductURL.strip())
	soup = BeautifulSoup(urlSourceCode)
	products=soup.find_all("div",attrs={"class":"fstRowGrid prod celwidget"})
	#print products
	for eachProduct in products:
		title=findTagValueInSoup(eachProduct,'h3',{"class":"newaps"})
		link=eachProduct.find('a')
		productURL="http://www.amazon.in/dp/"+link['href'].strip().split('/')[5]
		price=findTagValueInSoup(eachProduct,'span',{"class":"bld lrg red"})
		product=[productURL,title,price]
		#print product
		print >> f_out, '\t'.join(product)

	products=soup.find_all("div",attrs={"class":"rsltGrid prod celwidget"})
	#print products
	for eachProduct in products:
		title=findTagValueInSoup(eachProduct,'h3',{"class":"newaps"})
		link=eachProduct.find('a')
		productURL="http://www.amazon.in/dp/"+link['href'].strip().split('/')[5]
		price=findTagValueInSoup(eachProduct,'span',{"class":"bld lrg red"})
		product=[productURL,title,price]
		#print product
		print >> f_out, '\t'.join(product)
	nextPage=soup.find(id="pagnNextLink")
	try:
		pageLink = "http://www.amazon.in" + nextPage['href'].strip()
		print pageLink
	except:
		pageLink='NA'
	return pageLink


f_out = open("mobilesamazon.csv",'w')
pageLink=amazon(urllib2.unquote("http://www.amazon.in/s/ref=lp_1389401031_nr_n_1?rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1389401031%2Cn%3A1389432031&bbn=1389401031&ie=UTF8&qid=1401790556&rnid=1389401031"))
while(pageLink!='NA'):
	pageLink=amazon(pageLink)
