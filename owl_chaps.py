from requests import get
from bs4 import BeautifulSoup
import os
import shutil
import sys

def get_chaps(url):

    print(url)
    r = get(url)

    html = BeautifulSoup(r.content, "html.parser")

    chaps = html.findAll('a', class_="chapter-url")

    chapters = []
    for chap in chaps:
        chap_url = chap.attrs["href"]
        chap_title = chap.find("label").text.strip()
        chapter = {
            "value": chap_url,
            "label": chap_title
        }
        chapters.append(chapter)

    return (chapters)

#_url = "https://manga-owl.com/single/182/shingeki-no-kyojin"
#get_chaps(_url)