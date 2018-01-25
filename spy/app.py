from bs4 import BeautifulSoup
import requests
import os
import json

headers = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
}

def login():
  data = {
    'account': 'liujun',
    'password': 'Password1',
    'keepLogin[]': 'on',
    'referer': 'http://pj.mucfc.com/zentao/my-task.html'
  }
  r = requests.post('http://pj.mucfc.com/zentao/user-login.html', headers = headers, data = data)
  return r.cookies.get_dict()

def visitPage(url):
  r = requests.get(url, headers = headers, cookies = login())
  r.encoding = 'utf-8'
  soup = BeautifulSoup(r.text, 'lxml')
  return soup

def getTasks():
  tasks_list = []
  css_selector_1 = '#tasktable > tbody > tr > td:nth-of-type(4) > a'
  css_selector_2 = '#wrap > div.outer > div.row-table > div.col-side > div > fieldset:nth-of-type(2) > table td:nth-of-type(3)'
  css_selector_3 = '#wrap > div.outer > div.row-table > div.col-side > div > fieldset:nth-of-type(1) > table td:nth-of-type(1) a'

  tasks = visitPage('http://pj.mucfc.com/zentao/my-task.html').select(css_selector_1)

  for task in tasks:
    task_link = task.get('href')
    task_info = visitPage('http://pj.mucfc.com' + task_link)
    data = {
      '任务名称': task.get_text(),
      '禅道链接': 'http://pj.mucfc.com' + task_link,
      '所属项目': 'http://pj.mucfc.com' + task_info.select(css_selector_3)[0].get('href'),
      '结束时间': task_info.select(css_selector_2)[0].get_text().strip()
    }
    
    tasks_list.append(data)
  
  return tasks_list

def notify(title, text, subtitle):
  os.system("""
    osascript -e 'display notification "{}" with title "{}" subtitle "{}"'
  """.format(text, title, subtitle))

# notify('Hello', 'world', 'everyone')

print(getTasks())
