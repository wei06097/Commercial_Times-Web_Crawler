import datetime
import requests
from bs4 import BeautifulSoup

class Ctee:
    __HEADERS = {
        'authority': 'www.ctee.com.tw',
        'method': 'GET',
        'path': '/rss_web/livenews/policy',
        'scheme': 'https',
        'Referer': 'https://www.ctee.com.tw/livenews/policy',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
    }
    def __get_datetime(self):
        current_datetime = datetime.datetime.now()
        return current_datetime.strftime("%Y-%m-%d %H:%M")
    
    ### 取得文章列表
    def get_article_list(self):
        url = 'https://www.ctee.com.tw/rss_web/livenews/policy'
        response = requests.get(url, headers=self.__HEADERS)
        color = '\033[91m' if response.status_code == 403 else '\033[92m'
        print(f'[{self.__get_datetime()}] {color}{response}\033[0m list\n')

        soup = BeautifulSoup(response.text, 'xml')
        items = soup.find_all('item')
        articles = []
        for item in items:
            article = {
                'id': item.find('guid').text,
                'title': item.find('title').text,
                'link': item.find('link').text,
                'datetime': item.find('pubDate').text,
                'author': item.find('author').text,
            }
            articles.append(article)
        return articles
    
    ### 取得文章內容
    def get_article_content(self, url):
        response = requests.get(url, headers=self.__HEADERS)
        color = '\033[91m' if response.status_code == 403 else '\033[92m'
        print(f'[{self.__get_datetime()}] {color}{response}\033[0m article')
        
        soup = BeautifulSoup(response.text, 'html.parser')
        p_tags = soup.find('article').find_all('p')
        p_tags = [p_tag.text for p_tag in p_tags if p_tag.text != '']
        content = "\n\n".join(p_tags)
        return content
    