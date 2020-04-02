from requests import get
from bs4 import BeautifulSoup
import os
import shutil
import img2pdf
import sys
import io
from PIL import Image
import tkinter as tk
from time import sleep
import _thread
import urllib.request

r = tk.Tk() 

def tk_bt():
    r.title('Download') 
    button = tk.Button(r, text='Go!', width=20, height=10, command=sel) 
    button.pack() 
    r.mainloop() 

def sel():
    #dl(driver.current_url)
    print(r.clipboard_get().split('.com')[0])
    if r.clipboard_get().split('.com')[0] == 'https://allporncomic':
        _thread.start_new_thread(dl_allporncomics, (r.clipboard_get(), ))
        pass
    elif r.clipboard_get().split('.com')[0] == 'https://sexporncomics':
        _thread.start_new_thread(dl_sexporncomics, (r.clipboard_get(), ))
        pass
    elif r.clipboard_get().split('.info')[0] == 'https://www.porncomix':
        _thread.start_new_thread(dl_porncomix, (r.clipboard_get(), ))
        pass
    elif r.clipboard_get().split('.org')[0] == 'https://hentaihaven':
        _thread.start_new_thread(dl_haven, (r.clipboard_get(), ))
        pass
    return

def dl_allporncomics(url):
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
        print()

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

def dl_sexporncomics(url):
    ext = '.gif'

    url_ = url
    r = get(url_)

    html = BeautifulSoup(r.content, "html.parser")

    count = 0

    img_arr = []

    try:
        title = html.find_all("title")[0].text
        print(title)
    except:
        print()

    directory = os.getcwd() + '/' + title + '/'

    try:
        os.mkdir(directory)
    except:
        print()

    for img_page in html.find_all("div", class_="king-q-view-content")[0].find_all("img"):
        # print(img_page)
        count = count + 1
        img_link = img_page.attrs['src']
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

def dl_porncomix(url):
    ext = '.gif'

    url_ = url
    r = get(url_)

    html = BeautifulSoup(r.content, "html.parser")

    count = 0

    img_arr = []

    try:
        title = html.find_all("title")[0].text
        print(title)
    except:
        print()

    directory = os.getcwd() + '/' + title + '/'

    try:
        os.mkdir(directory)
    except:
        print()

    for img_page in html.find_all("dt", class_="gallery-icon"):
        #print(img_page)    
        for a in img_page.find_all("a", href=True):
            count = count + 1
            #print(a.attrs['href'])
            b = get(a.attrs['href'])
            
            if count < 10:
                count_str = "0" + str(count)
            else:
                count_str = str(count)
            
            img_link = BeautifulSoup(b.content,"html.parser").find_all("div", class_="attachment-image")[0].find_all("a", href=True)[0].attrs['href']
            
            c = get(img_link)

            with open(directory + title + (count_str) + ext, 'wb') as f:
                f.write(c.content)
                print(title + (count_str))
            
            Image.open(directory + title + (count_str) + ext).convert('RGB').save(directory + title + (count_str) + '.jpg')
            img_arr.append(directory + title + (count_str) + '.jpg')
                
    print(img_arr)


    with open("Comix/" + title + ".pdf", "wb") as f:
        f.write(img2pdf.convert([i for i in img_arr if i.endswith(".jpg")]))
    
    print('PDF Generated ' + title)
    shutil.rmtree(directory)

def dl_haven(url): ## Not Working
    url_ = url
    r = get(url_)

    html = BeautifulSoup(r.content, "html.parser")

    try:
        title = html.find_all("title")[0].text
        print(title)
    except:
        print()

    for img_page in html.find_all("video"):
        c = video_download(img_page.find_all("source")[0].attrs['src'])

        with open("Comix/" + title + ".mp4", 'wb') as f:
            f.write(c)
            print(title)
            
    print('Video Saved ' + title)

def video_download(url):
    resp = urllib.request.urlopen(url)
    length = resp.getheader('content-length')
    if length:
        length = int(length)
        blocksize = max(4096, length//100)
    else:
        blocksize = 1000000 # just made something up

    print(length, blocksize)

    video = io.BytesIO()
    size = 0
    with open("Comix/" + 'title' + ".mp4", 'wb') as f:
        while True:
            vid_buf = resp.read(blocksize)
            if not vid_buf:
                break
            video.write(vid_buf)
            size += len(vid_buf)
            if length:
                print('\r{:.2f} % Done  '.format(size*100/length), end='')
                f.write(vid_buf)
    
    return video.getbuffer()


tk_bt()