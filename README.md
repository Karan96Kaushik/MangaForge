# Comix Cloner Server

## Features

1. Downloads Images from comic sites and converts to PDF
    1. PComix.info
    1. SPComic.com
    1. AllPComics.com
1. Downloads videos from HH.org
1. Serves static files on local server
1. Provides pages to access static files and start download jobs

## Usage

1. Run **$ python3 downloader.py** for main downloader server
1. Run **$ node server** to start static file server
1. Use **http://0.0.0.0:3333/link** to send and monitor download jobs
1. Use **http://0.0.0.0:1996/files** to access static files
1. Use **http://0.0.0.0:1996/dex.html** to access gallery
1. Use **http://0.0.0.0:3333/prog** to access gallery
1. Use **python3 efukt.py <url> <folder>**

## Installation

1. Instead of using "pip3 install Pillow", use "sudo apt install python3-pillow"
2. Install modules in requirements.txt
3. Create cache and Comix folders

## Files & Folders

1. **Comix/** : Static File storage
1. **downloader.py** : Downloader script
1. **server.js** : Static file server
1. **efukt.py** : Continous Efukt vid downloader
1. **vidDL.py** : Vid downloader module (to be imported)