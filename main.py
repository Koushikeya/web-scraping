from bs4 import BeautifulSoup
import requests

html_response = requests.get('https://books.toscrape.com/')
print(html_response)

booksApp = BeautifulSoup(html_response.text, 'lxml')



books = booksApp.find_all('li', class_ ='col-xs-6 col-sm-4 col-md-3 col-lg-3')
print(books)

# flow of sequence li>article>h3 (accessing title attribute of h3)

for book in books:
    article = book.find("article", class_ = "product_pod")

    h3 = article.find("h3")

    og = h3.a["title"]

    print(og)

