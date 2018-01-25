from bs4 import BeautifulSoup

with open('./index.html') as web_data:
  Soup = BeautifulSoup(web_data, 'lxml')
  titles = Soup.select('section > h1')
  contents = Soup.select('section > p')

collect = []

for title, content in zip(titles, contents):
  data = {
    'title': title.get_text(),
    'content': content.get_text()
  }

  collect.append(data)

print(collect)