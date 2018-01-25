from bs4 import BeautifulSoup
import requests
import json

def getPage (url):
  headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
  }
  web_data = requests.get(url, headers = headers)
  Soup = BeautifulSoup(web_data.text, 'lxml')
  return Soup

def analyzeData (Soup):
  titles = Soup.select('a.title')
  authors = Soup.select('a.author')
  votes = Soup.select('div.score.unvoted')

  collect = []

  for title, author, vote in zip(titles, authors, votes):
    data = {
      'title': title.get_text(),
      'link': title.get('href'),
      'author': author.get_text(),
      'vote': vote.get_text()
    }

    collect.append(data)
  
  return collect

Soup = getPage('https://www.reddit.com/r/javascript/')
Data = analyzeData(Soup)

print(json.dumps(Data, indent = 2))

with open('./test.txt', 'w') as f:
  f.write(json.dumps(Data, indent = 2))
