import bs4
import urllib.request as url

def data_reterival(product):
    path = "https://www.flipkart.com/search?q={}".format("+".join(product.split()))
    print(path)
    http = url.urlopen(path)
    page = bs4.BeautifulSoup(http, features="lxml")
    if page.find("div",class_="_4rR01T"):
        name = page.find('div', class_="_4rR01T").text
        price = page.find('div', class_="_1_WHN1").text
        ul = page.find('ul', class_="_1xgFaf")
        li_tag = ul.find_all("li", class_="rgWa7D")
        li_data = []
        for li in li_tag:
            li_data.append(li.text)
        return name, price[1:], li_data
        
    elif page.find("a", class_="s1Q9rs"):
        a = page.find("a", class_="s1Q9rs")
        link = "https://www.flipkart.com" + a["href"]
        # to be completed by Mehak
data_reterival("apple x")