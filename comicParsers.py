from PIL import Image
from requests import get
from bs4 import BeautifulSoup
import os
import shutil
import img2pdf
import global_vars
import io
import urllib.request

save_location = os.getcwd() + '/Comix/'
vid_progress = {}


def dl_allporncomics(url):
	#ext = '.gif'

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

	directory = save_location + title + '/'

	try:
		os.mkdir(directory)
	except:
		print()

	for img_page in html.find_all("div", class_="page-break"):
		count = count + 1
		img_link = img_page.find_all("img")[0].attrs['data-src']

		if count < 10:
			count_str = "0" + str(count)
		else:
			count_str = str(count)
		c = get(img_link.strip())
		ext = img_link.split('.')[-1]

		with open(directory + title + (count_str) + ext, 'wb') as f:
			f.write(c.content)
			print(title + ' ' + (count_str))
		
		Image.open(directory + title + (count_str) + ext).convert('RGB').save(directory + title + (count_str) + '.jpg')
		img_arr.append(directory + title + (count_str) + '.jpg')

	#print(img_arr)

	try:
		with open(save_location + "Comix/" + title + ".pdf", "wb") as f:
			f.write(img2pdf.convert([i for i in img_arr if i.endswith('.jpg')]))
	except:
		print()

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
		with open(save_location + "Comix/" + title + ".pdf", "wb") as f:
			f.write(img2pdf.convert([i for i in img_arr if i.endswith('.jpg')]))
	except:
		print()

	print('PDF Generated ' + title)
	shutil.rmtree(directory)

def dl_porncomix(url):
	url_ = url
	r = get(url_)

	html = BeautifulSoup(r.content, "html.parser")

	count = 0

	img_arr = []

	if True:
	# try:
		title = html.find_all("title")[0].text
		print(title)
	# except:
		pass

	directory = save_location + '/cache/' + title + '/'

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
			ext = '.' + img_link.split('.')[-1]

			with open(directory + title + (count_str) + ext, 'wb') as f:
				f.write(c.content)
				print(title + (count_str))
			
			Image.open(directory + title + (count_str) + ext).convert('RGB').save(directory + title + (count_str) + '.jpg')
			img_arr.append(directory + title + (count_str) + '.jpg')
				
	print(img_arr)


	with open(save_location + "Comix/" + title + ".pdf", "wb") as f:
		f.write(img2pdf.convert([i for i in img_arr if i.endswith(".jpg")]))
	
	print('PDF Generated ' + title)
	shutil.rmtree(directory)

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
