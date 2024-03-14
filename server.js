const express = require('express')
const path = require('path')
const bodyParser = require("body-parser")
var session = require('express-session')
var flush = require('connect-flash')
const spawn = require("child_process").spawn
var userprof = ''

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

app.get('/homepage', (req,res) =>{
    res.render(userprof + 'Page');
})

app.get('/manager_updateprofile', (req, res) => {
    // Render the UpdateManagerAccount.ejs page
    res.render('UpdateManagerAccount');
});

app.get('/manager_createws', (req, res) => {
    // Render the UpdateManagerAccount.ejs page
    res.render('CreateWorkShift');
});

app.get('/', (req, res) => {
    res.redirect('/logingui')
})

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
        if(loggedin.length != 0){
            loggedin.length = 0
        }
        if(loggedin.length === 0){
            var pythonProcess2 = spawn('python',["./GetEmployeeIDController.py",myJSON2])
                pythonProcess2.stdout.on('data',(data)=>{
                var alldata2 = JSON.parse(data.toString())
                myJSON["employeeid"] = alldata2[0][0]   
            })
            loggedin.push(myJSON)
            req.flash('message','Enter Details')
            const parseprof = req.body.selectedoption.split(' ')
            userprof = parseprof[1]
            console.log(userprof)
            res.redirect('/homepage')    
        }
    }
})
})

app.get('/createuserorprofile', (req,res) =>{
    res.render('CreateUserOrProfile');
})

app.get('/createadminaccount', (req,res) =>{
    res.render('AdminCreateAdminAccountGUI');
})

app.post('/createadminaccount', (req,res) =>{
    const myJSON = {
        fullname : req.body.name,
        address : req.body.Address,
        email : req.body.email,
        phonenumber : req.body.Number,
        username : req.body.username,
        password : req.body.password,
        Maxhrs : req.body.MaxHours
    }
    const myJSON2 = JSON.stringify(myJSON)
    console.log(myJSON)
    console.log(myJSON2)
    var pythonProcess = spawn('python',["./AdminCreateAdminAccountController.py",myJSON2])
    pythonProcess.stdout.on('data',(data)=>{
    var bool = data.toString()
    console.log(bool)
    if (bool.trim() == "Failed")
    {
        req.flash('message15','Unable to create User. Double check your values entered')
        res.redirect('/createadminaccount')
    }
    else
    {
        req.flash('message15','User Account Created')
        res.redirect('/createadminaccount')
    }
})
})

app.get('/createemployeeaccount', (req,res) =>{
    res.render('EmployeeCreateEmployeeAccountGUI');
})

app.post('/createemployeeaccount', (req,res) =>{
    const myJSON = {
        fullname : req.body.name,
        address : req.body.Address,
        email : req.body.email,
        phonenumber : req.body.Number,
        username : req.body.username,
        password : req.body.password,
        Maxhrs : req.body.MaxHours
    }
    const myJSON2 = JSON.stringify(myJSON)
    console.log(myJSON)
    console.log(myJSON2)
    var pythonProcess = spawn('python',["./EmployeeCreateEmployeeAccountController.py",myJSON2])
    pythonProcess.stdout.on('data',(data)=>{
    var bool = data.toString()
    console.log(bool)
    if (bool.trim() == "Failed")
    {
        req.flash('message15','Unable to create User. Double check your values entered')
        res.redirect('/createemployeeaccount')
    }
    else
    {
        req.flash('message15','User Account Created')
        res.redirect('/createemployeeaccount')
    }
})
})

app.get('/chooseaccount', (req,res) =>{
    res.render('ChooseAccount');
})

//UpdateManagerAccount
app.get('/updatemanageraccount', (req,res) =>{
    res.render('UpdateManagerAccount');
})

app.post('/updatemanageraccount', (req,res) =>{
    const myJSON = {
        fullname : req.body.name,
        email : req.body.email,
        phonenumber : req.body.Number,
        username : req.body.username,
        password : req.body.password,
        Maxhrs : req.body.MaxHours
    }
    const myJSON2 = JSON.stringify(myJSON)
    console.log(myJSON)
    console.log(myJSON2)
    var pythonProcess = spawn('python',["./UpdateManagerAccountController.py",myJSON2])
    pythonProcess.stdout.on('data',(data)=>{
    var bool = data.toString()
    console.log(bool)
    if (bool.trim() == "Failed")
    {
        req.flash('message15','Unable to update account. Double check your values entered')
        res.redirect('/UpdateManagerAccount')
    }
    else
    {
        req.flash('message15','Update Account successful')
        res.redirect('/UpdateManagerAccount')
    }
})
})


//Listening to port 3000
app.listen(port, () => console.info('Listening on port ',port))