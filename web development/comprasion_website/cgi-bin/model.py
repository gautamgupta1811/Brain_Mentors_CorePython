import bs4
import urllib.request as url

def data_reterival(product):
    path = "https://www.flipkart.com/search?q=".format("%20".join(product.split()))
    http = url.urlopen(path)
    page = bs4.BeautifulSoup(http, features="lxml")
    print(page.find("a", class_="s1Q9rs"))
    if page.find("a", class_="s1Q9rs"):
        print("card format")
    elif page.find("div",class_="_4rR01T"):
        print("list format")

data_reterival("realme 3")