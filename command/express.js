var express = require('express')
var bodyParser = require('body-parser')
var bodyCookie = require('cookie-parser')
var session = require('express-session')

var app = express()

app.use(express.static('www'))
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: false }))
app.use(session({
    secret: 'quanquan',
    key: 'quanquan',
    cookie: { maxAge: 1000 * 60 * 60 * 24 * 30 },
    resave: false,
    saveUninitialized: true,
}));

console.log('init express.')

module.exports = app