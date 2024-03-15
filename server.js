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
            userprof = parseprof[0]
            console.log(parseprof)
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
    res.render('AdminCreateEmployeeAccountGUI');
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
    var pythonProcess = spawn('python',["./AdminCreateEmployeeAccountController.py",myJSON2])
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

app.get('/createmanageraccount', (req,res) =>{
    res.render('AdminCreateManagerAccountGUI');
})

app.post('/createmanageraccount', (req,res) =>{
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
    var pythonProcess = spawn('python',["./AdminCreateManagerAccountController.py",myJSON2])
    pythonProcess.stdout.on('data',(data)=>{
    var bool = data.toString()
    console.log(bool)
    if (bool.trim() == "Failed")
    {
        req.flash('message15','Unable to create User. Double check your values entered')
        res.redirect('/createmanageraccount')
    }
    else
    {
        req.flash('message15','User Account Created')
        res.redirect('/createmanageraccount')
    }
})
})

app.get('/chooseaccount', (req,res) =>{
    res.render('ChooseAccount');
})


app.get('/admin_update', (req,res) =>{
    res.render('AdminUpdateChoose');
})

app.get('/createuserprofile', (req,res) =>{
    var pythonProcess = spawn('python',["./UserProfileSelectorController.py"])
    pythonProcess.stdout.on('data',(data) =>{
        try{
            var myList = JSON.parse(data.toString())
            res.render('AdminCreateUserProfileGUI',{myList, message: req.flash('message')})
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

app.post('/createuserprofile', (req,res) =>{
    const myJSON = {
        employeeid : req.body.employeeid,
        profile : req.body.selectedoption,
        role : req.body.role
    }
    const myJSON2 = JSON.stringify(myJSON)
    var pythonProcess = spawn('python',["./CreateUserProfileController.py",myJSON2])
    pythonProcess.stdout.on('data',(data)=>{
    var bool = data.toString()
    console.log(bool)
    if (bool.trim() == "Failed")
    {
        req.flash('message','Unable to create Profile. Double check your values entered')
        res.redirect('/createuserprofile')
    }
    else
    {
        req.flash('message','User Profile Created')
        res.redirect('/createuserprofile')
    }
})
})

app.get('/admin_update', (req,res) =>{
    res.render('AdminUpdateChoose');
})

app.get('/updateuserprofile', (req,res) =>{
    res.render('AdminUpdateUserProfileGUI',{message: req.flash('message')})
})

app.post('/updateuserprofile', (req,res) =>{
    const myJSON = {
        employeeid : req.body.employeeid,
        selectedoption : req.body.selectedoption,
        role : req.body.role
    }
    const myJSON2 = JSON.stringify(myJSON)
    var pythonProcess = spawn('python',["./UpdateUserProfileController.py",myJSON2])
    pythonProcess.stdout.on('data',(data)=>{
    var bool = data.toString()
    console.log(bool)
    if (bool.trim() == "Failed")
    {
        req.flash('message','Unable to update Profile. Double check your values entered')
        res.redirect('/updateuserprofile')
    }
    else
    {
        req.flash('message','User Profile Updated')
        res.redirect('/updateuserprofile')
    }
})
})

app.get('/adminupdateaccountchoose', (req,res) =>{
    res.render('AdminUpdateChooseAccount')
})

app.get('/adminupdateadminaccount', (req,res) =>{
    var pythonProcess = spawn('python',["./grabUserAccountTableColumnsController.py"])
    pythonProcess.stdout.on('data',(data) =>{
        try{
            var myList = JSON.parse(data.toString())
            res.render('AdminUpdateAdminAccountGUI',{myList, message: req.flash('message')})
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

app.post('/adminupdateadminaccount', (req,res) =>{
    const myJSON = {
        employeeid : req.body.employeeid,
        selectedoption : req.body.selectedoption,
        value : req.body.value
    }
    const myJSON2 = JSON.stringify(myJSON)
    console.log(myJSON2)
    var pythonProcess = spawn('python',["./AdminUpdateAdminAccountController.py",myJSON2])
    pythonProcess.stdout.on('data',(data)=>{
    var bool = data.toString()
    console.log(bool)
    if (bool.trim() == "Failed")
    {
        req.flash('message','Unable to update Admin Account. Double check your values entered')
        res.redirect('/adminupdateadminaccount')
    }
    else
    {
        req.flash('message','Admin Account Updated')
        res.redirect('/adminupdateadminaccount')
    }
})
})

app.get('/adminupdatemanageraccount', (req,res) =>{
    var pythonProcess = spawn('python',["./grabUserAccountTableColumnsController.py"])
    pythonProcess.stdout.on('data',(data) =>{
        try{
            var myList = JSON.parse(data.toString())
            res.render('AdminUpdateManagerAccountGUI',{myList, message: req.flash('message')})
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

app.post('/adminupdatemanageraccount', (req,res) =>{
    const myJSON = {
        employeeid : req.body.employeeid,
        selectedoption : req.body.selectedoption,
        value : req.body.value
    }
    const myJSON2 = JSON.stringify(myJSON)
    console.log(myJSON2)
    var pythonProcess = spawn('python',["./AdminUpdateManagerAccountController.py",myJSON2])
    pythonProcess.stdout.on('data',(data)=>{
    var bool = data.toString()
    console.log(bool)
    if (bool.trim() == "Failed")
    {
        req.flash('message','Unable to update Admin Account. Double check your values entered')
        res.redirect('/adminupdatemanageraccount')
    }
    else
    {
        req.flash('message','Admin Account Updated')
        res.redirect('/adminupdatemanageraccount')
    }
})
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