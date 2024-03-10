const express = require('express')
const path = require('path')
const bodyParser = require("body-parser")
var session = require('express-session')
var flush = require('connect-flash')
const spawn = require("child_process").spawn

const app = express()
const port = 3000

app.use(bodyParser.urlencoded({extended:false}))
app.use(bodyParser.json())
app.use(session({
    secret:'secret',
    resave:false,
    saveUninitialized:false
}))
app.use(flush())

app.set('views','./views')
app.set('view engine','ejs')

//static files
app.use(express.static('public'))
app.use('/css',express.static(__dirname +"public/css/"))
app.use('/js',express.static(__dirname +"public/js/"))
app.use('/img',express.static(__dirname +"public/img/"))

app.use(express.json())

app.get('/logingui', (req,res) =>{
    res.render('LoginGUI',{message: req.flash('message')});
})

//Listening to port 3000
app.listen(port, () => console.info('Listening on port ',port))