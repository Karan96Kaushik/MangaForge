from requests import get
from bs4 import BeautifulSoup
import os
import shutil
import img2pdf
import sys
from vidDL import vidDownloader as vid

def page(url, folder):
    directory = os.getcwd() + '/Comix/' + folder + '/'

    try:
        os.mkdir(directory)
    except:
        print()

    r = get(url)

    html = BeautifulSoup(r.content, "html.parser")

    title = html.find("title").text.split(' - XNXX.COM')[0]
    #print(html)
    vid_link_script = str(html.find("div",id="video-player-bg").find_all("script")[4])
    # print(vid_link_script)
    # print(len("setVideoUrlHigh('"))
    link_index1 = vid_link_script.find("setVideoUrlHigh('")
    link_index2 = vid_link_script.find("')", link_index1)

    print(link_index1,link_index2)
    vid_link = (vid_link_script[link_index1 + 17:link_index2])
    print(vid_link)
    #next_link = ''

    #next_link = 'https://xnxx.com' + html.find("div", class_='mozaique').find("a").attrs['href']
    
    print()
    print(title)

    try:
        vid(vid_link, title, directory)
    except():
        print('Err')
    #page(next_link)

#page(url_)