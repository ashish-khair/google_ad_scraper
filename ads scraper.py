import requests
from bs4 import BeautifulSoup
from selenium import webdriver

header = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}
query = input("Enter a search query: ")
url = f"https://www.google.com/search?q={query}"
response = requests.get(url,headers = header)
chrome_driver_path = 'C:\Development\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')
product_details = soup.find_all('a',{'class':"plantl pla-unit-single-clickable-target clickable-card"})

all_image = soup.find_all('div',{"class":"Gor6zc"})

image_link = []
for i in range(len(all_image)):
    try:
        im = all_image[i].find('img')['src']
        image_link.append(im)
    except:
        continue
ads_details = {}
for i in range(len(product_details)):
    ads_details[i] = {
        "Product title":product_details[i]["aria-label"],
        "purchase line":product_details[i]["href"],
        "product image":image_link[i]
    }

print(ads_details)
driver.quit()