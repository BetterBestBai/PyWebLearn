
import requests
import bs4
response = requests.get('http://wufazhuce.com/one/1295')
soup = bs4.BeautifulSoup(response.text,"html.parser")
print soup
print type(response)