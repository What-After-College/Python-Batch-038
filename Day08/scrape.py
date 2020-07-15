import requests
import bs4

url = "https://github.com/requests/requests"

response = requests.get(url)
# print(response)
# print(response.text)

web_page = bs4.BeautifulSoup(response.text, "lxml")
# print(web_page)

# print(web_page.head)

# print(web_page.head.title.text)


sub_web_page = web_page.find_all(name="ul")
print(sub_web_page)