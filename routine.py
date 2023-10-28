import excel
from ctee import Ctee

### 主要爬蟲功能
def routine():
    # 沒有檔案就建立
    excel.check_xlsx()
    # 取得文章列表
    ctee = Ctee()
    articles = ctee.get_article_list()
    print('===================================')
    
    # 遍歷文章列表
    counter = 0
    for article in articles[::-1]:
        # 檢查文章是否已經存在
        existing = excel.check_existance(article['id'])
        if (existing):
            counter += 1
            continue
        # 取得文章內容
        content = ctee.get_article_content(article['link'])
        # 新增一筆資料
        data_to_add = [
            article['id'],
            article['title'],
            article['link'],
            article['datetime'],
            article['author'],
            content
        ]
        excel.add_data(data_to_add)
        print(f'\033[92m => Data addition completed\033[0m')
    
    print('===================================')
    message = 'Done' +\
            f'\033[92m ({len(articles)-counter} added)\033[0m' +\
            f'\033[93m ({counter} already exist)\033[0m\n'
    print(message)
