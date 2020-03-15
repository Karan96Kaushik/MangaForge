const express = require('express')
const bodyParser = require('body-parser')
const app = express()
var fs = require('fs');

//const routes = Routes(app)

global.path = require('path');

app.listen(1996);

app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())
app.use(express.static('Comix'));
app.set('etag', false);

console.log('Server started')

app.get('/', (req, res) => {
    var files = fs.readdirSync('/home/karan/Documents/GitWorkSpace/Comix_Cloner/Comix/');
    var _files = []
    files.forEach(element => {
        _files.push("http://192.168.31.167:1996/" + element)
    });
    res.json(_files);
})

app.get('/files', (req, res) => {
    var html = ` <head></head><body>`
    var files = fs.readdirSync('/home/karan/Documents/GitWorkSpace/Comix_Cloner/Comix/');

    files.forEach(element => {
        var lnk = '<a href="http://192.168.31.167:1996/' + element + '">' + element + '</a><br>'
        html += lnk
    });

    html += '</body>'
    res.send(html);
})