from urllib.request import Request, urlopen
import io

def vidDownloader(url, title, directory):
    req = Request(url)
    req.add_header("User-Agent", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0")
    resp = urlopen(req)

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