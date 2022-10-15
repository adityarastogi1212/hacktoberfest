from bs4 import BeautifulSoup
from openpyxl import workbook
import csv
from selenium import webdriver
from msedge.selenium_tools import Edge, EdgeOptions
## Startup the Web-Driver
# options = EdgeOptions()
# options.use_chromium = True
driver = webdriver.Chrome(executable_path="D:\\setup\\ChromeDriver\\chromedriver_win32\\chromedriver.exe")
# driver = Edge(options = options)

book_name = input('Which Books Author Do you Want: ')
book_name = book_name.replace(' ','+')
# print(book_name)
url = f"https://www.amazon.in/s?k={book_name}&i=stripbooks&s=review-rank"
# url = 'https://www.amazon.in/s?k=the+psychology+of+money&i=stripbooks&s=review-rank'
print(url)
driver.get(url)
soup = BeautifulSoup(driver.page_source,'lxml')
section = soup.find_all('a',class_='a-size-base a-color-base a-link-normal s-underline-text s-underline-link-text s-link-style')
title = soup.find_all('span',class_='a-size-medium a-color-base a-text-normal')
# auth_name = set()
# book_name = set()

# # pair = {}
# for auth in section:
# 	auth_name.add(auth.text)

# for book in title:
# 	book_name.add(book.text)
# 	# pair.add(new_pair)
# both = zip(book_name,auth_name)
# print(list(both))

# print(auth_name)
# print(book_name)
auth_name = []
book_name = []

# pair = {}
for auth in section:
	auth_name.append(auth.text)

for book in title:
	book_name.append(book.text)
	# pair.add(new_pair)
both = zip(book_name,auth_name)
print(list(both))

# print(auth_name)
# print(book_name)
# for auth,book in section,title:
# 	new_pair = {auth.text:book.text}
# 	pair.update(new_pair)
# for auth in section:
# 	auth_name.add(auth.text)
# 	book_name.add(auth.text)
# 	# pair.add(new_pair)
# print(section)
# for auth in section:
# 	auth_name.add(auth.text)
# 	# pair.add(new_pair)
