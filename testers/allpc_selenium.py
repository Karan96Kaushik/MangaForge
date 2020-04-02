from requests import get
from bs4 import BeautifulSoup
import os
import shutil
import img2pdf
import sys
from PIL import Image
import tkinter as tk
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from IPython.core.display import display, HTML
from time import sleep
import thread

options = Options()
options.headless = False
options.add_argument("window-size=400,600")

driver = webdriver.Firefox(options=options)

driver.get('http://allporncomic.com')

def tk_bt():
    r = tk.Tk() 
    r.title('Download') 
    button = tk.Button(r, text='Go!', width=20, height=10, command=sel) 
    button.pack() 
    r.mainloop() 

def sel():
    #dl(driver.current_url)
    thread.start_new_thread(dl, driver.current_url)
    return

def dl(url):
    ext = '.gif'

    url_ = url
    r = get(url_)

    

    html = BeautifulSoup(r.content, "html.parser")

    count = 0

    img_arr = []

    try:
        title = html.find_all("h1", id="chapter-heading")[0].text
        print(title)
    except:

    directory = os.getcwd() + '/' + title + '/'

    try:
        os.mkdir(directory)
    except:
        print()

    for img_page in html.find_all("div", class_="page-break"):
        # print(img_page)
        count = count + 1
        img_link = img_page.find_all("img")[0].attrs['src']
        #print(img_link)

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

    #print(img_arr)

    try:
        with open("Comix/" + title + ".pdf", "wb") as f:
            f.write(img2pdf.convert([i for i in img_arr if i.endswith('.jpg')]))
    except:
        print()

    print('PDF Generated ' + title)
    shutil.rmtree(directory)

tk_bt()