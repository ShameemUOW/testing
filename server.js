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
const loggedin = []


app.get('/logingui', (req,res) =>{
    var pythonProcess = spawn('python',["./UserProfileSelectorController.py"])
    pythonProcess.stdout.on('data',(data) =>{
        try{
            var myList = JSON.parse(data.toString())
            res.render('LoginGUI',{myList, message: req.flash('message')})
        }catch(error){
            console.error('Error parsing JSON data:, error')
            res.status(500).send('Error parsing JSON data')
        }
    })
    pythonProcess.stderr.on('data',(data) =>{
        console.error('Error from Python Script:', data.toString())
        res.status(500).send('Error from python script')
    })
})

app.post("/logingui", (req,res)=>{
    
    const myJSON = {
        username: req.body.Username,
        password: req.body.Password,
        mainrole: req.body.selectedoption
    }
    const myJSON2 = JSON.stringify(myJSON)
    console.log(myJSON2)
    var pythonProcess = spawn('python',["./LoginController.py",myJSON2])
    pythonProcess.stdout.on('data',(data)=>{
    var bool = data.toString()
    console.log(bool)
    if (bool == "False\r\n")
    {
        req.flash('message','Invalid User')
        res.redirect('/logingui')
        
    }
    else
    {
        req.flash('message','Correct User')
        res.redirect('/logingui')
    }
})
})


//Listening to port 3000
app.listen(port, () => console.info('Listening on port ',port))