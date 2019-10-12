from bs4 import BeautifulSoup
import requests


page = requests.get('http://www.01xq.com/xqplayer/xqrating.asp',timeout=5)
soup = BeautifulSoup(page.content,'html.parser')

arr=[]
arr2=[]

#contents[2] is player name
#contents[4] is rating
#contents[5] is rank
# getting the countries;  arr.append(j.contents[3].get_text()) 

#Based on the parse tree structure for this web page, range limit should be 84 to retrieve the top 20 players in Chinese chesss 
for x in range(1,63):
    for i,j in enumerate(soup.find_all('tr')):
        if i==x:
            arr.append(j.contents[2].get_text())                        
            arr.append(j.contents[4].get_text())            
            arr.append(j.contents[5].get_text())
    
    arr2.append(arr[x])
    


# Removing unneeded information in the list.
# arr2.remove('Registration')
arr2.remove('Rating')
arr2.remove('Current Rank')


print(arr2)


