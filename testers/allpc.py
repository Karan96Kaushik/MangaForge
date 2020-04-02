from requests import get
from bs4 import BeautifulSoup
import os
import shutil
import img2pdf
import sys
from PIL import Image

ext = '.gif'

#url_ = "https://www.porncomix.info/dna-2-jabcomix/"
url_ = sys.argv[1]
r = get(url_)
title = sys.argv[2]

directory = os.getcwd() + '/' + title + '/'

try:
    os.mkdir(directory)
except:
    print()

html = BeautifulSoup(r.content, "html.parser")

count = 0

img_arr = []

for img_page in html.find_all("div", class_="page-break"):
    # print(img_page)
    count = count + 1
    img_link = img_page.find_all("img")[0].attrs['src']
    print(img_link)

    if count < 10:
        count_str = "0" + str(count)
    else:
        count_str = str(count)

    c = get(img_link)

    with open(directory + title + (count_str) + ext, 'wb') as f:
        f.write(c.content)
        print(title + (count_str))
    
    Image.open(directory + title + (count_str) + ext).convert('RGB').save(directory + title + (count_str) + '.jpg')
    img_arr.append(directory + title + (count_str) + '.jpg')

print(img_arr)


with open("Comix/" + title + ".pdf", "wb") as f:
    f.write(img2pdf.convert([i for i in img_arr if i.endswith('.jpg')]))
