from PIL import Image
from requests import get
from bs4 import BeautifulSoup
from time import sleep
from flask import Flask, request, jsonify, json, abort, redirect, send_file
from flask_cors import CORS, cross_origin
import os
import shutil
import img2pdf
import sys
import io
#import tkinter as tk
import _thread
import urllib.request
import pyperclip

vid_progress = {}
methods = ('GET', 'POST')
app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/down', methods=methods)
def hello_world():
    req = request.args
    sel(req.get('fname'))
    return redirect('/prog')

@app.route('/clip', methods=methods)
def hell():
    req = request.args
    sel('')
    return redirect('/prog')

@app.route('/vids', methods=methods)
def vids():
    return jsonify(vid_progress)

@app.route('/link', methods=methods)
def down_link():
    html = '''
        <head></head><body>
        
        <form action="/down" method="get">
        <input type="text" id="fname" name="fname"><br>
        <input type="submit" id="fname" name="fname" value="Go!"><br>
        </form>

        <form action="/clip" method="get">
        <input type="submit" id="fname" name="fname" value="Use Copied"><br>
        </form> 
        
        </body>
        '''
    return html

@app.route('/files', methods=methods)
def files():
    onlyfiles = [f for f in os.listdir('Comix/') if os.path.isfile( os.path.join('Comix/', f) )]
    html = "<head></head><body>"
    for file in onlyfiles:
        lnk = '<a href="/' + file + '">' + file + '</a><br>'
        html = html + lnk
    html = html + '</body>'
    return html

@app.route('/<path:path>', methods=['GET'])
def serve_file(path):
    print(path)
    return send_file('Comix/' + path)

@app.route('/prog', methods=['GET'])
def s():
    return send_file('if.html')
 

def sel(_url):
    #dl(driver.current_url)
    print('SEL', _url)
    url = ''
    if(_url == ''):
        url = pyperclip.paste()
    else:
        url = _url
    
    if url.split('.com')[0] == 'https://allporncomic':
        _thread.start_new_thread(dl_allporncomics, (url, ))
        pass
    elif url.split('.com')[0] == 'https://sexporncomics':
        _thread.start_new_thread(dl_sexporncomics, (url, ))
        pass
    elif url.split('.info')[0] == 'https://www.porncomix':
        _thread.start_new_thread(dl_porncomix, (url, ))
        pass
    elif url.split('.org')[0] == 'https://hentaihaven':
        _thread.start_new_thread(dl_haven, (url, ))
        pass
    elif url.split('.com')[0] == 'https://www.aznude':
        _thread.start_new_thread(dl_az, (url, ))
        pass
    return

def dl_az(url):
    url_ = url
    r = get(url_)

    html = BeautifulSoup(r.content, "html.parser")
    name = html.find_all("title")[0].text
    directory = os.getcwd() + '/Comix/' + name + '/'
    try:
        os.mkdir(directory)
    except:
        print()

    count = 0
    for img_page in html.find_all("a", lightbox=True):
        clip_name = img_page.attrs['lightbox'].split('<small>')[0]

        count = count + 1

        try:
            print('http://cdn' + img_page.attrs['href'].split('//cdn')[1])
            b = get('http://cdn' + img_page.attrs['href'].split('//cdn')[1])
            ext  = img_page.attrs['href'].split('.')[len(img_page.attrs['href'].split('.')) - 1]

            with open(directory + clip_name + str(count) + '.' + ext, 'wb') as f:
                f.write(b.content)
                print(clip_name + str(count) + '.' + ext)
        except Exception as ex:
            print(ex)

    for vid_link in html.find_all("a", lightbox=True, class_="video"):
        count = count + 1
        clip_name = vid_link.attrs['lightbox'].split('<small>')[0]
        folder = directory + name + '/'

        b = get('https://www.aznude.com' + vid_link.attrs['href'])
        print(vid_link.attrs['href'])
        try:
            vid_url = BeautifulSoup(b.content,"html.parser").find_all("ul", class_="sorting-buttons")[0].find_all("a", href=True)[0].attrs['href']
            res = get('https:' + vid_url)
            with open(directory + clip_name + str(count) + ".mp4", 'wb') as f:
                f.write(res.content)
        except:
            a = 0

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

def dl_haven(url):
    url_ = url
    r = get(url_)

    html = BeautifulSoup(r.content, "html.parser")

    try:
        title = html.find_all("title")[0].text
        print(title)
    except:
        print()

    #print(html.find_all("video"))
    try:
        img_page = html.find_all("video")[0]

        try:
            c = video_download(img_page.find_all("source")[0].attrs['src'], title)
        except:
            c = video_download(img_page.find_all("source")[1].attrs['src'], title)

        print('Video Saved ' + title)
    except:
        try:
            img_page = html.find_all("video")[1]
            try:
                c = video_download(img_page.find_all("source")[0].attrs['src'], title)
            except:
                c = video_download(img_page.find_all("source")[1].attrs['src'], title)

            print('Video Saved ' + title)

        except:
            vid_progress[title] = 'Error'

def video_download(url, title):
    url = url.replace(' ', '%20')
    resp = urllib.request.urlopen(url)

    length = resp.getheader('content-length')
    if length:
        length = int(length)
        blocksize = max(4096, length//100)
    else:
        blocksize = 1000000 # just made something up

    vid_progress[title] = 0

    #print(length, blocksize)

    video = io.BytesIO()
    size = 0
    with open("Comix/" + title + ".mp4", 'wb') as f:
        print('Started ' + title)
        while True:
            vid_buf = resp.read(blocksize)
            if not vid_buf:
                break
            video.write(vid_buf)
            size += len(vid_buf)
            if length:
                vid_progress[title] = round(size*100/length)
                #print(vid_progress[title])
                #print('\r{:.2f} % Done  '.format(), end='')
                f.write(vid_buf)
    
    return video.getbuffer()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3333, debug=False, use_evalex=False)
