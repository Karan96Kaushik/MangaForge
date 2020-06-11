from gogoanime import gogo_search,eps,get_vid_link
from requests import get
#gogo_search("hunter x hunter")

link = "https://gogoanimetv.io/anime/hunter-x-hunter-2011-dub-/12189/"

episodes = eps(link)
# print(episodes)
for ep in episodes:
    print(ep)
    epi = get_vid_link(ep["value"])
    epi["anime"] = ep["anime"]
    epi["anime_url"] = ep["anime_url"]
    res = get("http://localhost:4545/gogo_ep", json=epi).content

    print(res)