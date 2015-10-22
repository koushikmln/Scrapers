import sys
import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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
	

	
def infibeam(soup):
	table=soup.find('ul',attrs={"class":"srch_result default"})
	products=table.find_all('li')
	#print products
	for eachProduct in products:
		title=findTagValueInSoup(eachProduct,'span',{"class":"title"})
		#print title.strip()
		if title != 'NA':
			link=eachProduct.find('a')
			link="http://www.infibeam.com"+link['href'].strip().split('?')[0]
			#print link['href']
			price=findTagValueInSoup(eachProduct,'span',{"class":"normal"})
			product=[link,title,price]
			#print product
			print >> f_out, '\t'.join(product)
		

f_out = open("mobilesinfibeam.csv",'w')
for i in range(1,50):
	try:
		driver = webdriver.Firefox()
		url=('http://www.infibeam.com/Mobiles#store=Mobiles&page=%d')%(i)
		doc=driver.get(url)
		soup=BeautifulSoup(driver.page_source)
		driver.close()
		infibeam(soup)
		print i
	except:
		print url	