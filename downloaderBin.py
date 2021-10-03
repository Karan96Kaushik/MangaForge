from PIL import Image
from requests import get
from bs4 import BeautifulSoup
from time import sleep
import os
import shutil
import img2pdf
import sys
import io
# import _thread
import urllib.request
import pyperclip
import subprocess
from comicParsers import dl_allporncomics, dl_haven, dl_porncomix, dl_sexporncomics

import global_vars

from aznude import dl_az
from m_owl import dl
import m_kakalot
from xnxx import page as xnxx
from owl_chaps import get_chaps

import argparse

parser = argparse.ArgumentParser(description='MangaForge')
parser.add_argument('--url', help='foo help')

args = parser.parse_args()

save_location = os.getcwd() + '/Comix/'

vid_progress = {}

owl_pg_count = {}

def sel(_url):
	resp = ''

	url = ''
	if(_url == ''):
		url = pyperclip.paste()
	else:
		url = _url
	
	if url.split('.com')[0] == 'https://mangakakalot' or url.split('.com')[0] == 'https://manganelo' or url.split('.com')[0] == 'https://readmanganato':
		m_kakalot.dl(url)
		resp = 'Manga Kakalot'
		pass
	elif url.split('.com')[0] == 'https://allporncomic':
		dl_allporncomics(url)
		resp = 'APC'
		pass
	else:
		resp = 'Unknown Source, Dowload Failed for "' + _url + '"'
	return resp

print(sel(args.url))

# if __name__ == '__main__':
# 	app.run(host='0.0.0.0', port=3333, debug=False, use_evalex=False)
