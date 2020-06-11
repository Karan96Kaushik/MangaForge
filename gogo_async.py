import async_get
import asyncio
import aiohttp
from bs4 import BeautifulSoup as bs
import global_vars as gv
from datetime import datetime
from get_page_links import get_page_links
from csv_writer import wr_csv, wr_head
from requests import get
from gogoanime import gogo_search,eps,get_vid_link

PARALELLS = 5

eps_ = []

async def parse_vid_link(url):
    print("Starting download from", url + "...")
    r = get(url)

    html = BeautifulSoup(r.content, "html.parser")
    # print(html)
    title = html.find("title").text.strip().split("Watch ")[1].split("at gogoanime")[0]
    frame = html.find_all("iframe")[0].attrs["src"]

    # print("Got Frame", frame)
    if frame.find("https") == -1:
        frame = "https:" + frame
    
    r = get(frame).content.decode()

    print("Finding video link...")

    vid_src_start = r.find("sources:[{file: '") + 17
    vid_src_end = r.find("',label: 'HD P','type' : 'mp4'}]")

    vid_src = r[vid_src_start: vid_src_end]

    return {
        "name": title.strip(),
        "link": vid_src
        }


async def make_request(session, req_link):
    _link = "https://upload.umin.ac.jp/cgi-open-bin/ctr_e/" + req_link.split("./")[1]
    async with session.get(_link, verify_ssl=False) as resp:
        if resp.status == 200:
            data = await resp.text()
            obj = await parse_data(data, req_link)
        else:
            with session.get(_link) as resp:
                if resp.status == 200:
                    print("retrying")
                    data = await resp.text()
                    obj = await parse_data(data, req_link)
                    gv.add_csv(obj)
                else:
                    print("req failed", _link)


async def main(urls):
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(
            *[make_request(session, i) for i in urls]
        )


link = "https://gogoanimetv.io/anime/hunter-x-hunter-2011-dub-/12189/"

urls = eps(link)

last = 0
for loc in range(int(len(urls)/PARALELLS)):
    print("running", loc)
    loop.run_until_complete(async_get.main(urls[loc* PARALELLS :loc* PARALELLS + PARALELLS]))
    last = loc* PARALELLS + PARALELLS

try:
    loop.run_until_complete(async_get.main(urls[last:]))
except:
    pass


