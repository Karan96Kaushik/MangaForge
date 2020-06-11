from requests import get, post
from bs4 import BeautifulSoup
import os
import shutil
import img2pdf
import sys
from vidDL2 import vidDownloader as vid

# url_ = sys.argv[1]
# folder = sys.argv[2]

# directory = os.getcwd() + '/Comix/' + folder + '/'

# try:
#     os.mkdir(directory)
# except:
#     print()

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

def get_vid_link(url):
    print("Starting download from", url + "...")
    r = get(url)

    html = BeautifulSoup(r.content, "html.parser")

    title = html.find("title").text.strip().split("Watch ")[1].split("at gogoanime")[0]
    frame = html.find_all("iframe")[0].attrs["src"]

    # print("Got Frame", frame)
    if frame.find("https") == -1:
        frame = "https:" + frame
    
    r = get(frame).content.decode()

    print("Finding video link...")

    vid_src_start = r.find("sources:[{file: '") + 17
    vid_src_end = r.find("',label: 'HD P','type' : 'mp4'}]")

    vid_src = r[vid_src_start: vid_src_end]

    return {
        "name": title,
        "link": vid_src
        }


# page(url_)

# eps_array = []

def eps(url):
    print(url)
    print("Finding eps...")
    r = get(url)

    html = BeautifulSoup(r.content, "html.parser")

    ep_list = html.find("ul", id="episode_related")
    eps = ep_list.find_all("li")

    eps_array = []
    # global eps_array

    for ep in eps:
        link = "https://gogoanimetv.io" + ep.find("a").attrs["href"].strip()
        name = " ".join(ep.text.split())

        eps_array.append({
            "value":link,
            "label":name 
            })

    return eps_array
        # print(, link)
        # get_vid(link)

    # for i, ep in enumerate(eps_array):
    #     print(i, " : ", ep)
    
    # selected_ep = int(input("Select ep index:"))

    # get_vid(eps_array[selected_ep])

    # page(url_)    

def gogo_search(search_string):
    print(search_string)
    print("Finding shows...")
    
    headers = {
        'User-Agent': 'Mozilla/5.0',
        "content-type": "application/x-www-form-urlencoded"
    }
    r = post("https://gogoanimetv.io/ajax/ajax.php",data={"query" : search_string}, headers=headers)

    html = BeautifulSoup(r.content, "html.parser")
    # print(html)
    
    els = html.find_all("a")

    list_array = []
    # global eps_array

    for ep in els:
        link = "https://gogoanimetv.io" + ep.attrs["href"].strip()
        name = " ".join(ep.text.split())
        list_array.append({
            "label": name,
            "value": link
        })

    return list_array

# eps(url_)
# print(gogo_search("hunter x hunter"))