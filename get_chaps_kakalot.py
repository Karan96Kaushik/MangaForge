from requests import get
from bs4 import BeautifulSoup
import os
import shutil
import img2pdf
import sys
from PIL import Image
import urllib.parse
import global_vars
from datetime import datetime
from m_kakalot import dl

def parseChaps(url_):
    r = get(url_)

    html = BeautifulSoup(r.content,"html.parser")

    allRows = html.find(class_="row-content-chapter")
    allRows = allRows.find_all("li")

    for i, row in enumerate(allRows):
        chap = row.find("a")
        # print(str(i) + " " + chap.attrs["href"])

        if(i > 77 and i < 89):
            dl(chap.attrs["href"])
            
        continue
    

parseChaps('https://readmanganato.com/manga-vy951833')