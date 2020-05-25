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

def dl(url_):
    r = get(url_)

    html = BeautifulSoup(r.content,"html.parser")
    title = html.find('div', {'id': 'bs-example-navbar-collapse-1'}).find('li', {'class': 'active'}).find('a').attrs['title']
    manga_name = os.getcwd() + '/Comix/Comix/Manga/' + title + '/'
    rel_location = '/Comix/Comix/Manga/' + title + '/'
    started = datetime.now().timestamp()

    try:
        os.mkdir(manga_name)
    except:
        pass

    count = 0

    img_arr = []

    #ch_name = html.find("img", class_="owl-lazy").attrs['data-src'].split('/')[-2]
    ch_ = html.find("iframe", id="readerContinue").attrs["src"]
    ch_name = (urllib.parse.parse_qs(ch_)["chapterName"][0])
    print(ch_name)

    directory = os.getcwd() + '/Comix/Comix/Manga/' + title + '/' + ch_name + '/'

    try:
        os.mkdir(directory)
    except:
        pass

    global_vars.update_status((title + ' - ' + ch_name), [0, 1, '', started])

    # global_vars.owl_pg_count['_'.join(title.split()) + '_' + '_'.join(ch_name.split()) + ".pdf"] = 0
    im_pages = html.find_all("img", class_="owl-lazy")

    total_pgs = len(im_pages)

    for img_page in im_pages:
        #print(img_page)
        count = count + 1
        
        #print(img_page.attrs['data-src'])
        
        if count < 10:
            count_str = "0" + str(count)
        else:
            count_str = str(count)
        
        c = get(img_page.attrs['data-src'])

        im_name = directory + title + ch_name + (count_str) + ".jpg"
        
        img_arr.append(im_name)
        
        with open(im_name, 'wb') as f:
            f.write(c.content)
            print(im_name)

        im = Image.open(im_name)
        if(im.mode != 'RGB'):
            im = im.convert(mode='RGB')

        im.save(im_name)

        global_vars.update_status( (title + ' - ' + ch_name), [count, total_pgs, rel_location + '_'.join(title.split()) + '_' + ch_name + ".pdf", started])
    
    #print(img_arr)

    with open(manga_name + '_'.join(title.split()) + '_' + ch_name + ".pdf", "wb") as f:
        f.write(img2pdf.convert([i for i in img_arr if i.endswith(".jpg")]))
        print('PDF Generated for', '_'.join(title.split()) + '_' + '_'.join(ch_name.split()) + ".pdf")

    shutil.rmtree(directory)

#dl('http://chessmoba.us/reader/reader/182/669049')