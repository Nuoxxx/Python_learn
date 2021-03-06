# coding:utf8
'''
Created on 2017��4��26��

@author: kaiyue
'''

from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin


class HtmlParser(object):
    
    
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        #<a target="_blank" href="/item/%E8%83%B6%E6%B0%B4%E8%AF%AD%E8%A8%80">胶水语言</a>
        links = soup.find_all('a',href = re.compile(r'/item/*'))
        for link in links:
            new_url = link['href']
            new_full_url = urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls
    
    
    def _get_new_data(self, page_url, soup):
        res_data = {}
        
        #url
        res_data['url'] = page_url
        
        #<dd class="lemmaWgt-lemmaTitle-title><h1>Python</h1>
        title_node = soup.find('dd',class_ = 'lemmaWgt-lemmaTitle-title').find("h1")
        res_data['title'] = title_node.get_text()
        
        #<div class="lemma-summary">
        summary_data = soup.find('div',class_ = 'lemma-summary')
        res_data['summary'] = summary_data.get_text()
        return res_data
        
    
    
    def parse(self,page_url, html_cont):
        
        if page_url is None or html_cont is None:
            return
        
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')       
        new_urls = self._get_new_urls(page_url,soup)              
        new_data = self._get_new_data(page_url,soup)        
        return new_urls,new_data
    
    



