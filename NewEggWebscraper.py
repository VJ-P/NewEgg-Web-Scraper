import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.ca/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=7708'

#opening the connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")

#grab each product
containers = page_soup.findAll("div",{"class":"item-container"})

#open an excel file to store the information
filename = "NeweggProduct.csv"
f = open(filename, "w")

headers = "brand, productName, price, shipping\n"
f.write(headers)

for container in containers:
    brand_name = container.find("a", {"class":"item-brand"}).img["title"]       #extracts the brand name of the product
    product_name = container.find("a", {"class":"item-title"}).text             #extracts the name of the product
    product_price = container.find("li", {"class":"price-current"}).strong.text #extracts the price of the product
    shipping_price = container.find("li", {"class":"price-ship"}).text.strip()  #extracts the shipping price of the product

    print("brand_name: " + brand_name)
    print("product_name: " + product_name)
    print("product_price: " + product_price)
    print("shipping_price: " + shipping_price + "\n")

    f.write(brand_name + "," + product_name.replace(",", "|" ) + "," + product_price.replace(",", "") + "," + shipping_price + "\n")
