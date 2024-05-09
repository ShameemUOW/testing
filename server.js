const express = require('express')
const path = require('path')
const bodyParser = require("body-parser")
var session = require('express-session')
var flush = require('connect-flash')
const spawn = require("child_process").spawn
const Holiday = require('date-holidays');

const app = express()
const port = process.env.PORT || 3000

app.use(bodyParser.urlencoded({extended:false}))
app.use(bodyParser.json())
app.use(session({
    secret:'oHn2mKV567n1m$%^',
    resave:false,
    saveUninitialized:true
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

function getFiles() {
    fs = require('fs')
    files = fs.readdirSync('./views')
    if(files.includes('AdminCreateAdminAccountGUI.ejs')){
        console.log('yes')
    }
}

getFiles()

app.get('/homepage', (req,res) =>{
    res.render(ssn.userprof + 'Page');
})

app.get('/resetpassword', (req,res) =>{
    res.render('ResetPassword', {username : ssn.username});
})

app.get('/createmanagerchoose', (req,res) =>{
    res.render('ManagerCreateChooseGUI');
})

app.get('/viewmanagerchoose', (req,res) =>{
    res.render('ManagerViewChooseGUI');
})

app.get('/searchfiltermanagerchoose', (req,res) =>{
    res.render('ManagerSearchFilterChooseGUI');
})

app.get('/manager_search', (req,res) =>{
    res.render('ManagerSearchChooseGUI');
})

app.get('/manager_filter', (req,res) =>{
    res.render('ManagerFilterChooseGUI');
})

app.get('/updatemanagerchoose', (req,res) =>{
    res.render('ManagerUpdateChooseGUI');
})

app.get('/empupdatechoose', (req,res) =>{
    res.render('EmployeeUpdateChoose');
})

app.get('/rejectapprovemanagerchoose', (req,res) =>{
    res.render('ManagerDecisionChooseGUI');
})

app.get('/deletemanagerchoose', (req,res) =>{
    res.render('ManagerDeleteChooseGUI');
})

app.get('/adminfilterchoose', (req,res) =>{
    res.render('AdminFilterAccountsGUI.ejs');
})

app.post("/resetpass", (req,res)=>{
    ssn = req.session
    const myJSON = {
        password: req.body.newpass,
        employeeid: ssn.emlpoyeeidentity
    }
    const myJSON2 = JSON.stringify(myJSON)
    console.log(myJSON2)
    var pythonProcess = spawn('python',["./ResetPasswordController.py",myJSON2])
    pythonProcess.stdout.on('data',(data)=>{
    var bool = data.toString()
    })
    res.redirect('/homepage')
})

app.get('/', (req, res) => {
    res.redirect('/logingui')
})

app.get('/logout', (req,res) => {
    ssn = req.session
    if(ssn.userprof){
        delete ssn.userprof
    }
    res.redirect('/')
})

app.get('/logingui', (req,res) =>{
    ssn = req.session
    var pythonProcess = spawn('python',["./UserProfileSelectorController.py"])
    pythonProcess.stdout.on('data',(data) =>{
        try{
            var myList = JSON.parse(data.toString())
            res.render('LoginGUI',{myList, message: req.flash('message')})
            console.log(myList)
        }catch(error){
            console.error('Error parsing JSON data:, error')
            res.status(500).send('Error parsing JSON data')
        }
    })
    pythonProcess.stderr.on('data',(data) =>{
        console.error('Error from Python Script:', data.toString())
        res.status(500).send('Error from python script')
    })
    if(ssn.userprof){
        res.redirect("/homepage")
    }
})

app.post("/logingui", (req,res)=>{
    ssn = req.session
    ssn.emlpoyeeidentity = 0
    ssn.username = req.body.Username
    const myJSON = {
        username: req.body.Username,
        password: req.body.Password,
        mainrole: req.body.selectedoption
    }
    const myJSON2 = JSON.stringify(myJSON)
    console.log(myJSON2)
    var pythonProcess = spawn('python',["./LoginController.py",myJSON2])
    pythonProcess.stdout.on('data',(data)=>{
    req.flash('message', null)
    var bool = data.toString().trim()
    console.log(bool)
    if (bool == "False")
    {
        req.flash('message', null);
        req.flash('message','Invalid User')
            // Redirect to login page
        res.redirect('/logout');
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
                ssn.emlpoyeeidentity = myJSON["employeeid"]
                console.log(ssn.emlpoyeeidentity)
                ssn.userprof = req.body.selectedoption
                res.redirect('/homepage')  
            })   
        }
    }
})
})

app.get('/createuserorprofile', (req,res) =>{
    res.render('CreateUserOrProfile');
})

app.get('/createadminaccount', (req,res) =>{
    res.render('AdminCreateAdminAccountGUI',{message: req.flash('message15')});
    console.log(ssn.userprof)
})

