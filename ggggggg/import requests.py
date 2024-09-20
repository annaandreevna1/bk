import requests 
import csv
from bs4 import BeautifulSoup

class Worker :
    def __init__(self, name, post, date):
        self.name = name
        self.post = post
        self.date = date

workers = []

url = 'https://museum.anosov.ru/index.php?option=com_content&view=category&layout=blog&id=71&Itemid=116'
response = requests.get(url)
print(response.content)
soup = BeautifulSoup(response.text, 'lxml')
names = soup.find_all("strong")
for n in names:
    workers.append(Worker(n.get_text(), "", ""))

file = open("hh.csv","w", encoding="utf-8")


for worker in workers:
    print(worker)
    file.write(worker.name + "\n")