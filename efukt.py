from requests import get
from bs4 import BeautifulSoup
import os
import shutil
import img2pdf
import sys
from vidDL import vidDownloader as vid

url_ = sys.argv[1]
folder = sys.argv[2]

directory = os.getcwd() + '/Comix/' + folder + '/'

try:
    os.mkdir(directory)
except:
    print()

def page(url):
    r = get(url)

    html = BeautifulSoup(r.content, "html.parser")

    title = html.find_all("title")[0].text.split(' |')[0]
    vid_link = html.find_all("video")[0].find_all("source")[0].attrs['src']
    next_link = ''

    for x in html.find_all("a", class_='anchored_item', title=True):
        if(x.text == 'Next'):
            next_link = x.attrs['href']
    
    print()
    print(title)

    try:
        vid(vid_link, title, directory)
    except():
        print('Err')
    page(next_link)

page(url_)