app.post('/createadminaccount', (req,res) =>{
    const myJSON = {
        fullname : req.body.name,
        address : req.body.Address,
        email : req.body.email,
        phonenumber : req.body.Number,
        username : req.body.username,
        password : req.body.password,
        chatid : req.body.chatid,
        Maxhrs : req.body.MaxHours
    }
    const myJSON2 = JSON.stringify(myJSON)
    console.log(myJSON)
    console.log(myJSON2)
    var pythonProcess = spawn('python',["./AdminCreateAdminAccountController.py",myJSON2])
    pythonProcess.stdout.on('data',(data)=>{
    req.flash('message15', null)
    var bool = data.toString()
    console.log(bool.trim())
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
    res.render('AdminCreateEmployeeAccountGUI',{message: req.flash('message16')});
})

app.post('/createemployeeaccount', (req,res) =>{
    const myJSON = {
        fullname : req.body.name,
        address : req.body.Address,
        email : req.body.email,
        phonenumber : req.body.Number,
        username : req.body.username,
        password : req.body.password,
        chatid : req.body.chatid,
        Maxhrs : req.body.MaxHours
    }
    const myJSON2 = JSON.stringify(myJSON)
    console.log(myJSON)
    console.log(myJSON2)
    var pythonProcess = spawn('python',["./AdminCreateEmployeeAccountController.py",myJSON2])
    pythonProcess.stdout.on('data',(data)=>{
    req.flash('message16', null)
    var bool = data.toString()
    console.log(bool)
    if (bool.trim() == "Failed")
    {
        req.flash('message16','Unable to create User. Double check your values entered')
        res.redirect('/createemployeeaccount')
    }
    else
    {
        req.flash('message16','User Account Created')
        res.redirect('/createemployeeaccount')
    }
})
})

app.get('/createmanageraccount', (req,res) =>{
    res.render('AdminCreateManagerAccountGUI',{message: req.flash('message17')});
})

app.post('/createmanageraccount', (req,res) =>{
    const myJSON = {
        fullname : req.body.name,
        address : req.body.Address,
        email : req.body.email,
        phonenumber : req.body.Number,
        username : req.body.username,
        password : req.body.password,
        chatid : req.body.chatid,
        Maxhrs : req.body.MaxHours
    }
    const myJSON2 = JSON.stringify(myJSON)
    console.log(myJSON)
    console.log(myJSON2)
    var pythonProcess = spawn('python',["./AdminCreateManagerAccountController.py",myJSON2])
    pythonProcess.stdout.on('data',(data)=>{
    req.flash('message17', null);
    var bool = data.toString()
    console.log(bool)
    if (bool.trim() == "Failed")
    {
        req.flash('message17','Unable to create User. Double check your values entered')
        res.redirect('/createmanageraccount')
    }
    else
    {
        req.flash('message17','User Account Created')
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
    req.flash('message', null);
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
    req.flash('message', null);
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
    req.flash('message', null);
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
    req.flash('message', null);
    if (bool.trim() == "Failed")
    {
        req.flash('message','Unable to update Manager Account. Double check your values entered')
        res.redirect('/adminupdatemanageraccount')
    }
    else
    {
        req.flash('message','Manager Account Updated')
        res.redirect('/adminupdatemanageraccount')
    }
})
})

app.get('/adminupdateemployeeaccount', (req,res) =>{
    var pythonProcess = spawn('python',["./grabUserAccountTableColumnsController.py"])
    pythonProcess.stdout.on('data',(data) =>{
        try{
            var myList = JSON.parse(data.toString())
            res.render('AdminUpdateEmployeeAccountGUI',{myList, message: req.flash('message')})
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

app.post('/adminupdateemployeeaccount', (req,res) =>{
    const myJSON = {
        employeeid : req.body.employeeid,
        selectedoption : req.body.selectedoption,
        value : req.body.value
    }
    const myJSON2 = JSON.stringify(myJSON)
    console.log(myJSON2)
    var pythonProcess = spawn('python',["./AdminUpdateEmployeeAccountController.py",myJSON2])
    pythonProcess.stdout.on('data',(data)=>{
    var bool = data.toString()
    console.log(bool)
    req.flash('message', null);
    if (bool.trim() == "Failed")
    {
        req.flash('message','Unable to update Employee Account. Double check your values entered')
        res.redirect('/adminupdateemployeeaccount')
    }
    else
    {
        req.flash('message','Employee Account Updated')
        res.redirect('/adminupdateemployeeaccount')
    }
})
})

app.get('/admindeleteaccountchoose', (req,res) =>{
    res.render('AdminDeleteAccountChoiceGUI')
})

app.get('/admindeleteadminaccount', (req,res) =>{
    res.render('AdminDeleteAdminAccountGUI',{ message: req.flash('message')})
})

app.post('/admindeleteadminaccount', (req,res) =>{
    const myJSON = {
        employeeid : req.body.employeeid
    }
    const myJSON2 = JSON.stringify(myJSON)
    console.log(myJSON2)
    var pythonProcess = spawn('python',["./AdminDeleteAdminAccountController.py",myJSON2])
    pythonProcess.stdout.on('data',(data)=>{
    var bool = data.toString()
    console.log(bool)
    req.flash('message', null);
    if (bool.trim() == "Failed")
    {
        req.flash('message','Unable to delete Admin Account. Double check your values entered')
        res.redirect('/admindeleteadminaccount')
    }
    else
    {
        req.flash('message','Admin Account Deleted')
        res.redirect('/admindeleteadminaccount')
    }
})
})

app.get('/admindeletemanageraccount', (req,res) =>{
    res.render('AdminDeleteManagerAccountGUI',{ message: req.flash('message')})
})

app.post('/admindeletemanageraccount', (req,res) =>{
    const myJSON = {
        employeeid : req.body.employeeid
    }
    const myJSON2 = JSON.stringify(myJSON)
    console.log(myJSON2)
    var pythonProcess = spawn('python',["./AdminDeleteManagerAccountController.py",myJSON2])
    pythonProcess.stdout.on('data',(data)=>{
    var bool = data.toString()
    console.log(bool)
    req.flash('message', null);
    if (bool.trim() == "Failed")
    {
        req.flash('message','Unable to delete Manager Account. Double check your values entered')
        res.redirect('/admindeletemanageraccount')
    }
    else
    {
        req.flash('message','Manager Account Deleted')
        res.redirect('/admindeletemanageraccount')
    }
})
})

app.get('/admindeleteemployeeaccount', (req,res) =>{
    res.render('AdminDeleteEmployeeAccountGUI',{ message: req.flash('message')})
})

app.post('/admindeleteemployeeaccount', (req,res) =>{
    const myJSON = {
        employeeid : req.body.employeeid
    }
    const myJSON2 = JSON.stringify(myJSON)
    console.log(myJSON2)
    var pythonProcess = spawn('python',["./AdminDeleteEmployeeAccountController.py",myJSON2])
    pythonProcess.stdout.on('data',(data)=>{
    var bool = data.toString()
    console.log(bool)
    req.flash('message', null);
    if(bool.trim() == "Reassign")
    {
        req.flash('message','Unable to delete Employee Account. Reassign Shifts to another employee first')
        res.redirect('/admindeleteemployeeaccount')
    }
    else if (bool.trim() == "Failed")
    {
        req.flash('message','Unable to delete Employee Account. Double check your values entered')
        res.redirect('/admindeleteemployeeaccount')
    }
    else
    {
        req.flash('message','Employee Account Deleted')
        res.redirect('/admindeleteemployeeaccount')
    }
})
})

app.get('/admin_reassignshifts', (req,res) =>{
    res.render('AdminReassignShiftsGUI',{ message: req.flash('message17') })
})

app.post('/admin_reassignshifts', (req, res) => {
    const employeeid = req.body.employeeid;
    const myJSON = {
        employeeid: req.body.employeeid
    };
    const myJSON2 = JSON.stringify(myJSON);
    console.log(myJSON2);

    const pythonProcess = spawn('python', ["./AdminViewFutureShiftsController.py", myJSON2]);

    let allData = ""; // Variable to store all data from Python process

    pythonProcess.stdout.on('data', (data) => {
        allData += data.toString(); // Append data received from Python
        console.log(allData)
    });

    pythonProcess.on('close', (code) => {
        req.flash('message17', null);
        try {
            const parsedData = JSON.parse(allData);
            if (parsedData === "No table left") {
                req.flash('message17', 'No Table Left');
                res.render('AdminReassignWorkShiftsTableGUI', { message: req.flash('message17') });
            } else {
                req.flash('message17', 'Tables found');
                res.render('AdminReassignWorkShiftsTableGUI', { results: parsedData, message: req.flash('message17') });
            }
        } catch (error) {
            console.error("Error parsing JSON:", error);
            req.flash('message17', 'Error: Invalid data received');
            res.render('AdminReassignWorkShiftsTableGUI', { message: req.flash('message17') });
        }
    });

    pythonProcess.on('error', (err) => {
        console.error('Failed to start Python process.', err);
        req.flash('message17', 'Error: Failed to start Python process');
        res.render('AdminReassignWorkShiftsTableGUI', { message: req.flash('message17') });
    });
});

app.post('/admin_reassignshiftss', (req,res) =>{
    const button = req.body.buttonid
    const csvArray = button.split(',')
    const jsonObj = {
        id : csvArray[0],
        employeeid: req.body.employeeid
    }
    const jsonObj2 = JSON.stringify(jsonObj)
    console.log(jsonObj2)
    var pythonProcess = spawn('python',["./AdminReassignShiftsController.py",jsonObj2])
    pythonProcess.stdout.on('data',(data)=>{
    req.flash('message4', null);
    var alldata = data.toString().trim()
    console.log(alldata)
    if (alldata == "Success")
    {
        req.flash('message4','Reassigned Successfully')
        res.redirect("/admin_reassignshifts")
        
    }
    else
    {
        req.flash('message4','Unsuccessful')
        res.redirect("/admin_reassignshifts")
    }
})
})

app.get('/admin_view', (req,res) =>{
    res.render('AdminViewChoose')
})

app.get('/admin_view', (req,res) =>{
    res.render('AdminViewChoose')
})

app.get('/adminviewaccountchoose', (req,res) =>{
    res.render('AdminViewChooseAccount')
})

app.get('/adminviewuserprofile', (req,res) =>{
    var pythonProcess = spawn('python',["./AdminViewUserProfileController.py"])
    pythonProcess.stdout.on('data',(data)=>{
    req.flash('message17', null);
    try{
        var alldata = JSON.parse(data.toString())
    }catch(error)
    {
        console.log(alldata)
    }
    if (data.toString().trim() == "No table left")
    {
        req.flash('message17','No Table Left')
        res.render('AdminViewUserProfileGUI',{message: req.flash('message17')})
    }
    else
    {
        req.flash('message17','Tables found')
        res.render('AdminViewUserProfileGUI',({"results": alldata, message: req.flash('message17')}))
    }
}) 
})

app.get('/adminviewadminaccount', (req,res) =>{
    var pythonProcess = spawn('python',["./AdminViewAdminAccountsController.py"])
    pythonProcess.stdout.on('data',(data)=>{
    req.flash('message17', null);
    try{
        var alldata = JSON.parse(data.toString())
    }catch(error)
    {
        console.log(alldata)
    }
    if (data.toString().trim() == "No table left")
    {
        req.flash('message17','No Table Left')
        res.render('AdminViewAdminAccountGUI',{message: req.flash('message17')})
    }
    else
    {
        req.flash('message17','Tables found')
        res.render('AdminViewAdminAccountGUI',({"results": alldata, message: req.flash('message17')}))
    }
})
})

app.get('/adminviewmanageraccount', (req,res) =>{
    var pythonProcess = spawn('python',["./AdminViewManagerAccountsController.py"])
    pythonProcess.stdout.on('data',(data)=>{
    req.flash('message17', null);
    try{
        var alldata = JSON.parse(data.toString())
    }catch(error)
    {
        console.log(alldata)
    }
    if (data.toString().trim() == "No table left")
    {
        req.flash('message17','No Table Left')
        res.render('AdminViewManagerAccountGUI',{message: req.flash('message17')})
    }
    else
    {
        req.flash('message17','Tables found')
        res.render('AdminViewManagerAccountGUI',({"results": alldata, message: req.flash('message17')}))
    }
})
})

app.get('/adminviewemployeeaccount', (req,res) =>{
    var pythonProcess = spawn('python',["./AdminViewEmployeeAccountsController.py"])
    pythonProcess.stdout.on('data',(data)=>{
    req.flash('message17', null);
    try{
        var alldata = JSON.parse(data.toString())
    }catch(error)
    {
        console.log(alldata)
    }
    if (data.toString().trim() == "No table left")
    {
        req.flash('message17','No Table Left')
        res.render('AdminViewEmployeeAccountGUI',{message: req.flash('message17')})
    }
    else
    {
        req.flash('message17','Tables found')
        res.render('AdminViewEmployeeAccountGUI',({"results": alldata, message: req.flash('message17')}))
    }
})
})

app.get('/admin_searchfilter', (req,res) =>{
    res.render('AdminSearchFilterChooseGUI')
})

app.get('/admin_searchaccounts', (req,res) =>{
    res.render('AdminSearchAccountsGUI')
})

app.get('/adminsearchadmin', (req,res) =>{
    var pythonProcess = spawn('python',["./grabUserAccountTableColumnsController.py"])
    pythonProcess.stdout.on('data',(data) =>{
        try{
            var myList = JSON.parse(data.toString())
            res.render('AdminSearchAdminAccountGUI',{myList, message: req.flash('message')})
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

app.post('/adminsearchadmin', (req,res) =>{
    const jsonObj = {
        selectedoption : req.body.selectedoption,
        value : req.body.value
    }
    const jsonObj2 = JSON.stringify(jsonObj)
    var pythonProcess = spawn('python',["./AdminSearchAdminAccountsController.py",jsonObj2])
    pythonProcess.stdout.on('data',(data)=>{
    req.flash('message', null);
    try{
        var alldata = JSON.parse(data.toString())
    }catch(error)
    {
        console.log(alldata)
    }
    
    if (data.toString().trim() == "No table left" || data.toString().trim() == "Failed")
    {
        console.log(data.toString())
        req.flash('message','Failed Search')
        res.redirect('/adminsearchadmin')   
    }
    else
    {
        res.render('AdminSearchAdminTableGUI',{"results": alldata}) 
    }
})
});

app.get('/adminfilteradmin', (req,res) =>{
    var pythonProcess = spawn('python',["./AdminFiltergrabTableColumns.py"])
    pythonProcess.stdout.on('data',(data) =>{
        try{
            var myList = JSON.parse(data.toString())
            res.render('AdminFilterAdminAccountGUI',{myList, message: req.flash('message')})
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

app.post('/adminfilteradmin', (req,res) =>{
    const jsonObj = {
        selectedoption : req.body.selectedoption,
        value : req.body.value
    }
    const jsonObj2 = JSON.stringify(jsonObj)
    var pythonProcess = spawn('python',["./AdminFilterAdminAccountsController.py",jsonObj2])
    pythonProcess.stdout.on('data',(data)=>{
    req.flash('message', null);
    try{
        var alldata = JSON.parse(data.toString())
    }catch(error)
    {
        console.log(alldata)
    }
    
    if (data.toString().trim() == "No table left" || data.toString().trim() == "Failed")
    {
        console.log(data.toString())
        req.flash('message','Failed Search')
        res.redirect('/adminfilteradmin')   
    }
    else
    {
        res.render('AdminFilterAdminTableGUI',{"results": alldata}) 
    }
})
});

app.get('/adminsearchmanager', (req,res) =>{
    var pythonProcess = spawn('python',["./grabUserAccountTableColumnsController.py"])
    pythonProcess.stdout.on('data',(data) =>{
        try{
            var myList = JSON.parse(data.toString())
            res.render('AdminSearchManagerAccountGUI',{myList, message: req.flash('message')})
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

app.post('/adminsearchmanager', (req,res) =>{
    const jsonObj = {
        selectedoption : req.body.selectedoption,
        value : req.body.value
    }
    const jsonObj2 = JSON.stringify(jsonObj)
    var pythonProcess = spawn('python',["./AdminSearchManagerAccountsController.py",jsonObj2])
    pythonProcess.stdout.on('data',(data)=>{
    req.flash('message', null);
    try{
        var alldata = JSON.parse(data.toString())
    }catch(error)
    {
        console.log(alldata)
    }
    
    if (data.toString().trim() == "No table left" || data.toString().trim() == "Failed")
    {
        console.log(data.toString())
        req.flash('message','Failed Search')
        res.redirect('/adminsearchmanager')   
    }
    else
    {
        res.render('AdminSearchManagerTableGUI',{"results": alldata}) 
    }
})
});

app.get('/adminfiltermanager', (req,res) =>{
    var pythonProcess = spawn('python',["./AdminFiltergrabTableColumns.py"])
    pythonProcess.stdout.on('data',(data) =>{
        try{
            var myList = JSON.parse(data.toString())
            res.render('AdminFilterManagerAccountGUI',{myList, message: req.flash('message')})
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

app.post('/adminfiltermanager', (req,res) =>{
    const jsonObj = {
        selectedoption : req.body.selectedoption,
        value : req.body.value
    }
    const jsonObj2 = JSON.stringify(jsonObj)
    var pythonProcess = spawn('python',["./AdminFilterManagerAccountsController.py",jsonObj2])
    pythonProcess.stdout.on('data',(data)=>{
    req.flash('message', null);
    try{
        var alldata = JSON.parse(data.toString())
    }catch(error)
    {
        console.log(alldata)
    }
    
    if (data.toString().trim() == "No table left" || data.toString().trim() == "Failed")
    {
        console.log(data.toString())
        req.flash('message','Failed Search')
        res.redirect('/adminfiltermanager')   
    }
    else
    {
        res.render('AdminFilterManagerTableGUI',{"results": alldata}) 
    }
})
});


app.get('/adminsearchemployee', (req,res) =>{
    var pythonProcess = spawn('python',["./grabUserAccountTableColumnsController.py"])
    pythonProcess.stdout.on('data',(data) =>{
        try{
            var myList = JSON.parse(data.toString())
            res.render('AdminSearchEmployeeAccountGUI',{myList, message: req.flash('message23')})
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

app.post('/adminsearchemployee', (req,res) =>{
    const jsonObj = {
        selectedoption : req.body.selectedoption,
        value : req.body.value
    }
    const jsonObj2 = JSON.stringify(jsonObj)
    var pythonProcess = spawn('python',["./AdminSearchEmployeeAccountsController.py",jsonObj2])
    pythonProcess.stdout.on('data',(data)=>{
    req.flash('message23', null);
    try{
        var alldata = JSON.parse(data.toString())
    }catch(error)
    {
        console.log(alldata)
    }
    
    if (data.toString().trim() == "No table left" || data.toString().trim() == "Failed")
    {
        console.log(data.toString())
        req.flash('message23','Failed Search')
        res.redirect('/adminsearchemployee')   
    }
    else
    {
        res.render('AdminSearchEmployeeTableGUI',{"results": alldata}) 
    }
})
});

app.get('/adminfilteremployee', (req,res) =>{
    var pythonProcess = spawn('python',["./AdminFiltergrabTableColumns.py"])
    pythonProcess.stdout.on('data',(data) =>{
        try{
            var myList = JSON.parse(data.toString())
            res.render('AdminFilterEmployeeAccountGUI',{myList, message: req.flash('message')})
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

app.post('/adminfilteremployee', (req,res) =>{
    const jsonObj = {
        selectedoption : req.body.selectedoption,
        value : req.body.value
    }
    const jsonObj2 = JSON.stringify(jsonObj)
    var pythonProcess = spawn('python',["./AdminFilterManagerAccountsController.py",jsonObj2])
    pythonProcess.stdout.on('data',(data)=>{
    req.flash('message', null);
    try{
        var alldata = JSON.parse(data.toString())
    }catch(error)
    {
        console.log(alldata)
    }
    
    if (data.toString().trim() == "No table left" || data.toString().trim() == "Failed")
    {
        console.log(data.toString())
        req.flash('message','Failed Search')
        res.redirect('/adminfilteremployee')   
    }
    else
    {
        res.render('AdminFilterEmployeeTableGUI',{"results": alldata}) 
    }
})
});


//UpdateManagerAccount
app.get('/updatemanageraccount', (req,res) =>{
    var pythonProcess = spawn('python',["./grabUserAccountTableColumnsController.py"])
    pythonProcess.stdout.on('data',(data) =>{
        try{
            var myList = JSON.parse(data.toString())
            res.render('UpdateManagerAccount',{myList, message: req.flash('message')})
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

app.post('/updatemanageraccount', (req,res) =>{
    const emlpoyeeidentity = req.session.emlpoyeeidentity
    const myJSON = {
        employeeid : emlpoyeeidentity,
        selectedoption : req.body.selectedoption,
        value : req.body.value
    }
    const myJSON2 = JSON.stringify(myJSON)
    console.log(myJSON2)
    var pythonProcess = spawn('python',["./UpdateManagerAccountController.py",myJSON2])
    pythonProcess.stdout.on('data',(data)=>{
    var bool = data.toString()
    console.log(bool)
    req.flash('message', null);
    if (bool.trim() == "Failed")
    {
        req.flash('message','Unable to update Employee Account. Double check your values entered')
        res.redirect('/UpdateManagerAccount')
    }
    else
    {
        req.flash('message','Employee Account Updated')
        res.redirect('/UpdateManagerAccount')
    }
})
})


app.get('/manager_createws', (req, res) => {
    const countrycode = "SG"
    const holidays = new Holiday(countrycode);

    // Get the current year
    const currentYear = new Date().getFullYear();

    // Get the current month
    const currentMonth = new Date().getMonth() + 1; // Note: month is 0-indexed

    // Fetch holidays for the current month
    const currentMonthHolidays = holidays.getHolidays(currentYear, currentMonth)
    .filter(holiday => holiday.start.getMonth() === currentMonth - 1);
    console.log(currentMonthHolidays)
        // Render the UpdateManagerAccount.ejs page
    res.render('CreateWorkShift',{message: req.flash('message99'), holidays: currentMonthHolidays});
});

app.post('/manager_createws', (req, res) => {
    const { date, shift, start, end } = req.body;
    const dataToSend = JSON.stringify({ date, shift, start, end });
    
    // Spawn Python process and pass JSON data as argument
    const pythonProcess = spawn('python', ['./CreatewsController.py', dataToSend]);
    
    pythonProcess.stdout.on('data', (data) => {
        req.flash('message99', null);
        const result = data.toString().trim();
        if (result === 'Failed') {
            req.flash('message99','Failed to Create Workshift')
            res.redirect('/manager_createws')
        } else {
            req.flash('message99','Workshift Created')
            res.redirect('/manager_createws')
        }
    });
  
    pythonProcess.stderr.on('data', (data) => {
      console.error('Error from Python Script:', data.toString());
      res.status(500).send('Error from python script');
    });
  });

  app.get('/manager_createwsmutliple', (req, res) => {
    const countrycode = "SG"
    const holidays = new Holiday(countrycode);

    // Get the current year
    const currentYear = new Date().getFullYear();

    // Get the current month
    const currentMonth = new Date().getMonth() + 1; // Note: month is 0-indexed

    // Fetch holidays for the current month
    const currentMonthHolidays = holidays.getHolidays(currentYear, currentMonth)
    .filter(holiday => holiday.start.getMonth() === currentMonth - 1);
    console.log(currentMonthHolidays)
        // Render the UpdateManagerAccount.ejs page
    res.render('CreateWorkShiftMultipleGUI',{message: req.flash('message99'), holidays: currentMonthHolidays});
});

app.post('/manager_createwsmutliple', (req, res) => {
    const { startdate,enddate, shift, start, end } = req.body;
    const dataToSend = JSON.stringify({ startdate,enddate, shift, start, end });
    console.log(dataToSend)
    // Spawn Python process and pass JSON data as argument
    const pythonProcess = spawn('python', ['./CreateWorkShiftMultipleController.py', dataToSend]);
    
    pythonProcess.stdout.on('data', (data) => {
        req.flash('message99', null);
        const result = data.toString().trim();
        console.log(result)
        if (result === 'Failed') {
            req.flash('message99','Failed to Create Workshifts')
            res.redirect('/manager_createwsmutliple')
        } else {
            req.flash('message99','Workshifts Created')
            res.redirect('/manager_createwsmutliple')
        }
    });
  
    pythonProcess.stderr.on('data', (data) => {
      console.error('Error from Python Script:', data.toString());
      res.status(500).send('Error from python script');
    });
  });

app.get('/managerfilterpreference', (req,res) =>{
    var pythonProcess = spawn('python',["./grabShiftPreferenceController.py"])
    pythonProcess.stdout.on('data',(data) =>{
        try{
            var myList = JSON.parse(data.toString())
            var shiftPrefList = JSON.parse(myList.shift_pref);
            var dayList = JSON.parse(myList.day);
            console.log(myList)
            console.log(shiftPrefList)
            console.log(dayList)
            res.render('ManagerFilterPreferenceGUI',{shiftPrefList,dayList, message: req.flash('message23')})
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

app.post('/managerfilterpreference', (req,res) =>{
    const jsonObj = {
        shiftpref : req.body.selectedoption,
        day : req.body.selectedoption2,
    }
    console.log(jsonObj)
    const jsonObj2 = JSON.stringify(jsonObj)
    var pythonProcess = spawn('python',["./ManagerFilterShiftPreferenceController.py",jsonObj2])
    pythonProcess.stdout.on('data',(data)=>{
    req.flash('message23', null);
    try{
        var alldata = JSON.parse(data.toString())
    }catch(error)
    {
        console.log(alldata)
    }
    
    if (data.toString().trim() == "No table left" || data.toString().trim() == "Failed")
    {
        console.log(data.toString())
        req.flash('message23','Failed Search')
        res.redirect('/managerfilterpreference')   
    }
    else
    {
        res.render('ManagerFilterShiftPrefTableGUI',{"results": alldata}) 
    }
})
});

app.get('/manager_viewshiftpref', (req,res) =>{
    var pythonProcess = spawn('python',["./ManagerViewShiftPreferenceController.py"])
    pythonProcess.stdout.on('data',(data)=>{
    req.flash('message17', null);
    try{
        var alldata = JSON.parse(data.toString())
    }catch(error)
    {
        console.log(alldata)
    }
    if (data.toString().trim() == "No table left")
    {
        req.flash('message17','No Table Left')
        res.render('ManagerViewShiftPrefGUI',{message: req.flash('message17')})
    }
    else
    {
        req.flash('message17','Tables found')
        res.render('ManagerViewShiftPrefGUI',({"results": alldata, message: req.flash('message17')}))
    }
})
})

app.get('/managerviewemployeeaccounts', (req,res) =>{
    var pythonProcess = spawn('python',["./ManagerViewEmployeeAccountsController.py"])
    pythonProcess.stdout.on('data',(data)=>{
    req.flash('message17', null);
    try{
        var alldata = JSON.parse(data.toString())
    }catch(error)
    {
        console.log(alldata)
    }
    if (data.toString().trim() == "No table left")
    {
        req.flash('message17','No Table Left')
        res.render('ManagerViewEmployeeAccountsGUI.ejs',{message: req.flash('message17')})
    }
    else
    {
        req.flash('message17','Tables found')
        res.render('ManagerViewEmployeeAccountsGUI.ejs',({"results": alldata, message: req.flash('message17')}))
    }
})
})

app.get('/managerfilteremployeeaccounts', (req,res) =>{
    var pythonProcess = spawn('python',["./ManagerFiltergrabTableColumns.py"])
    pythonProcess.stdout.on('data',(data) =>{
        try{
            var myList = JSON.parse(data.toString())
            res.render('ManagerFilterEmployeeAccountGUI',{myList, message: req.flash('message23')})
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

app.post('/managerfilteremployeeaccounts', (req,res) =>{
    const jsonObj = {
        selectedoption : req.body.selectedoption,
        value : req.body.value
    }
    const jsonObj2 = JSON.stringify(jsonObj)
    var pythonProcess = spawn('python',["./ManagerFilterEmployeeController.py",jsonObj2])
    pythonProcess.stdout.on('data',(data)=>{
    req.flash('message23', null);    
    try{
        var alldata = JSON.parse(data.toString())
    }catch(error)
    {
        console.log(alldata)
    }
    
    if (data.toString().trim() == "No table left" || data.toString().trim() == "Failed")
    {
        console.log(data.toString())
        req.flash('message23','Failed Search')
        res.redirect('/managerfilteremployeeaccounts')   
    }
    else
    {
        res.render('ManagerFilterEmployeeAccountsTableGUI',{"results": alldata}) 
    }
})
});

app.get('/managersearchemployeeaccounts', (req,res) =>{
    var pythonProcess = spawn('python',["./ManagerFiltergrabTableColumns.py"])
    pythonProcess.stdout.on('data',(data) =>{
        try{
            var myList = JSON.parse(data.toString())
            res.render('ManagerSearchEmployeeAccountGUI',{myList, message: req.flash('message')})
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

app.post('/managersearchemployeeaccounts', (req,res) =>{
    const jsonObj = {
        selectedoption : req.body.selectedoption,
        value : req.body.value
    }
    const jsonObj2 = JSON.stringify(jsonObj)
    var pythonProcess = spawn('python',["./ManagerSearchEmployeeController.py",jsonObj2])
    pythonProcess.stdout.on('data',(data)=>{
    req.flash('message', null);
    try{
        var alldata = JSON.parse(data.toString())
    }catch(error)
    {
        console.log(alldata)
    }
    
    if (data.toString().trim() == "No table left" || data.toString().trim() == "Failed")
    {
        console.log(data.toString())
        req.flash('message','Failed Search')
        res.redirect('/managersearchemployeeaccounts')   
    }
    else
    {
        res.render('ManagerSearchEmployeeAccountsTableGUI',{"results": alldata}) 
    }
})
});


app.get('/manager_viewws', (req, res) => {
    var pythonProcess = spawn('python', ["./ManagerViewWorkshiftsController.py"]);
    let alldata = "";
    pythonProcess.stdout.on('data', (data) => {
        alldata += data.toString();
    });
    pythonProcess.stdout.on('end', () => {
        req.flash('message17', null);
        try {
            const jsonData = JSON.parse(alldata.trim());
            if (jsonData === "No table left") {
                req.flash('message17', 'No Table Left');
                res.render('ManagerViewWorkshiftssGUI', { message: req.flash('message17') });
            } else {
                req.flash('message17', 'Tables found');
                res.render('ManagerViewWorkshiftssGUI', { results: jsonData, message: req.flash('message17') });
            }
        } catch (error) {
            console.error("Error parsing JSON:", error);
            req.flash('message17', 'Error retrieving data');
            res.render('ManagerViewWorkshiftssGUI', { message: req.flash('message17') });
        }
    });
    pythonProcess.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
    });
});



app.get('/manager_deletews', (req, res) => {
    var pythonProcess = spawn('python', ["./ManagerViewWorkshiftsController.py"]);
    let alldata = "";
    pythonProcess.stdout.on('data', (data) => {
        alldata += data.toString();
    });
    pythonProcess.stdout.on('end', () => {
        try {
            const jsonData = JSON.parse(alldata.trim());
            if (jsonData === "No table left") {
                req.flash('message17', 'No Table Left');
                res.render('DeleteWsGUI', { message: req.flash('message17') });
            } else {
                req.flash('message17', 'Tables found');
                res.render('DeleteWsGUI', { results: jsonData, message: req.flash('message17') });
            }
        } catch (error) {
            console.error("Error parsing JSON:", error);
            req.flash('message17', 'Error retrieving data');
            res.render('DeleteWsGUI', { message: req.flash('message17') });
        }
    });
    pythonProcess.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
    });
});


app.post('/manager_deletews', (req,res) =>{
    const button = req.body.buttonid
    const csvArray = button.split(',')
    const jsonObj = {
        id : csvArray[0]
    }
    const jsonObj2 = JSON.stringify(jsonObj)
    console.log(jsonObj2)
    var pythonProcess = spawn('python',["./DeletewsController.py",jsonObj2])
    pythonProcess.stdout.on('data',(data)=>{
    req.flash('message17', null);
    var alldata = data.toString().trim()
    console.log(alldata)
    if (alldata == "Success")
    {
        req.flash('message17','Deleted Successfully')
        res.redirect('/manager_deletews')
        
    }
    else
    {
        req.flash('message17','Unsuccessful')
        res.redirect('/manager_deletews') 
    }
})
})

app.get('/managerapproveleave', (req, res) => {
    var pythonProcess = spawn('python', ["./ManagerViewPendingLeaveController.py"]);
    let alldata = "";
    pythonProcess.stdout.on('data', (data) => {
        alldata += data.toString();
    });
    pythonProcess.stdout.on('end', () => {
        req.flash('message17', null);
        try {
            const jsonData = JSON.parse(alldata.trim());
            if (jsonData === "No table left") {
                req.flash('message17', 'No Table Left');
                res.render('ManagerApproveLeaveGUI', { message: req.flash('message17') });
            } else {
                req.flash('message17', 'Tables found');
                res.render('ManagerApproveLeaveGUI', { results: jsonData, message: req.flash('message17') });
            }
        } catch (error) {
            console.error("Error parsing JSON:", error);
            req.flash('message17', 'Error retrieving data');
            res.render('ManagerApproveLeaveGUI', { message: req.flash('message17') });
        }
    });
    pythonProcess.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
    });
});

app.post('/managerapproveleave', (req,res) =>{
    const button = req.body.buttonid
    const csvArray = button.split(',')
    const jsonObj = {
        id : csvArray[0]
    }
    const jsonObj2 = JSON.stringify(jsonObj)
    console.log(jsonObj2)
    var pythonProcess = spawn('python',["./ManagerApproveLeaveController.py",jsonObj2])
    pythonProcess.stdout.on('data',(data)=>{
    req.flash('message17', null);
    var alldata = data.toString().trim()
    console.log(alldata)
    if (alldata == "Success")
    {
        req.flash('message17','Approved Successfully')
        res.redirect('/managerapproveleave')
        
    }
    else
    {
        req.flash('message17','Unsuccessful')
        res.redirect('/managerapproveleave') 
    }
})
})

app.get('/managerrejectleave', (req, res) => {
    var pythonProcess = spawn('python', ["./ManagerViewPendingLeaveController.py"]);
    let alldata = "";
    pythonProcess.stdout.on('data', (data) => {
        alldata += data.toString();
    });
    pythonProcess.stdout.on('end', () => {
        req.flash('message17', null);
        try {
            const jsonData = JSON.parse(alldata.trim());
            if (jsonData === "No table left") {
                req.flash('message17', 'No Table Left');
                res.render('ManagerRejectLeaveGUI', { message: req.flash('message17') });
            } else {
                req.flash('message17', 'Tables found');
                res.render('ManagerRejectLeaveGUI', { results: jsonData, message: req.flash('message17') });
            }
        } catch (error) {
            console.error("Error parsing JSON:", error);
            req.flash('message17', 'Error retrieving data');
            res.render('ManagerRejectLeaveGUI', { message: req.flash('message17') });
        }
    });
    pythonProcess.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
    });
});

app.post('/managerrejectleave', (req,res) =>{
    const button = req.body.buttonid
    const csvArray = button.split(',')
    const reason = req.body[`reason${csvArray[0]}`];
    console.log(reason)
    const jsonObj = {
        id : csvArray[0],
        reason: reason
    }
    const jsonObj2 = JSON.stringify(jsonObj)
    console.log(jsonObj2)
    var pythonProcess = spawn('python',["./ManagerRejectLeaveController.py",jsonObj2])
    pythonProcess.stdout.on('data',(data)=>{
    req.flash('message17', null);
    var alldata = data.toString().trim()
    console.log(alldata)
    if (alldata == "Success")
    {
        req.flash('message17','Approved Successfully')
        res.redirect('/managerrejectleave')
        
    }
    else
    {
        req.flash('message17','Unsuccessful')
        res.redirect('/managerrejectleave') 
    }
})
})


app.get('/manager_viewempleave', (req, res) => {
    var pythonProcess = spawn('python', ["./ManagerViewLeaveController.py"]);
    let alldata = "";
    pythonProcess.stdout.on('data', (data) => {
        alldata += data.toString();
    });
    pythonProcess.stdout.on('end', () => {
        req.flash('message17', null);
        try {
            const jsonData = JSON.parse(alldata.trim());
            if (jsonData === "No table left") {
                req.flash('message17', 'No Table Left');
                res.render('ManagerViewLeavesGUI', { message: req.flash('message17') });
            } else {
                req.flash('message17', 'Tables found');
                res.render('ManagerViewLeavesGUI', { results: jsonData, message: req.flash('message17') });
            }
        } catch (error) {
            console.error("Error parsing JSON:", error);
            req.flash('message17', 'Error retrieving data');
            res.render('ManagerViewLeavesGUI', { message: req.flash('message17') });
        }
    });
    pythonProcess.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
    });
});

app.get('/manager_viewattendance', (req, res) => {
    var pythonProcess = spawn('python', ["./ManagerViewAttendanceController.py"]);
    let alldata = "";
    pythonProcess.stdout.on('data', (data) => {
        alldata += data.toString();
    });
    pythonProcess.stdout.on('end', () => {
        req.flash('message17', null);
        try {
            const jsonData = JSON.parse(alldata.trim());
            if (jsonData === "No table left") {
                req.flash('message17', 'No Table Left');
                res.render('ManagerViewAttendanceGUI', { message: req.flash('message17') });
            } else {
                req.flash('message17', 'Tables found');
                res.render('ManagerViewAttendanceGUI', { results: jsonData, message: req.flash('message17') });
            }
        } catch (error) {
            console.error("Error parsing JSON:", error);
            req.flash('message17', 'Error retrieving data');
            res.render('ManagerViewAttendanceGUI', { message: req.flash('message17') });
        }
    });
    pythonProcess.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
    });
});

app.get('/managerfilterattendance', (req,res) =>{
    var pythonProcess = spawn('python',["./grabAttendanceTableColumnsController.py"])
    pythonProcess.stdout.on('data',(data) =>{
        try{
            var myList = JSON.parse(data.toString())
            res.render('ManagerFilterAttendanceGUI',{myList, message: req.flash('message')})
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

app.post('/managerfilterattendance', (req,res) =>{
    const jsonObj = {
        selectedoption : req.body.selectedoption,
        value : req.body.value
    }
    const jsonObj2 = JSON.stringify(jsonObj)
    var pythonProcess = spawn('python',["./ManagerFilterAttendnaceController.py",jsonObj2])
    pythonProcess.stdout.on('data',(data)=>{
        req.flash('message', null);
    try{
        var alldata = JSON.parse(data.toString())
    }catch(error)
    {
        console.log(alldata)
    }
    
    if (data.toString().trim() == "No table left" || data.toString().trim() == "Failed")
    {
        console.log(data.toString())
        req.flash('message','Failed Search')
        res.redirect('/managerfilterattendance')   
    }
    else
    {
        res.render('ManagerFilterAttendanceTableGUI',{"results": alldata}) 
    }
})
});

app.get('/managermanualassignemployees', (req,res) =>{
    var pythonProcess = spawn('python',["./grabShiftPreferenceController.py"])
    pythonProcess.stdout.on('data',(data) =>{
        try{
            var myList = JSON.parse(data.toString())
            var shiftPrefList = JSON.parse(myList.shift_pref);
            var dayList = JSON.parse(myList.day);
            console.log(myList)
            console.log(shiftPrefList)
            console.log(dayList)
            var myList = JSON.parse(data.toString())
            res.render('ManagerManualAssignEmployeesGUI',{shiftPrefList, message4: req.flash('message4')})
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

app.post('/managermanualassignemployees', (req, res) => {
    const { employeeid, date, selectedoption } = req.body;
    const dataToSend = JSON.stringify({ employeeid, date, selectedoption });
    
    // Spawn Python process and pass JSON data as argument
    const pythonProcess = spawn('python', ['./ManagerManualAssignEmployeesController.py', dataToSend])
    
    pythonProcess.stdout.on('data', (data) => {
        req.flash('message4', null);
      const result = data.toString().trim()
      if (result === 'Failed') {
        res.status(500).send('Unable to Assign workshift. Double check your values entered')
      } else {
        console.log(result)
        req.flash('message4','Assigned Successfully')
        res.redirect('/managermanualassignemployees')
      }
    });
  
    pythonProcess.stderr.on('data', (data) => {
      console.error('Error from Python Script:', data.toString())
      res.status(500).send('Error from python script')
    });
});

// Create Employee leave route
app.get('/employee_createLeave', (req,res) =>{
    res.render('EmployeeCreateLeave',{message: req.flash('message')});
})

app.post('/employee_createLeave', (req, res) => {
    const employeeId = req.session.emlpoyeeidentity
    // const myJSON = {
    //     employeeId : emlpoyeeidentity,
    //     value : req.body.value
    // }
    // const myJSON2 = JSON.stringify(myJSON)
    const { date, leavetype } = req.body;
    const dataToSend = JSON.stringify({ employeeId, date, leavetype });
    console.log("Employee identity: " + employeeId)
    console.log(dataToSend)
    // Spawn Python process and pass JSON data as argument
    const pythonProcess = spawn('python', ['./CreateEmployeeLeaveController.py', dataToSend]);
    
    pythonProcess.stdout.on('data', (data) => {
    req.flash('message', null);
      const result = data.toString().trim();
      if (result === 'Failed EmployeeLeaveClass') {
        req.flash('message','Leave created successfully')
        res.redirect('/employee_createLeave')
      } else {
        req.flash('message','Leave created successfully')
        res.redirect('/employee_createLeave')
      }
    });
  
    pythonProcess.stderr.on('data', (data) => {
      console.error('Error from Python Script:', data.toString())
      res.status(500).send('Error from python script')
    });
});

app.get('/employee_clockinout', (req,res) =>{
    res.render('EmployeeClockinClockOutGUI')
})

app.get('/employeeclockin', (req,res) =>{
    process.env.TZ = 'Asia/Singapore';
    const currentDate = new Date().toLocaleDateString()
    const currentTime = new Date().toLocaleTimeString()
    console.log(currentTime)
    res.render('EmployeeClockInGUI', { currentDate, currentTime, message6: req.flash('message6') })
})

app.post('/employeeclockin', (req, res) => {
    // Get current date and time
    process.env.TZ = 'Asia/Singapore';
    ssn = req.session
    employeeid = req.session.emlpoyeeidentity
    const currentDate = new Date().toLocaleDateString()
    const currentTime = new Date().toLocaleTimeString()
    const clockInTime = new Date().toLocaleString()
    console.log(currentDate)
    console.log(currentTime)
    const dataToSend = JSON.stringify({ employeeid, currentDate, currentTime });

    // Send the current time as a response
    const pythonProcess = spawn('python', ['./EmployeeClockInController.py', dataToSend]);

    let outputData = '';

    pythonProcess.stdout.on('data', (data) => {
        outputData += data.toString();
    });

    pythonProcess.on('close', (code) => {
        req.flash('message6', null);
        if (code === 0) {
            console.log(outputData.trim())
            if (outputData.trim() === '') {
                req.flash('message6', 'Clocked In At: ' + clockInTime)
                res.redirect(`employeeclockin`);
            } else {
                req.flash('message6', 'Check that you are assigned to the correct shift or you have clock out of all shifts.')
                res.redirect(`employeeclockin`);
            }
        } else {
            console.error('Python process exited with code:', code);
            res.redirect(`employeeclockin?error=Error from python script`);
        }
    });

    pythonProcess.stderr.on('data', (data) => {
        console.error('Error from Python Script:', data.toString());
        res.redirect(`employeeclockin?error=Error from python script`);
    });
});

app.get('/employeeclockout', (req,res) =>{
    process.env.TZ = 'Asia/Singapore';
    const currentDate = new Date().toLocaleDateString()
    const currentTime = new Date().toLocaleTimeString()
    console.log(currentTime)
    res.render('EmployeeClockOutGUI', { currentDate, currentTime, message5: req.flash('message5') })
})

app.post('/employeeclockout', (req, res) => {
    process.env.TZ = 'Asia/Singapore';
    // Get current date and time
    ssn = req.session
    employeeid = req.session.emlpoyeeidentity
    const currentTime = new Date().toLocaleTimeString()
    const clockInTime = new Date().toLocaleString()
    console.log(currentTime)
    const dataToSend = JSON.stringify({ employeeid, currentTime });

    // Send the current time as a response
    const pythonProcess = spawn('python', ['./EmployeeClockOutController.py', dataToSend]);

    let outputData = '';

    pythonProcess.stdout.on('data', (data) => {
        outputData += data.toString();
    });

    pythonProcess.on('close', (code) => {
        req.flash('message5', null);
        if (code === 0) {
            console.log(outputData.trim())
            if (outputData.trim() === 'Clock-out time updated successfully.') {
                req.flash('message5', 'Clocked Out At: ' + clockInTime)
                res.redirect(`employeeclockout`);
            } else {
                req.flash('message5', 'Check That you have clocked in before.')
                res.redirect(`employeeclockout`);
            }
        } else {
            console.error('Python process exited with code:', code);
            res.redirect(`employeeclockout?error=Error from python script`);
        }
    });

    pythonProcess.stderr.on('data', (data) => {
        console.error('Error from Python Script:', data.toString());
        res.redirect(`employeeclockout?error=Error from python script`);
    });
});

app.get('/employee_viewall', (req,res) =>{
    res.render('EmployeeViewChoose')
})

app.get('/employee_viewaccount', (req, res) => {
    const employeeId = req.session.emlpoyeeidentity;
    const dataToSend = JSON.stringify({ employeeId });
    var pythonProcess = spawn('python', ["./EmployeeViewAccountController.py", dataToSend]);
    console.log(dataToSend);
    pythonProcess.stdout.on('data', (data) => {
        req.flash('message17', null);
        try {
            var alldata = JSON.parse(data.toString());
            console.log(alldata);
        } catch (error) {
            console.log(alldata);
        }
        if (data.toString().trim() == "No table left") {
            req.flash('message17', 'No Table Left');
            res.render('EmployeeViewAccount', { message: req.flash('message17') });
        } else {
            req.flash('message17', 'Tables found');
            res.render('EmployeeViewAccount', { alldata: alldata, message: req.flash('message17') });
        }
    });
});


app.get('/manager_filterws', (req,res) =>{
    var pythonProcess = spawn('python',["./grabworkshiftsTableColumnsController.py"])
    pythonProcess.stdout.on('data',(data) =>{
        try{
            var myList = JSON.parse(data.toString())
            res.render('FilterWsGUI',{myList, message: req.flash('message')})
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

app.post('/manager_filterws', (req,res) =>{
    const jsonObj = {
        selectedoption : req.body.selectedoption,
        value : req.body.value
    }
    const jsonObj2 = JSON.stringify(jsonObj)
    var pythonProcess = spawn('python',["./FilterwsController.py",jsonObj2])
    pythonProcess.stdout.on('data',(data)=>{
        req.flash('message', null);
    try{
        var alldata = JSON.parse(data.toString())
    }catch(error)
    {
        console.log(alldata)
    }
    
    if (data.toString().trim() == "No table left" || data.toString().trim() == "Failed")
    {
        console.log(data.toString())
        req.flash('message','Failed Search')
        res.redirect('/manager_filterws')   
    }
    else
    {
        res.render('ManagerFilterWorkShiftTable',{"results": alldata}) 
    }
})
});

//Update workshift
app.get('/manager_updatews', (req,res) =>{
    var pythonProcess = spawn('python',["./grabworkshiftsTableColumnsController.py"])
    pythonProcess.stdout.on('data',(data) =>{
        try{
            var myList = JSON.parse(data.toString())
            res.render('UpdateWsGUI',{myList, message: req.flash('message')})
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

app.post('/manager_updatews', (req, res) => {
    const { id, selectedoption, value } = req.body;
    const myJSON = {
        id: id,
        selectedoption: selectedoption,
        value: value
    };
    const myJSON2 = JSON.stringify(myJSON);
    const pythonProcess = spawn('python', ["./UpdatewsController.py", myJSON2]);

    pythonProcess.stdout.on('data', (data) => { 
        req.flash('message', null);
        const result = data.toString().trim();        
        // Check the result and respond accordingly
        if (result === "Failed") {
            req.flash('message', 'Unable to update WorkShift. Double check your values entered');
        } else {
            req.flash('message', 'WorkShift Updated');
        }      
        // Redirect back to the same page
        res.redirect('/manager_updatews');
    });

    // Handle errors from the Python process
    pythonProcess.stderr.on('data', (data) => {
        console.error(`Error from Python script: ${data}`);
        req.flash('message', 'Error updating WorkShift');
        res.redirect('/manager_updatews');
    });
});

app.get('/managercreateemppref', (req,res) =>{
    var pythonProcess = spawn('python',["./grabShiftPreferenceController.py"])
    pythonProcess.stdout.on('data',(data) =>{
        try{
            var myList = JSON.parse(data.toString())
            var shiftPrefList = JSON.parse(myList.shift_pref);
            var dayList = JSON.parse(myList.day);
            console.log(myList)
            console.log(shiftPrefList)
            console.log(dayList)
            res.render('ManagerCreateEmpPrefGUI',{shiftPrefList ,days: ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'],message:req.flash('message')})
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

app.post('/managercreateemppref', (req, res) => {
    const { employeeid } = req.body;
    const schedule = {};
    // Loop through each key in req.body and extract schedule data
    for (const key in req.body) {
        if (key.startsWith('schedule')) {
            const matches = key.match(/schedule\[(.*?)\]\[(.*?)\]/);
            if (matches !== null) { // Check if matches is not null
                const day = matches[1];
                const type = matches[2];
    
                if (!schedule[day]) {
                    schedule[day] = {};
                }
    
                schedule[day][type] = req.body[key];
            } else {
                console.error('Key ',{key},' does not match the expected pattern');
            }
        }
    }
    // Convert schedule and employeeid to JSON strings
    const scheduleJSON = JSON.stringify(schedule);
    const employeeidJSON = JSON.stringify(employeeid);
    const pythonProcess = spawn('python', ["./ManagerCreateEmployeePreference.py", scheduleJSON,employeeidJSON]);
    console.log(scheduleJSON)
    pythonProcess.stdout.on('data', (data) => { 
        req.flash('message', null);
        const result = data.toString().trim();        
        // Check the result and respond accordingly
        if (result === "Failed") {
            req.flash('message', 'Unable to Create Preference. Double check your values entered');
        } else {
            req.flash('message', 'Preference Created');
        }      
        // Redirect back to the same page
        res.redirect('/managercreateemppref');
    });

    // Handle errors from the Python process
    pythonProcess.stderr.on('data', (data) => {
        console.error(`Error from Python script: ${data}`);
        req.flash('message', 'Error updating WorkShift');
        res.redirect('/managercreateemppref');
    });
});

app.get('/managerautoassignemp', (req,res) =>{
    res.render('ManagerAutoAssignEmployeesGUI', { message: req.flash('message23') })
})

app.post('/managerautoassignemp', (req, res) => {
    // Prepare JSON object to send to Python script
    const jsonObj = {
        start: req.body.start,
        end: req.body.end,
        numberofemployees: req.body.number
    }
    // Convert JSON object to string
    const jsonObjStr = JSON.stringify(jsonObj);
    
    // Spawn a Python process and pass the JSON string as argument
    const pythonProcess = spawn('python', ['./ManagerAutoAssignEmployeesController.py', jsonObjStr]);

    let assignedEmployees = [];
    let unassignedShifts = [];

    // Listen for stdout data from the Python process
    pythonProcess.stdout.on('data', (data) => {
        req.flash('message23', null);
        try {
            // Parse the JSON data received from Python
            alldata = JSON.parse(data.toString())
            console.log(alldata)
            // Split the data into assigned employees and unassigned shifts
            assignedEmployees = alldata.assigned_employees;
            unassignedShifts = alldata.unassigned_shifts;

            // Render the page with the data received from Python
            res.render('ManagerAutoAssignTableGUI', {
                "assignedEmployees": assignedEmployees,
                "unassignedShifts": unassignedShifts
            });
        } catch (error) {
            console.error('Error parsing JSON data:', error);
            // Redirect to a failure page if there's an error
            req.flash('message23', 'Failed');
            res.redirect('/managerautoassignemp');
        }
    });

    // Listen for any errors from the Python process
    pythonProcess.stderr.on('data', (data) => {
        console.error('Error from Python script:', data.toString());
        // Redirect to a failure page if there's an error
        req.flash('message23', 'Failed');
        res.redirect('/managerautoassignemp');
    });
});

app.get('/employee_viewpasthistory', (req, res) => {
    const employeeId = req.session.emlpoyeeidentity;
    const dataToSend = JSON.stringify({ employeeId });
    var pythonProcess = spawn('python', ["./EmployeeViewPastWorkHistoryController.py", dataToSend]);
    console.log(dataToSend);
    pythonProcess.stdout.on('data', (data) => {
        req.flash('message17', null);
        try {
            var alldata = JSON.parse(data.toString());
            console.log(alldata);
        } catch (error) {
            console.log(alldata);
        }
        if (data.toString().trim() == "No table left") {
            req.flash('message17', 'No Table Left');
            res.render('EmployeeViewPastWorkHistory', { message: req.flash('message17') });
        } else {
            req.flash('message17', 'Tables found');
            res.render('EmployeeViewPastWorkHistory', { alldata: alldata, message: req.flash('message17') });
        }
    });
});

app.get('/employee_viewnotification', (req, res) => {
    const employeeid = req.session.emlpoyeeidentity;
    const dataToSend = JSON.stringify({ employeeid });
    var pythonProcess = spawn('python', ["./EmployeeViewNotificationController.py", dataToSend]);
    console.log(dataToSend);
    pythonProcess.stdout.on('data', (data) => {
        req.flash('message17', null);
        try {
            var alldata = JSON.parse(data.toString());
            console.log(alldata);
        } catch (error) {
            console.log(alldata);
        }
        if (data.toString().trim() == "Failed") {
            req.flash('message17', 'No Table Left');
            res.render('EmployeeViewNotificationGUI', { message: req.flash('message17') });
        } else {
            req.flash('message17', 'Tables found');
            res.render('EmployeeViewNotificationGUI', { alldata: alldata, message: req.flash('message17') });
        }
    });
});

app.get('/employeeclockinQR', (req, res) => {
    process.env.TZ = 'Asia/Singapore';
    const currentDate = new Date().toLocaleDateString()
    const currentTime = new Date().toLocaleTimeString()
    res.render('ClockInQrCodeGUI',{ currentDate, currentTime, message6: req.flash('message6')});
});

app.post('/employeeclockinQR', (req, res) => {
    process.env.TZ = 'Asia/Singapore';
    // Get current date and time
    const currentDate = new Date().toLocaleDateString()
    const currentTime = new Date().toLocaleTimeString()
    const clockInTime = new Date().toLocaleString()
    const employeeid = req.body.employeeId
    const dataToSend = JSON.stringify({ employeeid, currentDate, currentTime });

    // Send the current time as a response
    const pythonProcess = spawn('python', ['./EmployeeClockInController.py', dataToSend]);

    let outputData = '';

    pythonProcess.stdout.on('data', (data) => {
        outputData += data.toString();
    });

    pythonProcess.on('close', (code) => {
        req.flash('message6', null);
        if (code === 0) {
            console.log(outputData.trim())
            if (outputData.trim() === '') {
                req.flash('message6', 'Clocked In At: ' + clockInTime)
                res.redirect(`employeeclockinQR`);
            } else {
                req.flash('message6', 'Check that you are assigned to the correct shift or you have clock out of all shifts.')
                res.redirect(`employeeclockinQR`);
            }
        } else {
            console.error('Python process exited with code:', code);
            res.redirect(`employeeclockinQR?error=Error from python script`);
        }
    });

    pythonProcess.stderr.on('data', (data) => {
        console.error('Error from Python Script:', data.toString());
        res.redirect(`employeeclockinQR?error=Error from python script`);
    });
    
});


app.get('/employeeclockoutQR', (req,res) =>{
    process.env.TZ = 'Asia/Singapore';
    const currentDate = new Date().toLocaleDateString()
    const currentTime = new Date().toLocaleTimeString()
    console.log(currentTime)
    res.render('ClockOutQrCodeGUI', { currentDate, currentTime, message5: req.flash('message5') })
})

app.post('/employeeclockoutQR', (req, res) => {
    process.env.TZ = 'Asia/Singapore';
    // Get current date and time
    const currentTime = new Date().toLocaleTimeString()
    const clockInTime = new Date().toLocaleString()
    console.log(currentTime)
    const employeeid = req.body.employeeId
    const dataToSend = JSON.stringify({ employeeid, currentTime });

    // Send the current time as a response
    const pythonProcess = spawn('python', ['./EmployeeClockOutController.py', dataToSend]);

    let outputData = '';

    pythonProcess.stdout.on('data', (data) => {
        outputData += data.toString();
    });

    pythonProcess.on('close', (code) => {
        req.flash('message5', null);
        if (code === 0) {
            console.log(outputData.trim())
            if (outputData.trim() === 'Clock-out time updated successfully.') {
                req.flash('message5', 'Clocked Out At: ' + clockInTime)
                res.redirect(`employeeclockoutQR`);
            } else {
                req.flash('message5', 'Check That you have clocked in before.')
                res.redirect(`employeeclockoutQR`);
            }
        } else {
            console.error('Python process exited with code:', code);
            res.redirect(`employeeclockoutQR?error=Error from python script`);
        }
    });

    pythonProcess.stderr.on('data', (data) => {
        console.error('Error from Python Script:', data.toString());
        res.redirect(`employeeclockoutQR?error=Error from python script`);
    });
});

app.get('/updateemployeeaccount', (req,res) =>{
    var pythonProcess = spawn('python',["./grabUserAccountTableColumnsController.py"])
    pythonProcess.stdout.on('data',(data) =>{
        try{
            var myList = JSON.parse(data.toString())
            res.render('UpdateEmployeeAccount',{myList, message: req.flash('message')})
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

app.post('/updateemployeeaccount', (req,res) =>{
    const emlpoyeeidentity = req.session.emlpoyeeidentity
    const myJSON = {
        employeeid : emlpoyeeidentity,
        selectedoption : req.body.selectedoption,
        value : req.body.value
    }
    const myJSON2 = JSON.stringify(myJSON)
    console.log(myJSON2)
    var pythonProcess = spawn('python',["./UpdateManagerAccountController.py",myJSON2])
    pythonProcess.stdout.on('data',(data)=>{
    var bool = data.toString()
    console.log(bool)
    req.flash('message', null);
    if (bool.trim() == "Failed")
    {
        req.flash('message','Unable to update Employee Account. Double check your values entered')
        res.redirect('/updateemployeeaccount')
    }
    else
    {
        req.flash('message','Employee Account Updated')
        res.redirect('/updateemployeeaccount')
    }
})
})

app.get('/employeedeleteleave', (req, res) => {
    const emlpoyeeidentity = req.session.emlpoyeeidentity
    const myJSON = {
        employeeid : emlpoyeeidentity
    }
    const myJSON2 = JSON.stringify(myJSON)
    console.log(myJSON2)
    var pythonProcess = spawn('python', ["./EmployeeViewPendingLeaveController.py",myJSON2]);
    let alldata = "";
    pythonProcess.stdout.on('data', (data) => {
        alldata += data.toString();
        console.log(alldata)
    });
    pythonProcess.stdout.on('end', () => {
        req.flash('message17', null);
        try {
            if (alldata.trim() === "No table left"){
                req.flash('message17', 'No Table Left');
                res.render('EmployeeDeleteLeaveGUI', { message: req.flash('message17') });
            } else {
                const jsonData = JSON.parse(alldata.trim());
                req.flash('message17', 'Tables found');
                res.render('EmployeeDeleteLeaveGUI', { results: jsonData, message: req.flash('message17') });
            }
        } catch (error) {
            console.error("Error parsing JSON:", error);
            req.flash('message17', 'Error retrieving data');
            res.render('EmployeeDeleteLeaveGUI', { message: req.flash('message17') });
        }
    });
    pythonProcess.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
    });
});

app.post('/employeedeleteleave', (req,res) =>{
    const button = req.body.buttonid
    const csvArray = button.split(',')
    const jsonObj = {
        id : csvArray[0]
    }
    const jsonObj2 = JSON.stringify(jsonObj)
    console.log(jsonObj2)
    var pythonProcess = spawn('python',["./ManagerApproveLeaveController.py",jsonObj2])
    pythonProcess.stdout.on('data',(data)=>{
    var alldata = data.toString().trim()
    console.log(alldata)
    if (alldata == "Success")
    {
        req.flash('message17','Deleted Successfully')
        res.redirect('/employeedeleteleave')
        
    }
    else
    {
        req.flash('message17','Unsuccessful')
        res.redirect('/employeedeleteleave') 
    }
})
})

app.get('/managerviewcalender', (req, res) => {
    var pythonProcess = spawn('python', ["./ViewCalenderFormatWorkController.py"])
    pythonProcess.stdout.on('data', (data) => {
        req.flash('message17', null);
        try {
            var shiftsData = JSON.parse(data.toString());
            console.log("Shifts data:", shiftsData); // Check the shiftsData here
            if (!Array.isArray(shiftsData)) {
                shiftsData = []; // Ensure shiftsData is an array
            }
        } catch (error) {
            console.log("Error parsing JSON data:", error);
            shiftsData = []; // Set empty array if parsing fails
        }
        if (shiftsData.length === 0) {
            req.flash('message17', 'No Table Left');
            res.render('ManagerViewWorkshiftCalenderGUI', { message: req.flash('message17') });
        } else {
            req.flash('message17', 'Tables found');
            res.render('ManagerViewWorkshiftCalenderGUI', { results: shiftsData, message: req.flash('message17') });
        }
    });
});

app.get('/managerupdateshifthrs', (req, res) => {
    res.render('ManagerUpdateEmployeeNoOfHrsWorkedGUI', { message: req.flash('message17') });
});

app.post('/managerupdateshifthrs', (req, res) => {
    var pythonProcess = spawn('python', ["./ManagerUpdateEmployeeHoursController.py"])
    pythonProcess.stdout.on('data',(data)=>{
    req.flash('message17', null);
    var alldata = data.toString().trim()
    console.log(alldata)
    if (alldata == "Success")
    {
        req.flash('message17','Reset Successfully')
        res.redirect('/managerupdateshifthrs')
    }
    else
    {
        req.flash('message17','Unsuccessful')
        res.redirect('/managerupdateshifthrs') 
    }
})
});

app.get('/managerincharge', (req, res) => {
    res.render('ManagerUpdateManagerInChargeGUI', { message: req.flash('message17') });
});

app.post('/managerincharge', (req,res) =>{
    const jsonObj = {
        employeeid : req.body.employeeid
    }
    const jsonObj2 = JSON.stringify(jsonObj)
    console.log(jsonObj2)
    var pythonProcess = spawn('python',["./UpdateManagerInChargeController.py",jsonObj2])
    pythonProcess.stdout.on('data',(data)=>{
    var alldata = data.toString().trim()
    console.log(alldata)
    if (alldata == "Success")
    {
        req.flash('message17','Updated Successfully')
        res.redirect('/managerincharge')
        
    }
    else
    {
        req.flash('message17','Unsuccessful')
        res.redirect('/managerincharge') 
    }
})
})

app.get('/employeeupdateshiftpref', (req,res) =>{
    var pythonProcess = spawn('python',["./grabShiftPreferenceController.py"])
    pythonProcess.stdout.on('data',(data) =>{
        try{
            var myList = JSON.parse(data.toString())
            var shiftPrefList = JSON.parse(myList.shift_pref);
            var dayList = JSON.parse(myList.day);
            console.log(myList)
            console.log(shiftPrefList)
            console.log(dayList)
            res.render('EmployeeUpdateShiftPrefGUI',{shiftPrefList ,days: ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'],message:req.flash('message')})
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

app.post('/employeeupdateshiftpref', (req, res) => {
    const emlpoyeeidentity = req.session.emlpoyeeidentity
    const schedule = {};
    // Loop through each key in req.body and extract schedule data
    for (const key in req.body) {
        if (key.startsWith('schedule')) {
            const matches = key.match(/schedule\[(.*?)\]\[(.*?)\]/);
            if (matches !== null) { // Check if matches is not null
                const day = matches[1];
                const type = matches[2];
    
                if (!schedule[day]) {
                    schedule[day] = {};
                }
    
                schedule[day][type] = req.body[key];
            } else {
                console.error('Key ',{key},' does not match the expected pattern');
            }
        }
    }
    const myJSON = {
        employeeid : emlpoyeeidentity
    }
    // Convert schedule and employeeid to JSON strings
    const scheduleJSON = JSON.stringify(schedule);
    const employeeidJSON = JSON.stringify(myJSON);
    console.log(employeeidJSON)
    const pythonProcess = spawn('python', ["./EmployeeUpdateShiftPreferenceController.py", scheduleJSON,employeeidJSON]);
    console.log(scheduleJSON)
    pythonProcess.stdout.on('data', (data) => { 
        req.flash('message', null);
        const result = data.toString().trim();    
        console.log(result)    
        // Check the result and respond accordingly
        if (result === "Failed") {
            req.flash('message', 'Unable to Create Preference. Double check your values entered');
        } else {
            req.flash('message', 'Preference Created');
        }      
        // Redirect back to the same page
        res.redirect('/employeeupdateshiftpref');
    });

    // Handle errors from the Python process
    pythonProcess.stderr.on('data', (data) => {
        console.error(`Error from Python script: ${data}`);
        req.flash('message', 'Error updating WorkShift');
        res.redirect('/employeeupdateshiftpref');
    });
});

app.get('/employee_updateleave', (req,res) =>{
    var pythonProcess = spawn('python',["./grabEmployeeLeaveColumnsController.py"])
    pythonProcess.stdout.on('data',(data) =>{
        try{
            var myList = JSON.parse(data.toString())
            res.render('EmployeeUpdateLeaveGUI',{myList, message: req.flash('message')})
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

app.post('/employee_updateleave', (req,res) =>{
    const myJSON = {
        leaveid : req.body.leaveid,
        selectedoption : req.body.selectedoption,
        value : req.body.value
    }
    const myJSON2 = JSON.stringify(myJSON)
    console.log(myJSON)
    var pythonProcess = spawn('python',["./EmployeeUpdateLeaveController.py",myJSON2])
    pythonProcess.stdout.on('data',(data)=>{
    var bool = data.toString()
    console.log(bool)
    req.flash('message', null);
    if (bool.trim() == "Failed")
    {
        req.flash('message','Unable to update Leave. Double check your values entered')
        res.redirect('/employee_updateleave')
    }
    else
    {
        req.flash('message','Leave Updated')
        res.redirect('/employee_updateleave')
    }
})
})

app.get('/employeeviewshifts', (req, res) => {
    const myJSON = {
        employeeid: req.session.emlpoyeeidentity
    };
    const myJSON2 = JSON.stringify(myJSON);
    console.log(myJSON2);

    const pythonProcess = spawn('python', ["./EmployeeViewShiftsController.py", myJSON2]);

    let allData = ""; // Variable to store all data from Python process

    pythonProcess.stdout.on('data', (data) => {
        allData += data.toString(); // Append data received from Python
        console.log(allData)
    });

    pythonProcess.on('close', (code) => {
        req.flash('message17', null);
        try {
            if (allData.trim() == "Failed"){
                req.flash('message17', 'No Table Left');
                res.render('EmployeeViewShiftsGUI', { message: req.flash('message17') });
            }
            else{
                const parsedData = JSON.parse(allData);
                if (parsedData === "No table left" || parsedData === "") {
                    req.flash('message17', 'No Table Left');
                    res.render('EmployeeViewShiftsGUI', { message: req.flash('message17') });
                } else {
                    req.flash('message17', 'Tables found');
                    res.render('EmployeeViewShiftsGUI', { results: parsedData, message: req.flash('message17') });
                }
            }
        } catch (error) {
            console.error("Error parsing JSON:", error);
            req.flash('message17', 'Error: Invalid data received');
            res.render('EmployeeViewShiftsGUI', { message: req.flash('message17') });
        }
    });

    pythonProcess.on('error', (err) => {
        console.error('Failed to start Python process.', err);
        req.flash('message17', 'Error: Failed to start Python process');
        res.render('EmployeeViewShiftsGUI', { message: req.flash('message17') });
    });
});

app.get('/employeecreatefeedback', (req,res) =>{
    res.render('EmployeeCreateFeedbackGUI',{ message: req.flash('message')})
})

app.get('/feedbackchoose', (req,res) =>{
    res.render('FeedbackChooseGUI')
})

app.get('/adminviewfeedback', (req, res) => {
    var pythonProcess = spawn('python', ["./AdminViewFeedbackController.py"]);
    pythonProcess.stdout.on('data', (data) => {
        req.flash('message17', null);
        try {
            var alldata = JSON.parse(data.toString());
            console.log(alldata);
        } catch (error) {
            console.log(alldata);
        }
        if (data.toString().trim() == "Failed") {
            req.flash('message17', 'No Table Left');
            res.render('AdminViewFeedbackGUI', { message: req.flash('message17') });
        } else {
            req.flash('message17', 'Tables found');
            res.render('AdminViewFeedbackGUI', { alldata: alldata, message: req.flash('message17') });
        }
    });
});

app.get('/managerviewfeedback', (req, res) => {
    var pythonProcess = spawn('python', ["./ManagerViewFeedbackController.py"]);
    pythonProcess.stdout.on('data', (data) => {
        req.flash('message17', null);
        try {
            var alldata = JSON.parse(data.toString());
            console.log(alldata);
        } catch (error) {
            console.log(alldata);
        }
        if (data.toString().trim() == "Failed") {
            req.flash('message17', 'No Table Left');
            res.render('ManagerViewFeedbackGUI', { message: req.flash('message17') });
        } else {
            req.flash('message17', 'Tables found');
            res.render('ManagerViewFeedbackGUI', { alldata: alldata, message: req.flash('message17') });
        }
    });
});

app.post('/employeecreatefeedback', (req,res) =>{
    const myJSON = {
        feedback : req.body.feedback
    }
    const myJSON2 = JSON.stringify(myJSON)
    console.log(myJSON)
    var pythonProcess = spawn('python',["./EmployeeCreateFeedbackController.py",myJSON2])
    pythonProcess.stdout.on('data',(data)=>{
    var bool = data.toString()
    console.log(bool)
    req.flash('message', null);
    if (bool.trim() == "Failed")
    {
        req.flash('message','Unable to create Feedback.')
        res.redirect('/employeecreatefeedback')
    }
    else
    {
        req.flash('message','Feedback Created')
        res.redirect('/employeecreatefeedback')
    }
})
})


app.get('/managercreatefeedback', (req,res) =>{
    res.render('ManagerCreateFeedbackGUI',{ message: req.flash('message')})
})


app.post('/managercreatefeedback', (req,res) =>{
    const myJSON = {
        feedback : req.body.feedback
    }
    const myJSON2 = JSON.stringify(myJSON)
    console.log(myJSON)
    var pythonProcess = spawn('python',["./ManagerCreateFeedbackController.py",myJSON2])
    pythonProcess.stdout.on('data',(data)=>{
    var bool = data.toString()
    console.log(bool)
    req.flash('message', null);
    if (bool.trim() == "Failed")
    {
        req.flash('message','Unable to create Feedback.')
        res.redirect('/managercreatefeedback')
    }
    else
    {
        req.flash('message','Feedback Created')
        res.redirect('/managercreatefeedback')
    }
})
})

app.get('/managerviewemployeeworkshift', (req, res) => {
    var pythonProcess = spawn('python', ["./ManagerViewEmployeeShiftController.py"])
    pythonProcess.stdout.on('data', (data) => {
        req.flash('message17', null);
        try {
            var shiftsData = JSON.parse(data.toString());
            console.log("Shifts data:", shiftsData); // Check the shiftsData here
            if (!Array.isArray(shiftsData)) {
                shiftsData = []; // Ensure shiftsData is an array
            }
        } catch (error) {
            console.log("Error parsing JSON data:", error);
            shiftsData = []; // Set empty array if parsing fails
        }
        if (shiftsData.length === 0) {
            req.flash('message17', 'No Table Left');
            res.render('ManagerViewEmployeeWorkShiftGUI', { message: req.flash('message17') });
        } else {
            req.flash('message17', 'Tables found');
            res.render('ManagerViewEmployeeWorkShiftGUI', { shiftsData: shiftsData, message: req.flash('message17') });
        }
    });
});

app.get('/manager_reassignshifts', (req,res) =>{
    res.render('ManagerReassignShiftsGUI',{ message: req.flash('message17') })
})

app.post('/manager_reassignshifts', (req, res) => {
    const employeeid = req.body.employeeid;
    const myJSON = {
        employeeid: req.body.employeeid
    };
    const myJSON2 = JSON.stringify(myJSON);
    console.log(myJSON2);

    const pythonProcess = spawn('python', ["./AdminViewFutureShiftsController.py", myJSON2]);

    let allData = ""; // Variable to store all data from Python process

    pythonProcess.stdout.on('data', (data) => {
        allData += data.toString(); // Append data received from Python
        console.log(allData)
    });

    pythonProcess.on('close', (code) => {
        req.flash('message17', null);
        try {
            const parsedData = JSON.parse(allData);
            if (parsedData === "No table left") {
                req.flash('message17', 'No Table Left');
                res.render('ManagerReassignWorkShiftsTableGUI', { message: req.flash('message17') });
            } else {
                req.flash('message17', 'Tables found');
                res.render('ManagerReassignWorkShiftsTableGUI', { results: parsedData, message: req.flash('message17') });
            }
        } catch (error) {
            console.error("Error parsing JSON:", error);
            req.flash('message17', 'Error: Invalid data received');
            res.render('ManagerReassignWorkShiftsTableGUI', { message: req.flash('message17') });
        }
    });

    pythonProcess.on('error', (err) => {
        console.error('Failed to start Python process.', err);
        req.flash('message17', 'Error: Failed to start Python process');
        res.render('ManagerReassignWorkShiftsTableGUI', { message: req.flash('message17') });
    });
});

app.post('/manager_reassignshiftss', (req,res) =>{
    const button = req.body.buttonid
    const csvArray = button.split(',')
    const jsonObj = {
        id : csvArray[0],
        employeeid: req.body.employeeid
    }
    const jsonObj2 = JSON.stringify(jsonObj)
    console.log(jsonObj2)
    var pythonProcess = spawn('python',["./ManagerReassignShiftsController.py",jsonObj2])
    pythonProcess.stdout.on('data',(data)=>{
    req.flash('message4', null);
    var alldata = data.toString().trim()
    console.log(alldata)
    if (alldata == "Success")
    {
        req.flash('message4','Reassigned Successfully')
        res.redirect("/manager_reassignshifts")
        
    }
    else
    {
        req.flash('message4','Unsuccessful')
        res.redirect("/manager_reassignshifts")
    }
})
})




//Listening to port 3000
app.listen(port, () => console.info('Listening on port ',port))