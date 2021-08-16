import urllib.request
from bs4 import BeautifulSoup

url ="https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%BD%94%EB%A1%9C%EB%82%9819"
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,'html.parser')

title=soup.find_all(class_='info_title',)
num=soup.find_all(class_='info_num')

l_title=[]
l_num=[]

for i in title:
    if i.string!=None:
        l_title.append(i.string)



for j in num:
    l_num.append(j.string)


for k in range(len(l_title)):
    print(l_title[k]+" : "+l_num[k])




