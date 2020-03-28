import urllib.request
import io

def vidDownloader(url, title, directory):
    resp = urllib.request.urlopen(url)
    length = resp.getheader('content-length')
    if length:
        length = int(length)
        blocksize = max(4096, length//100)
    else:
        blocksize = 1000000 # just made something up

    print(length, blocksize)

    video = io.BytesIO()
    size = 0
    print(directory + title + '.mp4')
    with open(directory + title + '.mp4', 'wb') as f:
        while True:
            vid_buf = resp.read(blocksize)
            if not vid_buf:
                break
            video.write(vid_buf)
            size += len(vid_buf)
            if length:
                f.write(vid_buf)
                print('\r{:.2f} % Done  '.format(size*100/length), end='')