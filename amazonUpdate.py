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

def scrapAmazon(amazonURL):
	urlSourceCode = urllib2.urlopen(amazonURL.strip())
	soup = BeautifulSoup(urlSourceCode)
	productPrice = findTagValueInSoup(soup, "b", {"class": "priceLarge"})
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
			newPrice=scrapAmazon(row[1])
			sql='update '+tableName+' set productPrice="'+newPrice+'" where AMZ_URL="'+row[1]+'"'
			cursor.execute(sql)
			print newPrice
		except:
			print row[3]
	db.commit()
	db.close()

if __name__ == '__main__':
	main()