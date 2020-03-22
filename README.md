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

## Files & Folders

1. **Comix/** : Static File storage
1. **downloader.py** : Downloader script
1. **server.js** : Static file server