#!/usr/bin/python
# -*- coding: utf-8 -*- 
import MySQLdb
import time
import urllib2
from bs4 import BeautifulSoup
import flipkart
import codecs

#Flipkart
def flipkart_data(flipkartURL):
	""" Scrapes the Flipkart product Details.
		Returns a list of URL, Product_Name, Price, Color, Model, Product_ID
		Takes pageURL as an argument """
	soup = BeautifulSoup(urllib2.urlopen(flipkartURL).read())
	mobile=soup.find("h1", attrs={"itemprop": "name"})
	flipkart_name=mobile.string.strip().replace(',','')
	print flipkart_name
	color=soup.find("div", attrs={"class": "line extra_text bmargin10"})
	flipkart_color=color.string.strip().strip('()').replace(',','')
	print flipkart_color
	price=soup.find("span",attrs={"class":"fk-font-verybig pprice fk-bold"})
	flipkart_price=price.string.strip().replace(',','')
	print flipkart_price
	attribute_soup=str(soup)
	flipkart_model=flipkart_attribute(attribute_soup,'Model Name')
	flipkart_id=flipkart_attribute(attribute_soup,'Model ID')	
	return [flipkartURL,flipkart_name,flipkart_price,flipkart_color,flipkart_model,flipkart_id]

def flipkart_attribute(soup,key):
	""" Finds and Returns attributes of Flipkart Product.
		Arguments are Product-Table-Data and the Attribute-Name. """
	soup=BeautifulSoup(soup)
	try:
		key=soup.find(text=key)
		parent=key.find_parent("td")
		next=parent.find_next("td")
		flipkart_key=next.string.strip().replace(',','')
		print flipkart_key
	except:
		flipkart_key='NA'
		print flipkart_key
	return flipkart_key

def flipkart_variant_data(VariantURL):
	""" Gets the variants and then returns their data. 
		Returns the data of 4 variants if present else returns NA.
		Takes pageURL as argument. """
	soup=BeautifulSoup(urllib2.urlopen(VariantURL).read())
	variants=soup.find("tr",attrs={"id":"irritatingSliderElement-1"})
	if str(variants)=="None":
		flipkart_variant1=null()
		flipkart_variant2=null()
		flipkart_variant3=null()
		flipkart_variant4=null()
	else:
		variant=str(variants)
		flipkart_variantURL1=flipkart_variantURL(variant)
		flipkart_variant1=flipkart_data(flipkart_variantURL1)
		variants=soup.find("tr",attrs={"id":"irritatingSliderElement-2"})
		if str(variants)=="None":
			flipkart_variant2=null()
			flipkart_variant3=null()
			flipkart_variant4=null()
		else:
			variant=str(variants)
			flipkart_variantURL2=flipkart_variantURL(variant)
			flipkart_variant2=flipkart_data(flipkart_variantURL2)
			variants=soup.find("tr",attrs={"id":"irritatingSliderElement-3"})
			if str(variants)=="None":
				flipkart_variant3=null()
				flipkart_variant4=null()
			else:
				variant=str(variants)
				flipkart_variantURL3=flipkart_variantURL(variant)
				flipkart_variant3=flipkart_data(flipkart_variantURL3)
				variants=soup.find("tr",attrs={"id":"irritatingSliderElement-4"})
				if str(variants)=='None':
					flipkart_variant4=null()
				else:
					variant=str(variants)
					flipkart_variantURL4=flipkart_variantURL(variant)
					flipkart_variant4=flipkart_data(flipkart_variantURL4)
	return[flipkart_variant1,flipkart_variant2,flipkart_variant3,flipkart_variant4]	

def flipkart_variantURL(variant):
	""" Gets and returns the VariantURL.
		Takes variant table data as argument. """ 
	variants=BeautifulSoup(variant)
	url=variants.find('a')
	flipkarturl=url['href'].strip()
	flipkart_url='http://www.flipkart.com'+flipkarturl.split('&')[0]
	print flipkart_url
	return flipkart_url


#Amazon
def amazon_data(amazonURL):
	""" Scrapes the Flipkart product Details.
		Returns a list of URL, Product_Name, Price, Color, Model
		Takes pageURL as an argument """
	try:
		soup = BeautifulSoup(urllib2.urlopen(amazonURL).read())
		head=soup.find("span", attrs={"id": "btAsinTitle"})
		amazon_name=str(head.get_text()).strip().replace(',','')
		print amazon_name
		price=soup.find("b", attrs={"class": "priceLarge"})
		amazon_price=price.get_text()
		amazon_price = amazon_price.encode('ascii','ignore').strip().replace(',','')
		print amazon_price
		attributesoup=soup.find('div',attrs={'class':'content pdClearfix'})
		attributesoup=str(attributesoup)
		amazon_model=amazon_attribute(attributesoup,'Item model number')
		amazon_color=amazon_attribute(attributesoup,' Colour ')
		return [amazonURL,amazon_name,amazon_price,amazon_color,amazon_model,'NA']
	except:
		return [amazonURL,'NA','NA','NA','NA','NA']

def amazon_attribute(soup,key):
	""" Finds and Returns attributes of Amazon Product.
		Arguments are Product-Table-Data and the Attribute-Name. """
	try:
		soup=BeautifulSoup(soup)
		key=soup.find(text=key)
		parent=key.find_parent('td')
		sibling=parent.find_next('td')
		amazon_key=sibling.string.strip().replace(',','')
	except:
		amazon_key='NA'
	print amazon_key
	return amazon_key

