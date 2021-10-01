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

base = "https://eggporncomics.com"

def dl(url_):
    r = get(url_)

    html = BeautifulSoup(r.content,"html.parser")
    title = html.find('title').text.split("|")[0]
    # title = html.find("title", class_="panel-breadcrumb").find_all("a")[1].text.strip().split(sep=" - ")[0]
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
    
    # print(ch_name)

    directory = os.getcwd() + '/Comix/Manga/' + title + '/'

    try:
        os.mkdir(directory)
    except:
        # print("Err", e)
        pass

    global_vars.update_status((title), [0, 1, '', started])

    # global_vars.owl_pg_count['_'.join(title.split()) + '_' + '_'.join(ch_name.split()) + ".pdf"] = 0
    links = html.find_all("div", class_="grid-item")

    total_pgs = len(links)

    for img_link in links[:-2]:
        count = count + 1
        # print(count)
        # continue
        img_page_data = get(base + img_link.find("a").attrs['href'])

        page_html = BeautifulSoup(img_page_data.content,"html.parser")

        img = page_html.find("div", class_="comix").find("img").attrs['src']

        if count < 10:
            count_str = "0" + str(count)
        else:
            count_str = str(count)
        
        # print(base + img)
        # continue
        c = get(base + img)

        im_name = directory + title + img.split(sep="/")[-1]
        
        with open(im_name, 'wb') as f:
            f.write(c.content)
            print(im_name)

        im = Image.open(im_name)
        rgb_im = im.convert('RGB')
        rgb_im.save(im_name)
        
        img_arr.append(im_name)

        # global_vars.update_status( (title + ' - ' + ch_name), [count, total_pgs, rel_location + '_'.join(title.split()) + '_' + ch_name + ".pdf", started])
    
    print(img_arr)

    with open(manga_name + '_'.join(title.split()) + '_' + title + ".pdf", "wb") as f:
        f.write(img2pdf.convert([i for i in img_arr if i.endswith(".jpg")]))
        print('PDF Generated for', '_'.join(title.split()) + '_' + '_'.join(title.split()) + ".pdf")

    shutil.rmtree(directory)

dl('https://eggporncomics.com/comics/37886/straight-line-to-love-ch4')