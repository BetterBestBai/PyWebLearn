#coding=utf-8
'''
Created on 2016年4月21日

@author: PI
'''
import argparse
import re
import requests
import bs4
import time
import json
from multiprocessing import Pool
import io
from posixfile import fileopen


root_url = 'http://wufazhuce.com'
def get_url(num):
    return root_url + '/one/' + str(num)    
    
def get_urls(num):
    urls = map(get_url, range(100, 100+num))
    return urls 

def get_data(url):
    datalist = {}
    response = requests.get(url)
    if response.status_code !=200:
        return {'noValue':'noValue'}  
    soup = bs4.BeautifulSoup(response.text, 'html.parser')   
    datalist['index'] = soup.title.string[4:8]
    for meta in soup.select('meta'):
        if meta.get('name') == 'description':
            datalist['content'] = meta.get('content')
            print meta.get('content')
    datalist['imgUrl'] = soup.find_all('img')[1]['src']
    
if __name__=='__main__':
    pool = Pool(4)   #pool可以用来创建大量的子进程。
    dataList = []
    urls = get_urls(10)
    start = time.time()
    dataList = pool.map(get_data, urls)
    end = time.time()
    print 'use: %.2f s' % (end - start)
    jsonData = json.dumps({'data':dataList})
    with open('data.txt', 'w') as outfile:
        json.dump(jsonData, outfile)    
        
    
    
    
    
    
    
    
    
    
    
    
    