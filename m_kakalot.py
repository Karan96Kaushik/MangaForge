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
    ch_name = html.find('title').text.split(" - ")[0]
    title = html.find("div", class_="panel-breadcrumb").find_all("a")[1].text.strip().split(sep=" - ")[0]
    print(title)
    manga_name = os.getcwd() + '/Comix/Manga/' + title + '/'
    rel_location = '/Comix/Manga/' + title + '/'
    started = datetime.now().timestamp()

    try:
        os.mkdir(manga_name)
    except Exception as e:
        print("Err", e)
        pass

    count = 0

    img_arr = []

    #ch_name = html.find("img", class_="owl-lazy").attrs['data-src'].split('/')[-2]
    # ch_name = (urllib.parse.parse_qs(ch_)["chapterName"][0])
    
    print(ch_name)

    directory = os.getcwd() + '/Comix/Manga/' + title + '/' + ch_name + '/'

    try:
        os.mkdir(directory)
    except:
        # print("Err", e)
        pass

    global_vars.update_status((title + ' - ' + ch_name), [0, 1, '', started])

    # global_vars.owl_pg_count['_'.join(title.split()) + '_' + '_'.join(ch_name.split()) + ".pdf"] = 0
    im_pages = html.find("div", class_="container-chapter-reader").find_all("img")

    total_pgs = len(im_pages)

    for img_page in im_pages:
        count = count + 1
        
        print(img_page.attrs['src'])
        
        if count < 10:
            count_str = "0" + str(count)
        else:
            count_str = str(count)
        
        headers = {
            "Host":"s61.mkklcdnv6tempv2.com",
            "Referer":"https://readmanganato.com/"
        }

        c = get(img_page.attrs['src'], headers=headers)
        print(c)
        im_name = directory + title + img_page.attrs['src'].split(sep="/")[-1]
        
        with open(im_name, 'wb') as f:
            f.write(c.content)
            print(im_name)

        im = Image.open(im_name)
        rgb_im = im.convert('RGB')
        rgb_im.save(im_name)
        
        img_arr.append(im_name)

        global_vars.update_status( (title + ' - ' + ch_name), [count, total_pgs, rel_location + '_'.join(title.split()) + '_' + ch_name + ".pdf", started])
    
    #print(img_arr)

    with open(manga_name + '_'.join(title.split()) + '_' + ch_name + ".pdf", "wb") as f:
        f.write(img2pdf.convert([i for i in img_arr if i.endswith(".jpg")]))
        print('PDF Generated for', '_'.join(title.split()) + '_' + '_'.join(ch_name.split()) + ".pdf")

    shutil.rmtree(directory)


# dl('https://readmanganato.com/manga-vy951833/chapter-136')