#ebay
def ebay_data(ebayURL):
	""" Scrapes the ebay product Details.
		Returns a list of URL, Product_Name, Price
		Takes pageURL as an argument """
	soup = BeautifulSoup(urllib2.urlopen(ebayURL).read())
	head=soup.find(id="vi-lkhdr-itmTitl")
	try:
		ebay_name=str(head.string).strip().replace(',','')
		price=soup.find(id="prcIsum")
		ebay_price=str(price.string).strip().replace(',','')
	except:
		ebay_name='NA'
		ebay_price='NA'
	print ebay_name
	print ebay_price
	return[ebayURL,ebay_name,ebay_price,'NA','NA','NA']


#HomeShop18
def homeshop18_data(homeshop18URL):
	""" Scrapes the HomeShop18 product Details.
		Returns a list of URL, Product_Name, Price, Color, Model, Product_ID
		Argument is ProductURL """
	soup = BeautifulSoup(urllib2.urlopen(homeshop18URL).read())
	head=soup.select("span#productTitleInPDP")
	h1=head[0].string
	try:
		h2=str(h1).split('-')
		homeshop18_name=h2[0].strip().replace(',','')
		homeshop18_color=h2[1].strip().replace(',','')
	except:
		homeshop18_name=h1
		homeshop18_color='NA'
	print homeshop18_name
	print homeshop18_color
	price=soup.find(id="hs18Price")
	hsprice=str(price).split('</span>')
	homeshop18_price=hsprice[1].decode('utf8').encode('ascii','ignore').strip().replace(',','')
	print homeshop18_price
	div=soup.find_all("div",attrs={"class":"productDetails"})
	divsoup=str(div)
	homeshop_brand=homeshop_attribute(divsoup,'Brand')
	homeshop18_model=homeshop_brand + homeshop_attribute(divsoup,'Model')
	homeshop18_id=homeshop_attribute(divsoup,'Model Number')
	return [homeshop18URL,homeshop18_name,homeshop18_price,homeshop18_color,homeshop18_model,homeshop18_id]

def  homeshop_attribute(soup,key):
	""" Finds and Returns attributes of HomeShop18 Product.
		Arguments are Product-Table-Data and the Attribute-Name. """
	soup=BeautifulSoup(soup)
	try:
		key=soup.find(text=key)
		span=key.find_parent("span")
		td=span.find_parent("td")
		sibling=td.find_next_sibling("td")
		homeshop18_key=sibling.string.strip().replace(',','')
		print homeshop18_key
	except:
		homeshop18_key="NA"
		print homeshop18_key
	return homeshop18_key


#infibeam
def infibeam_data(infibeamURL):
	""" Scrapes the Infibemam product Details.
		Returns a list of URL, Product_Name, Price, Color
		Argument is ProductURL """
	soup = BeautifulSoup(urllib2.urlopen(infibeamURL).read())
	head=soup.find("h1", attrs={"class": "product-title-big "})
	try:
		h2=(str(head.string)).split('(')
		infibeam_name=h2[0].strip().replace(',','')
		infibeam_color=h2[1].strip().strip('(').strip(')').replace(',','')
	except:
		infibeam_name=head.string.strip()
		infibeam_color='NA'
	print infibeam_name
	print infibeam_color
	price=soup.find("span", attrs={"class": "price"})
	infibeam_price=price.string.strip().replace(',','')
	print infibeam_price
	return [infibeamURL,infibeam_name,infibeam_price,infibeam_color,'NA','NA']

def null():
	return ['NA','NA','NA','NA','NA','NA']
def null_variant():
	return [null(),null(),null(),null()]


def main():
	db = MySQLdb.connect("localhost","root","cassandra","mysmartprice" )
	cursor=db.cursor()
	sql = "SELECT * FROM storelinks"
	cursor.execute(sql)
	f=open('finaldata.csv','w')
	sql1 = "SELECT * FROM mobiles"
	cursor1=db.cursor()
	cursor1.execute(sql1)
	results1=cursor1.fetchall()
	results=cursor.fetchall()
	for row,row1 in zip(results,results1):
		#flipkart
		if row[1]!='NA':
			print 'Flipkart'
			flipkart=flipkart_data(row[1])
			flipkart_variant=flipkart_variant_data(row[1])
		else:
			flipkart=null()
			flipkart_variant=null_variant()			  
		#amazon
		if row[2]!='NA':
			amazon=amazon_data(row[2])
			amazon_variant=null_variant()		
		else:
			amazon=null()
			amazon_variant=null_variant()
		#ebay
		if row[3]!='NA':
			print 'ebay'
			ebay=ebay_data(row[3])
			ebay_variant=null_variant()		
		else:
			ebay=null()
			ebay_variant=null_variant()
		#snapdeal
		if row[4]!='NA':
			print 'Snapdeal'
			snapdeal=null()
			print snapdeal
			snapdeal_variant=null_variant()
		else:
			snapdeal=null()
			snapdeal_variant=null_variant()
		#homeshop18
		if row[5]!='NA':
			print 'HomeShop18'
			homeshop18=homeshop18_data(row[5])
			homeshop18_variant=null_variant()
		else:
			homeshop18=null()
			homeshop18_variant=null_variant()
		#infibeam
		if row[6]!='NA':
			print 'Infibeam'
			infibeam=infibeam_data(row[6])
			infibeam_variant=null_variant()		
		else:
			infibeam=null()
			infibeam_variant=null_variant()	

		f.write(str([row1[0].strip(),row1[1],row1[2],
			flipkart,flipkart_variant,amazon,amazon_variant,
			ebay,ebay_variant,snapdeal,snapdeal_variant,
			homeshop18,homeshop18_variant,infibeam,infibeam_variant]).strip().replace('[','').replace(']',''))
		f.write('\n')
	db.close()
	f.close()

if __name__ == "__main__":
    main()

	

