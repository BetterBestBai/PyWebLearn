#coding=utf-8
'''
Created on 2016年4月21日

@author: PI
'''
import  requests
import bs4
response = requests.get('http://wufazhuce.com/one/1293')
soup = bs4.BeautifulSoup(response.text, 'html.parser')
print soup
print soup.title.string[4:8]
