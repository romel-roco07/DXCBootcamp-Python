from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/p/pl?N=100157995%20601360966%20601328394%204814&cm_sp=Tab_Computer-Systems-_-Flyout-_-GeForce-RTX-Gaming-Laptops_4'
uclient = uReq(my_url)
page_html = uclient.read()
uclient.close()
page_soup = soup(page_html,"html.parser")
containers = page_soup.findAll("div",{"class":"item-container"})

# C:\Users\rroco\OneDrive - DXC Production\Desktop\DXC\Bootcamp\Python\Repo\source_file
filename = "C:\source_file\product1.csv"
f = open(filename, "w")
headers = "brand, shipping, price \n"
f.write(headers)

for container in containers:
    brand = container.a.img["title"]
    shipping_container = container.findAll('li',{"class":"price-ship"})
    shipping = shipping_container[0].text.strip()
    price_list = container.findAll('li',{"class":"price-current"})
    price = price_list[0].text.strip().replace("|","").replace("\r","").replace("\n","")
    print("brand: " + brand)
    print("shipping: " + shipping)
    print("price: " + price)
    print("_________________________________")

    f.write(brand.replace(",","|") + "," + shipping + "," + price.replace(",",".") + "\n") 

f.close()