const express = require('express')
const bodyParser = require('body-parser')
const app = express()
const path = require('path')
const fs = require('fs');
const cors = require('cors')
const { spawn } = require('child_process');

global.path = require('path');

app.listen(1996);

app.use(cors())
app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())
app.use(express.static('Comix'));
app.use(express.static('public'));
app.set('etag', false);

console.log('Server started')

app.post('/download', async (req, res) => {

	let url = req.body.url

	const dowloader = spawn('./downloaderBin', ['--url='+url]);

	dowloader.stdout.on('data'	, (data) => console.log(`stdout: ${data}`))
	dowloader.stderr.on('data'	, (data) => console.log(`err: ${data}`))

	dowloader.on('close', (code) => {
		console.log(`exit: ${code}`)
		res.send("Completed")
	})

})






app.get('/files', (req, res) => {
	var html = ` <head></head><body>`
	var files = fs.readdirSync(__dirname + '/Comix/');

	files.forEach(element => {
		var lnk = '<a href="/Comix/' + element + '">' + element + '</a><br>'
		html += lnk
	});

	html += '</body>'
	res.send(html);
})


app.get('/jsonfolders', (req, res) => {
	catalogger()
	res.json(folders);
})

app.get('/json', (req, res) => {
	catalogger()
	res.json(tree_pics[req.query.folder]);
})

app.get('/jsonvids', (req, res) => {
	catalogger()
	vids = []
	tree_vids[req.query.folder].forEach(el => {
		vids. push({
			title: el,
			href: '/Comix/' + req.query.folder + '/' + el,
			type: 'video/mp4',
			//poster: 'https://i.imgur.com/MUSw4Zu.jpg'
		})
	})
   // console.log(vids);
	res.json(vids);
})

var tree_vids = {}
var tree_pics = {}

var folders = [];

function catalogger() {
	tree_vids = {}
	tree_pics = {}
	folders = [];
	
	var filesfolders = fs.readdirSync(__dirname + '/Comix/')


	filesfolders.forEach(el => {
		if(el.endsWith('.jpg') || el.endsWith('.html') || el.endsWith('.pdf') || el.endsWith('.png') || el.endsWith('.mp4') || el.endsWith('.ico') || el.endsWith('.sql')) {
		} else {
			folders.push(el)
		}
	})
	
	folders.forEach( el => {
		tree_pics[el] = []
		var files = fs.readdirSync(__dirname + '/Comix/' + el)
		files.forEach(pic => {
			if(pic.endsWith('.jpg')) {
				tree_pics[el].push(pic)
			}
		})
	})
	
	folders.forEach( el => {
		tree_vids[el] = []
		var files = fs.readdirSync(__dirname + '/Comix/' + el)
		files.forEach(vid => {
			if(vid.endsWith('.mp4')) {
				tree_vids[el].push(vid)
			}
		})
	})
}