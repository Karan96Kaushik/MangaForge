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
import urllib.request

url_link = ('http://hh.cx/files/72/[HH]direct_PID5430[SD].mp4')
title = "xa"

urllib.request.urlretrieve(url_link, title) 

print('Saved')

with open("Comix/" + title + ".mp4", 'wb') as f:
    f.write(c.content)
    print(title)