import requests
import bs4
import os

kv = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}

url = 'https://www.baidu.com/s?wd=%E7%94%B0%E9%B9%8F%E5%AE%87&rsv_spt=1&rsv_iqid=0xf7219b010003c755&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_dl=ib&rsv_sug3=11&rsv_sug1=7&rsv_sug7=100'

titles_urls = []

response = requests.get(url,headers = kv)
status_code = response.status_code

content = bs4.BeautifulSoup(response.content.decode("utf-8"), "lxml")

for i in range(1,11):
    element = content.find_all(id=i)
    for per in element:

       # psrc = per.find_all(name='div',attrs={"class":"c-tools"})
        psrc = per.find_all(class_='c-tools')

        for a in psrc:
            b = str(a)

            d = b.find('{')
            c = b.find('}')
            title_url = b[d:c+1]
        #    print(title_url)
            titles_urls.append(title_url)

print(status_code)
# print(element)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print(titles_urls)
