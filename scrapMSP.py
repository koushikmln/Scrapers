"""
AUTHOR : SANJAY KUMAR AGARWAL
OWNER : KAMPAYER.IN
DATE : MAY 22, 2014
"""

import sys
import urllib2
from bs4 import BeautifulSoup

storeIndex = {"flipkart":0, "amazon":1, "homeshop18":2, "infibeam":3, "ebay":4, "snapdeal":5}

def getShortestLink(productURL, productStore):
	productURL = urllib2.unquote(productURL)

	if productStore == "homeshop18":
		return urllib2.unquote(productURL.strip().split('redirect=')[-1]).split('?')[0]
	if productStore == "amazon":
		return 'http://www.amazon.in/dp/'+productURL.strip().split('/')[5]
	if productStore == "flipkart":
		return productURL.strip().split('&')[0]
	if productStore == "infibeam":
		return productURL.strip().split('?')[0]
	if productStore == "ebay":
		return urllib2.unquote(productURL.strip().split('&mpre=')[-1]).split('?')[0]
	if productStore == "snapdeal":
		return "NA"

	return "1";
		
def categoryScrap(categoryURL, category, fileName):
	urlSourceCode = urllib2.urlopen(categoryURL.strip())
	soup = BeautifulSoup(urlSourceCode)
	tableOfProducts = soup.findAll('div', 'listitems_rd')[0]
	products = tableOfProducts.findAll('div', 'msplistitem')
	
	f = open(fileName,'a')
	for product in products:
		mspId = product['data-mspid']
		productInfo = product.findAll('a', 'item-title')[0]
		productName = productInfo.text
		productURL = productInfo['href']
		print >> f, '\t'.join([mspId.strip(), productName.strip(), urllib2.unquote(productURL).strip()])
	
	nextPage = soup.find('a', 'msplistnav next')
	if nextPage:
		categoryScrap(nextPage['href'], category, fileName)
	
	f.close()
	return 1;
		

def productScrap(productURL, fileName, mspId, mspName):
	urlSourceCode = urllib2.urlopen(productURL.strip())
	soup = BeautifulSoup(urlSourceCode)
	tableStores = soup.findAll('div', "price_table_in")[0]
	stores = tableStores.findAll('div', "store_pricetable")
	f = open(fileName,'a')
	productStores = []
	for store in stores:
		if store.find('div', 'store_price').string == "Not Available":
			break;
		storeInfo = store.find('a')
		generalStoreLinkMSP, storeName = storeInfo['href'], storeInfo.find('img')['alt']
		if storeName not in ["flipkart", "amazon", "homeshop18", "infibeam", "ebay", "snapdeal"]:
			continue;

		generalStoreLink = BeautifulSoup(urllib2.urlopen(generalStoreLinkMSP)).find('a', "store-link")['href']
		productStores.append([storeName, generalStoreLink])
	
	storeInfos = [mspId, mspName, "NA", "NA", "NA", "NA", "NA", "NA"]
	for productStore in productStores:
		storeInfos[storeIndex[productStore[0]]+2] = getShortestLink(productStore[1], productStore[0])
	
	print >> f, '\t'.join(storeInfos)
	f.close()
	return 1;


f = open("mobile_phones.csv",'r')

for line in f:
	line = line.strip().split(',')
	try:
		productScrap(line[2], "productStores.csv",line[0],line[1])
	except:
		print line
f.close()