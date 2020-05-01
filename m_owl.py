from requests import get
from bs4 import BeautifulSoup
import os
import shutil
import img2pdf
import sys
from PIL import Image

def dl(url_):
    r = get(url_)

    html = BeautifulSoup(r.content,"html.parser")
    title = html.find('div', {'id': 'bs-example-navbar-collapse-1'}).find('li', {'class': 'active'}).find('a').attrs['title']
    manga_name = os.getcwd() + '/Comix/Comix/Manga/' + title + '/'

    try:
        os.mkdir(manga_name)
    except:
        pass

    count = 0

    img_arr = []

    
    ch_name = html.find("img", class_="owl-lazy").attrs['data-src'].split('/')[-2]
    print(ch_name)

    directory = os.getcwd() + '/Comix/Comix/Manga/' + title + '/' + ch_name + '/'

    try:
        os.mkdir(directory)
    except:
        pass

    for img_page in html.find_all("img", class_="owl-lazy"):
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
            print(title + (count_str))

        im = Image.open(im_name)
        if(im.mode != 'RGB'):
            im = im.convert(mode='RGB')

        im.save(im_name)

    #print(img_arr)

    with open(manga_name + '_'.join(title.split()) + '_' + ch_name + ".pdf", "wb") as f:
        f.write(img2pdf.convert([i for i in img_arr if i.endswith(".jpg")]))
        print('PDF Generated for', '_'.join(title.split()) + '_' + ch_name + ".pdf")

    shutil.rmtree(directory)

#dl('http://chessmoba.us/reader/reader/182/669049')