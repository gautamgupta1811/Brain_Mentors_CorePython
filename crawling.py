import bs4
import urllib.request as url

search = input("Enter Product: ")
search = "+".join(search.split())
path = "https://www.flipkart.com/search?q={}".format(search)
print(path)

# path_1 = "https://www.google.com/search?q=coding&sxsrf=APq-WBu3eAMDGw1ttxtHZAKY0EuO75prSg%3A1648389131739&source=hp&ei=C2xAYs2BK433-Qb50IaIBQ&iflsig=AHkkrS4AAAAAYkB6G-IL8nrKXawh2YEOTi2l4VC3wvhj&ved=0ahUKEwiNs5aFuOb2AhWNe94KHXmoAVEQ4dUDCAc&uact=5&oq=coding&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyCAgAEIAEELEDMggIABCABBCxAzILCAAQgAQQsQMQgwEyCAgAEIAEELEDMgUIABCABDIICAAQgAQQyQMyBQgAEJIDMgUIABCABDIFCAAQgAQ6CAgAELEDEIMBOggILhCxAxCDAToECAAQQzoKCAAQsQMQgwEQQzoOCC4QgAQQsQMQgwEQ1AJQAFibBWCdBmgAcAB4AIABuAGIAZwGkgEDMC41mAEAoAEB&sclient=gws-wiz"
http = url.urlopen(path)

page = bs4.BeautifulSoup(http)

name = page.find_all("div", class_="_4rR01T")
price = page.find_all("div", class_="_1_WHN1")
for element, p in zip(name, price):
    print(element.text, p.text)
