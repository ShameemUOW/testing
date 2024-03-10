const express = require('express')
const path = require('path')
const bodyParser = require("body-parser")
var session = require('express-session')
var flush = require('connect-flash')

const app = express()
const port = 3000

app.set('views','./views')
app.set('view engine','ejs')

//static files
app.use(express.static('public'))
app.use('/css',express.static(__dirname +"public/css"))
app.use('/js',express.static(__dirname +"public/js"))
app.use('/img',express.static(__dirname +"public/img"))

app.get('',(req,res) =>{
    res.render('index')
})

//Listening to port 3000
app.listen(port, () => console.info('Listening on port ',port))