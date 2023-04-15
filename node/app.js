const express = require('express');
const os = require('os');
const request = require('request');
var hostname = os.hostname();
const app = express();
app.set('port', process.env.PORT || 3000);

app.get('/', (req,res)=>{
    res.send(`hostname: ${hostname}<br/>version: ${process.env.VERSION}`);
});

app.get('/api/', (req, res)=>{
    var version = req.query.version
    var headers = {
        'version': version
    }
    const options = {
        // call using service name
        // uri: 'http://echo-hostname-backend:8000'
        uri: `${process.env.REQUEST_URL}`,
        headers:headers
    }
    request(options, (err, response, body)=>{
        res.send(`hostname: ${hostname}<br/>version: ${process.env.VERSION}</br><br/>api from backend : ${body}`)
    })
})

app.listen(app.get('port'), ()=>{
    console.log(`${app.get ('port')} listening...`);
});
