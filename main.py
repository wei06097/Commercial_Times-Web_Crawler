import requests
from bs4 import BeautifulSoup

HEADERS = {
    'authority': 'www.ctee.com.tw',
    'Referer': 'https://www.ctee.com.tw/livenews/policy',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

########################################
def get_article_list():
    url = 'https://www.ctee.com.tw/rss_web/livenews/policy'
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'xml')
    items = soup.find_all('item')
    articles = []
    for item in items:
        article = {
            'title': item.find('title').text,
            'link': item.find('link').text,
            'datetime': item.find('pubDate').text
        }
        articles.append(article)
    return articles

def get_article(url):
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')
    p_tags = soup.find('article').find_all('p')
    p_tags = [p_tag.text for p_tag in p_tags if p_tag.text != '']
    description = "\n\n".join(p_tags)
    return description

########################################
if __name__ == '__main__':
    articles = get_article_list()
    for index, article in enumerate(articles):
        print(f'No.{index}')
        print(f'title: {article["title"]}')
        print(f'link: {article["link"]}')
        print(f'datetime: {article["datetime"]}\n')

    description = get_article(articles[0]['link'])
    print("========================================")
    print(f'[{articles[0]["title"]}]\n\n{description}')
    