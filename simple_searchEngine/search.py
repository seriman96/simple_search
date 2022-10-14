# from urllib import request
from bs4 import BeautifulSoup
from requests import get
import urllib.request
import pymongo as pm
import pandas as pd
###########
myclient = pm.MongoClient("mongodb://127.0.0.1:27017/")

db = myclient["Myengine"]
colect = db["User"]
lst = colect.find({},{"_id":0})
dt = pd.DataFrame(list(lst))


def search(term, num_results=5, lang="en"):
    usr_agent = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/61.0.3163.100 Safari/537.36'}

    def fetch_results(search_term, number_results, language_code):
        escaped_search_term = search_term.replace(' ', '+')

        google_url = 'https://www.google.com/search?q={}&num={}&hl={}'.format(escaped_search_term, number_results+1,
                                                                              language_code)
        response = get(google_url, headers=usr_agent)
        response.raise_for_status()

        # soup = BeautifulSoup(response, 'html.parser') # , from_encoding=response.info().get_param('charset')

        return response.text
        # return soup

    '''
    html = fetch_results(term, num_results, lang)
    return parse_results(html)'''

    def parse_results(raw_html):
        soup = BeautifulSoup(raw_html, 'html.parser') 
        result_block = soup.find_all('div', attrs={'class': 'g'})
        meta = soup.find_all('div', attrs={'class': 'VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf'})
        ls = []
        des_mt = []
        tl = []
        for result,mt in zip(result_block,meta):
            link = result.find('a', href=True)
            title = result.find('h3')
            met_des = mt.find('span')
            if link and title and met_des:
                # yield link['href']
                ls.append(link['href'])
                des_mt.append(met_des.get_text())
                tl.append(title.get_text())
        ls.pop(-1)
        return zip(ls,des_mt,tl)
    html = fetch_results(term, num_results, lang)

    return list(parse_results(html))
        
'''to come back
    html = fetch_results(term, num_results, lang)

    ls1 = []
    ls = list(parse_results(html))
    ls.pop(-1)
    for i in ls:
        page = urllib.request.urlopen(i)
        sp = BeautifulSoup(page,'html.parser') 
        for tgs in sp.find_all('meta'):
            ls1.append(tgs.get('content'))
        # lst.extend(ls1)
            if len(ls1)>=1:
                break

    return list(zip(ls,ls1))    '''


'''def meta_content(google_url): # search_term, language_code="en"
    number_results=9
    escaped_search_term = search_term.replace(' ', '+')

    # google_url = 'https://www.google.com/search?q={}&num={}&hl={}'.format(escaped_search_term, number_results+1,language_code)
    page = urllib.request.urlopen(google_url)
    html = BeautifulSoup(page.read(),"html.parser")
    ls = []
    for tgs in html.find_all('meta'):
        ls.append(tgs.get('content'))
    return ls'''
                                                
# print(meta_content('https://www.google.com/search?fr=mcafee&type=E211US885G0&p=python'))

'''
https://www.python.org/
https://www.python.org/
https://en.wikipedia.org/wiki/Python_(programming_language)
https://www.w3schools.com/python/
https://www.tutorialspoint.com/python/index.htm
https://www.programiz.com/python-programming/online-compiler/
https://www.codecademy.com/catalog/language/python
https://www.codecademy.com/catalog/language/python
'''
'''ls = ['https://www.python.org/','https://www.python.org/','https://en.wikipedia.org/wiki/Python_(programming_language)']
ls1 = []
ls2 = []
lst = []
for i in ls:
    page = urllib.request.urlopen(i)
    sp = BeautifulSoup(page,'html.parser') 
    for tgs in sp.find_all('meta'):
        ls1.append(tgs.get('content'))
    # lst.extend(ls1)
        if len(ls1)>=1:
            break'''
# for lt in ls1:
    # ls2.append(lt)
# print(ls1)
#    print('\n')
#for j in ls2:
#    print(j)
'''for (lk,cnt) in zip(ls,ls1):
    print(lk)
    print(cnt)
    print("\n\n")'''
'''for k in ls1:
    print(k)
    print('\n\n\n')'''
'''def a():
    ls =[1,2,3]
    ls1 =[4,5,6]
    #t =()
    # r = (ls,ls1)
    # for i,j in zip(ls,ls1):
        # t += (i,j)
    # return list(zip(ls,ls1))'''


'''b = a()
# i,j=0,0
k = len(b)
o=2'''
'''for i in range(k):
    for j in range(o):
        print(b[i][j])

d=[1,2,3]
f=[5,6,9]
for i in d:
    for j in f:
    # p = list(i)
        if j !=f[0]:
            break
        else:
            print(i,j)
    # if p.pop(-1):
            # print(p)#,[i+1][j] [i][j]
        # print()
    # print() 
    
    {% if j != mdes[0] %}
                    {% break %}
                {% else %}
    '''


