from thumbnail_gen import thumb_dir
import urllib.request
from bs4 import BeautifulSoup
from requests import get
import os

link = 'https://maharerait.mahaonline.gov.in/PrintPreview/PrintPreview?q=nkUq50jPnz0xUJnlq%2f84ocCVVE%2fesa2ZbmUlX4xYDkI9kK3i0HAue4lUAANAUThL7xpH7hlmbLhLbss9m%2bi4WC6IUKE88YOaVm4vjTWwoeEZNQO3ZHufO2R%2b4MTjVamfsSBlhLIlp2I97dAwTyeGfDL%2brSzsGo63dz4FZpej16JNy7HfBNd4Eg%3d%3d'

url_ = link
r = get(url_)

html = BeautifulSoup(r.content, "html.parser")
name = html.find_all("title")[0].text
print(html)
name = html.find_all("div", class_='col-md-3')

print(name)