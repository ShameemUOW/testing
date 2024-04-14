select distinct mainrole From userprofile;
select * from useraccount;
select * from workshift;
select * from userprofile;
select * from notification;
select * from EmployeeShift;
select * from EmployeeShiftinformation;
select distinct employeeid, noofhrsworked from employeeshiftinformation;
select distinct shiftpref From employeeshiftinformation;
select * from Employeeshift;
select * from EmployeeLeave;
select * from ApprovedEmployeeLeave;
select * from attendance;
select * from workshift;
select employeeid, fullname, shiftpref, mainrole,job from useraccount natural join employeeshiftinformation natural join userprofile where shiftPref = 'Day';
select employeeid, Fullname, Address,Email,mobile,maxhours,job from useraccount natural join userprofile where mainrole = 'Employee';
select column_name from information_schema.columns where table_schema = 'FYP' and table_name = 'useraccount' and column_name not in ('PlaceHolder','Username','pass') union select column_name from information_schema.columns where table_schema = 'FYP' and table_name = 'userprofile' and column_name not in ('EmployeeID','MainRole') union select column_name from information_schema.columns where table_schema = 'FYP' and table_name = 'employeeshiftinformation' and column_name not in ('EmployeeID');
select EmployeeID,FullName,Address,Email,Mobile,MaxHours,Job,ShiftPref,NoOfHrsWorked from useraccount natural join employeeshiftinformation natural join userprofile where fullname = 'Tom';
select column_name from information_schema.columns where table_schema = 'FYP' and table_name = 'useraccount' and column_name not in ('EmployeeID');

update employeeleave set status = 'Pending' where leaveid >0;



SELECT ua.EmployeeID, ua.Fullname, ua.Mobile, w.start, w.end 
                    FROM EmployeeShiftInformation esi
                    JOIN userAccount ua ON esi.EmployeeID = ua.EmployeeID
                    JOIN workshift w ON esi.ShiftPref = w.shift
                    WHERE esi.Day = 'Thursday' AND esi.ShiftPref = 'Evening' AND esi.EmployeeID NOT IN (
                        SELECT EmployeeID FROM EmployeeLeave WHERE Date = '2024-03-28'
                    ) 
                    AND w.Date = '2024-03-28'
                    ORDER BY esi.NoOfHrsWorked ASC;

SELECT * FROM workshift WHERE Date BETWEEN '2024-03-23' AND '2024-03-28';

update employeeleave SET status = 'Approved' where leaveid = '6';
UPDATE useraccount SET fullname = 'noahhh' where employeeid = 10;
update employeeshiftinformation set NoOfHrsWorked = 0 where employeeid >0;
select * from employeeshiftinformation;