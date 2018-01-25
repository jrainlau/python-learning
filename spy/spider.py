
from bs4 import BeautifulSoup
import requests
import os

def visit_page(url):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
    }
    r = requests.get(url, headers = headers)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'lxml')
    return soup

def get_article_urls(page):
    articles = page.select('body > div.p_list > div.wrapper1200 > div > section.main.fl > div.con > div.bd > ul > li > p > a')
    collect = []

    for article in articles:
        data = {
            'title': article.get_text(),
            'url': 'http://laotiese.org' + article.get('href')
        }
        collect.append(data)

    return collect

def get_article(articles_urls):
    for index, article in enumerate(articles_urls):
        article_page = visit_page(article['url'])
        title = article['title']
        content = article_page.select('#content_news')[0].get_text()
        with open('./articles/' + title + '.txt', 'w+') as f:
            print('正在下载第' + str(index + 1) + '/' + str(len(articles_urls)) + '篇文章...')
            f.write(content)

PAGE = visit_page('http://laotiese.org/txtsex/index.html')
ARTICLE_URLS = get_article_urls(PAGE)
get_article(ARTICLE_URLS)
