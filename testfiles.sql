select distinct mainrole From userprofile;
select * from useraccount;
select * from workshift;
select * from userprofile;
select * from EmployeeShift;
select * from employeeshiftinformation;
select distinct shiftpref From employeeshiftinformation;
select * from Employeeshift;
select * from EmployeeLeave;
select * from attendance;
select * from workshift;
select employeeid, fullname, shiftpref, mainrole,job from useraccount natural join employeeshiftinformation natural join userprofile where shiftPref = 'Day';
select employeeid, Fullname, Address,Email,mobile,maxhours,job from useraccount natural join userprofile where mainrole = 'Employee';
select column_name from information_schema.columns where table_schema = 'FYP' and table_name = 'useraccount' and column_name not in ('PlaceHolder','Username','pass') union select column_name from information_schema.columns where table_schema = 'FYP' and table_name = 'userprofile' and column_name not in ('EmployeeID','MainRole') union select column_name from information_schema.columns where table_schema = 'FYP' and table_name = 'employeeshiftinformation' and column_name not in ('EmployeeID');
select EmployeeID,FullName,Address,Email,Mobile,MaxHours,Job,ShiftPref,NoOfHrsWorked from useraccount natural join employeeshiftinformation natural join userprofile where fullname = 'Tom';
select column_name from information_schema.columns where table_schema = 'FYP' and table_name = 'useraccount' and column_name not in ('EmployeeID');


update employeeleave SET status = 'Approved' where leaveid = '6';
UPDATE useraccount SET fullname = 'noahhh' where employeeid = 10;