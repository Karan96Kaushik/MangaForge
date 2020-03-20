const express = require('express')
const bodyParser = require('body-parser')
const app = express()
const path = require('path')

var fs = require('fs');

global.path = require('path');

app.listen(1996);

app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())
app.use(express.static('Comix'));
app.set('etag', false);

console.log('Server started')

app.get('/files', (req, res) => {
    var html = ` <head></head><body>`
    var files = fs.readdirSync(__dirname + '/Comix/');

    files.forEach(element => {
        var lnk = '<a href="/' + element + '">' + element + '</a><br>'
        html += lnk
    });

    html += '</body>'
    res.send(html);
})