from urllib.request import urlopen
from bs4 import BeautifulSoup




def title():
    for i in range(88756572,88756585):
        url = "https://finance.naver.com/item/board_read.nhn?code=000660&nid="+str(i)+"&st=&sw=&page=1"
        html = urlopen(url).read().decode( 'cp949' , 'ignore' )
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find_all('strong',{"class":"c p15"})
        body = soup.find_all('div',{"class":"view_se"})
        if len(title)!=0:
            if title[0].get_text():
                ab.insert(i, title[0].get_text())
                bcnt.insert(i, body[0].get_text())
                
            

    

ab = []
bcnt = []
title()
ab.sort(reverse=True)
bcnt.sort(reverse=True)
for j in range(0,9):
    print("제목 : ",ab[j])
    print('\n')
    print("글 내용 : ",bcnt[j])
    print('\n')
