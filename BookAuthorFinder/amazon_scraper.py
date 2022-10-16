from bs4 import BeautifulSoup
from openpyxl import workbook
import csv
from selenium import webdriver
driver = webdriver.Chrome(executable_path="D:\\setup\\ChromeDriver\\chromedriver_win32\\chromedriver.exe")
book_name = input('Which Books Author Do you Want: ')
book_name = book_name.replace(' ','+')
url = f"https://www.amazon.in/s?k={book_name}&i=stripbooks&ref=nb_sb_noss"
print(url)
driver.get(url)
soup = BeautifulSoup(driver.page_source,'lxml')
section = soup.find('a',class_='a-size-base').text
print(section)
# driver.close()
## Comments Below
# from msedge.selenium_tools import Edge, EdgeOptions
## Startup the Web-Driver
# options = EdgeOptions()
# options.use_chromium = True
# driver = Edge(options = options)
# print(book_name)
# url = 'https://www.amazon.in/s?k=the+psychology+of+money&i=stripbooks&s=review-rank'
# for auth in section:
# 	if(auth.text):
# 		auth_name = auth.text
# 	else:
# 		auth_name = ''
	# print(auth_name)