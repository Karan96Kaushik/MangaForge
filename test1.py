import urllib.request
import sys
import io

try:
    url = sys.argv[1]
except IndexError:
    print("usage: test.py url")
    exit(2)

resp = urllib.request.urlopen(url)
length = resp.getheader('content-length')
if length:
    length = int(length)
    blocksize = max(4096, length//100)
else:
    blocksize = 1000000 # just made something up

print(length, blocksize)
title = 'Test_Vid11'

video = io.BytesIO()
size = 0
with open("Comix/" + title + ".mp4", 'wb') as f:
    while True:
        vid_buf = resp.read(blocksize)
        if not vid_buf:
            break
        video.write(vid_buf)
        size += len(vid_buf)
        if length:
            f.write(vid_buf)
            print('\r{:.2f} % Done  '.format(size*100/length), end='')