from requests import get
from bs4 import BeautifulSoup
import os
import shutil
import img2pdf
import sys
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

options = Options()
options.headless = True
options.add_argument("window-size=400,600")

driver = webdriver.Firefox(options=options) #

#url_ = "https://www.porncomix.info/dna-2-jabcomix/"
url_ = sys.argv[1]

driver.get(url_)
sleep(3)

r = {
    'content':''
}

content = driver.page_source

print(content)

#r = get(url_)

title = url_.split('/')[len(url_.split('/')) - 4] + '_' + url_.split('/')[len(url_.split('/')) - 3] + '_' + url_.split('/')[len(url_.split('/')) - 2]
#title = sys.argv[2]

print(title)

directory = os.getcwd() + '/' + title + '/'

try:
    os.mkdir(directory)
except:
    print()

print(content)

html = BeautifulSoup(content,"html.parser")

count = 0

img_arr = []

for img_page in html.find_all("span", class_="single-comic-page"):
    print(img_page)
    img = img_page.find_all("img")[0]
    count = count + 1
    print(img.attrs['src'])
    
    if count < 10:
        count_str = "0" + str(count)
    else:
        count_str = str(count)
            
    c = get(img.attrs['src'])
        
    img_arr.append(directory + title + (count_str) + ".jpg")
        
    with open( directory + title + (count_str) + ".jpg", 'wb') as f:
        f.write(c.content)
        print(title + (count_str))
            
print(img_arr)


with open("Comix/" + title + ".pdf", "wb") as f:
    f.write(img2pdf.convert([i for i in img_arr if i.endswith(".jpg")]))

