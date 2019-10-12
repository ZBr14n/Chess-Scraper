from bs4 import BeautifulSoup
import requests



page = requests.get('https://en.wikipedia.org/wiki/FIDE_world_rankings',timeout=5)
soup = BeautifulSoup(page.content,'html.parser')


# Based on how the parse tree is structured for this wiki page:
# contents[1] to get the ranks.
# contents[5] to get the names.
# contents[7] to get the ratings.
#limit=21 gets the top 20 players in the wiki page.

storeInfo = []
for row in soup.find_all('tr',limit=21):
    storeInfo.append(row.contents[1].get_text().replace("\n",""))
    storeInfo.append(row.contents[5].get_text().replace("\n","").strip())
    storeInfo.append(row.contents[7].get_text().replace("\n",""))


#remove the first three elements that are not needed in the list (unneccesary info)
storeInfo.pop(0)
storeInfo.pop(0)
storeInfo.pop(0)


print(storeInfo)

