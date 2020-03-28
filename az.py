from requests import get
from bs4 import BeautifulSoup
from fpdf import FPDF
import os
import img2pdf
import sys
import pyperclip
import urllib.request

def video_download(url, title, folder):
	url = url.replace(' ', '%20')
	print(url + 'A')
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
	with open(folder + title + ".mp4", 'wb') as f:
		print('Started ' + title)
		while True:
			vid_buf = resp.read(blocksize)
			if not vid_buf:
				break
			video.write(vid_buf)
			size += len(vid_buf)
			if length:
				vid_progress[title] = round(size*100/length)
				print(vid_progress[title])
				f.write(vid_buf)

url_ = pyperclip.paste() #'https://www.aznude.com/view/celeb/p/parishilton.html'
#url_ = 'https://www.aznude.com/view/celeb/p/parishilton.html'
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
	except:
		a = 0
		print('Err ' + clip_name + str(count), img_page)

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
		#print()

	#video_download('https:' + vid_url, name + str(count), folder)
