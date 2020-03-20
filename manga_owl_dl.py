from requests import get
from bs4 import BeautifulSoup
import os
import shutil
import img2pdf
import sys

#url_ = "https://www.porncomix.info/dna-2-jabcomix/"
url_ = sys.argv[1]
r = get(url_)
title = sys.argv[2]

directory = os.getcwd() + '/' + title + '/'

os.mkdir(directory)

html = BeautifulSoup(r.content,"html.parser")

count = 0

img_arr = []

for img_page in html.find_all("img", class_="owl-lazy"):
    #print(img_page)
    count = count + 1
    print(img_page.attrs['data-src'])
    
    if count < 10:
        count_str = "0" + str(count)
    else:
        count_str = str(count)
            
    c = get(img_page.attrs['data-src'])
        
    img_arr.append(directory + title + (count_str) + ".jpg")
        
    with open( directory + title + (count_str) + ".jpg", 'wb') as f:
        f.write(c.content)
        print(title + (count_str))
            
print(img_arr)


with open("Comix/" + title + ".pdf", "wb") as f:
    f.write(img2pdf.convert([i for i in img_arr if i.endswith(".jpg")]))

