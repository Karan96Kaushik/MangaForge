import os
from requests import get
from bs4 import BeautifulSoup
import urllib.request
from thumbnail_gen import thumb_dir

def dl_az(url):
	url_ = url
	r = get(url_)

	html = BeautifulSoup(r.content, "html.parser")
	name = html.find_all("title")[0].text

	#vid_progress[name] = "Started"

	directory = os.getcwd() + '/Comix/' + name + '/'

	try:
		os.mkdir(directory)
	except:
		print()

	count = 0
	for img_page in html.find_all("a", lightbox=True):
		clip_name = img_page.attrs['href'].split('/')[-1].split('.')[0]

		count = count + 1

		try:
			print('http:' + img_page.attrs['href'])
			b = get('http:' + img_page.attrs['href'])
			ext  = img_page.attrs['href'].split('.')[len(img_page.attrs['href'].split('.')) - 1]

			with open(directory + clip_name + str(count) + '.' + ext, 'wb') as f:
				f.write(b.content)
				print(clip_name + str(count) + '.' + ext)
		except Exception as ex:
			print(ex)
			

	for vid_link in html.find_all("a", lightbox=True, class_="video"):
		count = count + 1
		folder = directory + name + '/'

		b = get('https://www.aznude.com' + vid_link.attrs['href'])
		print(vid_link.attrs['href'])
		try:
			vid_url = BeautifulSoup(b.content,"html.parser").find_all("ul", class_="sorting-buttons")[0].find_all("a", href=True)[0].attrs['href']
			clip_name = vid_url.split('/')[-1]
			
			res = get('https:' + vid_url)
			with open(directory + str(count) + clip_name, 'wb') as f:
				f.write(res.content)
		except:
			a = 0
	
	thumb_dir(directory)
	#vid_progress[name] = "Done"
	print(name + " Completed")