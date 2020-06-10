from requests import get
from bs4 import BeautifulSoup
import os
import shutil
import img2pdf
import sys
from vidDL2 import vidDownloader as vid

url_ = sys.argv[1]
folder = sys.argv[2]

directory = os.getcwd() + '/Comix/' + folder + '/'

try:
    os.mkdir(directory)
except:
    print()

def get_vid(url):
    print("Starting download from", url + "...")
    r = get(url)

    html = BeautifulSoup(r.content, "html.parser")

    title = html.find("title").text.strip().split("Watch ")[1]
    frame = html.find_all("iframe")[0].attrs["src"]

    # print("Got Frame", frame)
    if frame.find("https") == -1:
        frame = "https:" + frame
    
    r = get(frame).content.decode()

    print("Finding video link...")

    vid_src_start = r.find("sources:[{file: '") + 17
    vid_src_end = r.find("',label: 'HD P','type' : 'mp4'}]")

    vid_src = r[vid_src_start: vid_src_end]
    # print(">" + vid_src + "<")

    # print()

    # return
    # next_link = ''

    # for x in html.find_all("a", class_='anchored_item', title=True):
    #     if(x.text == 'Next'):
    #         next_link = x.attrs['href']
    
    # print()
    # print(title)

    try:
        vid(vid_src, title, directory)
    except():
        print('Err')
    # page(next_link)

# page(url_)

eps_array = []

def eps(url):
    print(url)
    print("Finding eps...")
    r = get(url)

    html = BeautifulSoup(r.content, "html.parser")

    ep_list = html.find("ul", id="episode_related")
    eps = ep_list.find_all("li")

    global eps_array

    for ep in eps:
        link = "https://gogoanimetv.io" + ep.find("a").attrs["href"].strip()
        eps_array.append(link)
        print(" ".join(ep.text.split()), link)
        # get_vid(link)

    for i, ep in enumerate(eps_array):
        print(i, " : ", ep)
    
    selected_ep = int(input("Select ep index:"))

    get_vid(eps_array[selected_ep])

# page(url_)

eps(url_)