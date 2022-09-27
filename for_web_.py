from bs4 import BeautifulSoup
from requests import get 

url = "https://www.google.com/search?q=10+day+forecast+for+youngstown+ohio"
response = get(url)
# print(response.text[:501])

soup = BeautifulSoup(response.text, 'html.parser')
# print(type(soup))
# print(soup)
temps = soup.findAll('class'== 'gNCp2e', 'class' == 'gNCp2e')
# teachers = soup.find_all('tr')
print(temps)
for item in temps:
    print(item.text[:50])