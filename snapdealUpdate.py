import MySQLdb
import time
import urllib2
from bs4 import BeautifulSoup

def databaseConnect():
	username='root'
	password='cassandra'
	database='mysmartprice'
	db = MySQLdb.connect("localhost",username,password,database)
	return db

def findTagValueInSoup(soup, tagName, attrsDict):
	element = soup.find(tagName, attrsDict)
	if element:
		elementValue = element.get_text().encode("ascii","ignore").strip()
	else:
		elementValue = "NA"
	
	return elementValue

def scrapSnapdeal(snapdealURL):
	urlSourceCode = urllib2.urlopen(snapdealURL.strip())
	soup = BeautifulSoup(urlSourceCode)
	productPrice = findTagValueInSoup(soup, "span", {"itemprop": "price","id":"selling-price-id"})
	if productPrice=="NA":
		seller=soup.find(id="mvfrstVisible")
		productPrice = findTagValueInSoup(seller, "strong", {"class":"redText fnt19"})
	return productPrice

def main():
	db=databaseConnect()
	cursor=db.cursor()
	#set Table Name Here
	tableName='`TABLE 12`'
	sql = "SELECT * FROM "+tableName
	cursor.execute(sql)
	results=cursor.fetchall()
	for row in results:
		try:
			newPrice=scrapSnapdeal(row[1])
			sql='update '+tableName+' set productPrice="'+newPrice+'" where SD_URL="'+row[1]+'"'
			cursor.execute(sql)
		except:
			print row[3]
	db.commit()
	db.close()

if __name__ == '__main__':
	main()