from PIL import Image
from requests import get
from bs4 import BeautifulSoup
from time import sleep
from flask import Flask, request, jsonify, json, abort, redirect, send_file, logging
from flask_cors import CORS, cross_origin
from logging.handlers import RotatingFileHandler
import os
import shutil
import img2pdf
import sys
import io
import _thread
import urllib.request
import pyperclip
import subprocess
from comicParsers import dl_allporncomics, dl_haven, dl_porncomix, dl_sexporncomics

import global_vars

app = Flask(__name__)

# log = logging.getLogger('werkzeug')
# log.setLevel(logging.ERROR)

from aznude import dl_az
from m_owl import dl
import m_kakalot
from xnxx import page as xnxx
from owl_chaps import get_chaps

save_location = os.getcwd() + '/Comix/'

vid_progress = {}
methods = ('GET', 'POST')
app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/status', methods=methods)
def hello_wo():
	return jsonify(global_vars.get_status())

@app.route('/down', methods=methods)
def hello_world():
	req = request.args
	resp = sel(req.get('fname'))
	return jsonify([resp])

@app.route('/jsondown', methods=methods)
def down_json():
	url = (request.form['fname'] + '')
	resp = sel(url)
	return resp

@app.route('/clip', methods=methods)
def hell():
	req = request.args
	sel('')
	return redirect('/link')

@app.route('/anime_list', methods=methods)
def chaps():
	req = request.args
	print(req["url"])
	print(get_chaps(req["url"]))
	return jsonify(get_chaps(req["url"]))

@app.route('/vids', methods=methods)
def vids():
	return jsonify(vid_progress)

@app.route('/jsonfolders', methods=methods)
def jsonfolders():
	mypath = os.getcwd() + '/Comix/'

	fol = []
	for (dirpath, dirnames, filenames) in os.walk(mypath):
		fol.extend(dirnames)
		break

	return jsonify(fol)
	
@app.route('/json', methods=methods)
def json():
	req = request.args
	folder = req.get('folder')
	mypath = os.getcwd() + '/Comix/' + folder + '/'

	files = []
	for (dirpath, dirnames, filenames) in os.walk(mypath):
		print(filenames)
		for file in filenames:
			if(file.endswith('.jpg')):
				files.append(file)
		break
	
	return jsonify(files)

@app.route('/jsonvids', methods=methods)
def jsonvids():
	req = request.args
	folder = req.get('folder')
	mypath = os.getcwd() + '/Comix/' + folder + '/'

	files = []
	for (dirpath, dirnames, filenames) in os.walk(mypath):
		print(filenames)
		for file in filenames:
			if(file.endswith('.mp4')):
				files.append({
					'title': file,
					'href': '/Comix/' + folder + '/' + file,
					'type': 'video/mp4',
					'poster': '/Comix/' + folder + '/thumbs/' + file + '.jpg',
				})
		break
	
	return jsonify(files)

##	GOGO Anime

from gogoanime import eps, gogo_search, get_vid_link

@app.route('/gogo_eps', methods=methods)
def gogos():
	req = request.args
	print(req["url"])
	# print(get_chaps(req["url"]))
	return jsonify(eps(req["url"]))

@app.route('/gogo_search', methods=methods)
def gogosearch():
	req = request.args
	print(req["string"])
	# print(get_chaps(req["url"]))
	return jsonify(gogo_search(req["string"]))

@app.route('/gogo_video', methods=methods)
def gogovid():
	req = request.args
	print(req["url"])
	# print(get_chaps(req["url"]))
	return jsonify([ get_vid_link(req["url"]) ])


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
	return send_file('public/' + path)

@app.route('/prog', methods=['GET'])
def s():
	return send_file('if.html')

owl_pg_count = {}

def sel(_url):
	resp = ''

	print('SEL', _url)
	url = ''
	if(_url == ''):
		url = pyperclip.paste()
	else:
		url = _url
	
	if url.split('$$')[0] == '':
		_thread.start_new_thread(dl, (url.split('$$')[1], ))
		resp = 'Manga Owl'
		pass
	elif url.split('.us')[0] == 'http://chessmoba':
		_thread.start_new_thread(dl, (url, ))
		resp = 'Manga Owl'
		pass
	elif url.split('.us')[0] == 'https://chessmoba':
		_thread.start_new_thread(dl, (url, ))
		resp = 'Manga Owl'
		pass
	elif url.split('.com')[0] == 'https://mangaowl':
		_thread.start_new_thread(dl, (url, ))
		resp = 'Manga Owl'
		pass
	elif url.split('.com')[0] == 'https://thefashion101':
		_thread.start_new_thread(dl, (url, ))
		resp = 'Manga Owl'
		pass
	elif url.split('.com')[0] == 'https://mangakakalot' or url.split('.com')[0] == 'https://manganelo' or url.split('.com')[0] == 'https://readmanganato':
		_thread.start_new_thread(m_kakalot.dl, (url, ))
		resp = 'Manga Kakalot'
		pass
	elif url.split('.com')[0] == 'https://xnxx':
		_thread.start_new_thread(xnxx, (url,"XNXX", ))
		resp = 'xnxx'
		pass
	elif url.split('.com')[0] == 'https://allporncomic':
		_thread.start_new_thread(dl_allporncomics, (url, ))
		resp = 'APC'
		pass
	elif url.split('.com')[0] == 'https://sexporncomics':
		_thread.start_new_thread(dl_sexporncomics, (url, ))
		resp = 'SPC'
		pass
	elif url.split('.info')[0] == 'https://www.porncomix':
		_thread.start_new_thread(dl_porncomix, (url, ))
		resp = 'PC'
		pass
	elif url.split('.org')[0] == 'https://hentaihaven':
		_thread.start_new_thread(dl_haven, (url, ))
		resp = 'HH'
		pass
	elif url.split('.com')[0] == 'https://www.aznude':
		_thread.start_new_thread(dl_az, (url, ))
		resp = 'AZ'
		pass
	else:
		resp = 'Unknown Source, Dowload Failed for "' + _url + '"'
	return resp



if __name__ == '__main__':
	app.run(host='0.0.0.0', port=3333, debug=False, use_evalex=False)
