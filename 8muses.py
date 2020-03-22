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

html = BeautifulSoup(r.content, "html.parser")

count = 0

img_arr = []

print(html)

for img_page in html.find_all("a", class_="c-tile t-hover"):
    count = count + 1
    #print(a.attrs['href'])
    b = get('http://8muses.com/' + img_page.attrs['href'])

    if count < 10:
        count_str = "0" + str(count)
    else:
        count_str = str(count)

    page_img = BeautifulSoup(b.content, "html.parser").find_all("img", class_="image")
    print(page_img)

    c = get('http://8muses.com/' + page_img)

    img_arr.append('/home/karan/Downloads/' + title +
                   '/' + title + (count_str) + ".jpg")

    with open('/home/karan/Downloads/' + title + '/' + title + (count_str) + ".jpg", 'wb') as f:
        f.write(c.content)
        print(title + (count_str))

print(img_arr)


with open("Comix/" + title + ".pdf", "wb") as f:
    f.write(img2pdf.convert([i for i in img_arr if i.endswith(".jpg")]))
