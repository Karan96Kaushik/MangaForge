from requests import get
from pyquery import PyQuery
from lxml.html import parse
from html.parser import HTMLParser
from bs4 import BeautifulSoup
from fpdf import FPDF
import os
import img2pdf
from flask import Flask, request, jsonify, json, abort
from flask_cors import CORS, cross_origin
import sys


#url_ = "https://www.porncomix.info/dna-2-jabcomix/"
url_ = sys.argv[1]
r = get(url_)
title = sys.argv[2]

directory = '/home/karan/Downloads/' + title + '/'
os.mkdir(directory)

html = BeautifulSoup(r.content,"html.parser")

count = 0

img_arr = []

for img_page in html.find_all("dt", class_="gallery-icon portrait"):
    #print(img_page)    
    for a in img_page.find_all("a", href=True):
        count = count + 1
        #print(a.attrs['href'])
        b = get(a.attrs['href'])
        
        if count < 10:
            count_str = "0" + str(count)
        else:
            count_str = str(count)
        
        page_img = BeautifulSoup(b.content,"html.parser").find_all("div", class_="attachment-image")[0].find_all("a", href=True)[0].attrs['href']
        
        c = get(page_img)
        
        img_arr.append('/home/karan/Downloads/' + title + '/' + title + (count_str) + ".jpg")
        
        with open('/home/karan/Downloads/' + title + '/' + title + (count_str) + ".jpg", 'wb') as f:
            f.write(c.content)
            print(title + (count_str))
            
print(img_arr)


with open("Comix/" + title + ".pdf", "wb") as f:
    f.write(img2pdf.convert([i for i in img_arr if i.endswith(".jpg")]))
