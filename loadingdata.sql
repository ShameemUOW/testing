insert into useraccount (Fullname,Address,Email,Mobile,Username,pass,MaxHours,PlaceHolder) values ('Jake','America 2','jake@gmail.com','12341234','jake','jake22','40','Admin');
insert into useraccount (Fullname,Address,Email,Mobile,Username,pass,MaxHours,PlaceHolder) values ('Tom','America 3','Tom@gmail.com','45671234','Tom','Tom22','40','Employee');
insert into useraccount (Fullname,Address,Email,Mobile,Username,pass,MaxHours,PlaceHolder) values ('Son','America 4','Son@gmail.com','86751234','Son','son22','40','Manager');
insert into useraccount (Fullname,Address,Email,Mobile,Username,pass,MaxHours,PlaceHolder) values ('Daughter','America 5','Daughter@gmail.com','23451234','Daughter','Daughter22','40','Manager');
insert into useraccount (Fullname,Address,Email,Mobile,Username,pass,MaxHours,PlaceHolder) values ('Aiden','America 2','Aiden@gmail.com','12341234','aiden','aiden22','40','Manager');
insert into useraccount (Fullname,Address,Email,Mobile,Username,pass,MaxHours,PlaceHolder) values ('Mike','America 1','mike@gmail.com','32121234','mike','mike22','40','Manager');
insert into useraccount (Fullname,Address,Email,Mobile,Username,pass,MaxHours,PlaceHolder) values ('Harold','America 1','Harold@gmail.com','23121234','harold','harold22','40','Employee');
insert into useraccount (Fullname,Address,Email,Mobile,Username,pass,MaxHours,PlaceHolder) values ('James','America 5','James@gmail.com','23121223','james','james22','40','Employee');
insert into useraccount (Fullname,Address,Email,Mobile,Username,pass,MaxHours,PlaceHolder) values ('Jack','America 6','Jack@gmail.com','23121212','jack','jack22','40','Employee');
insert into useraccount (Fullname,Address,Email,Mobile,Username,pass,MaxHours,PlaceHolder) values ('Noah','America 7','Noah@gmail.com','23121234','noah','noah22','40','Manager');
insert into useraccount (fullname,address,email,mobile,username,pass,MaxHours,PlaceHolder) values ('Noa','America 7','Noa@gmail.com','23121234','noa','noa22','40','Manager');
insert into useraccount (fullname,address,email,mobile,username,pass,MaxHours,PlaceHolder) values ('Noas','America 7','Noa@gmail.com','23121234','noas','noas22','40','Employee');



insert into userprofile values ('1','Admin','NIL');
insert into userprofile values ('2','Employee','Waiter');
insert into userprofile values ('3','Manager','NIL');
insert into userprofile values ('4','Manager','NIL');
insert into userprofile values ('5','Manager','NIL');
insert into userprofile values ('6','Employee','Cashier');
insert into userprofile values ('7','Employee','Chef');
insert into userprofile values ('8','Employee','Waiter');
insert into userprofile values ('9','Manager', 'NIL'); 
insert into userprofile values ('10','Manager', 'NIL'); 

insert into employeeshiftinformation values ('2','Tuesday','Day','0');
insert into employeeshiftinformation values ('6','Monday','Night','0');
insert into employeeshiftinformation values ('7','Tuesday','Morning','0');
insert into employeeshiftinformation values ('8','Wednesday','Afternoon','0');

INSERT INTO workshift (Date, shift, start, end)
VALUES ('2024-03-15', 'Morning', '08:00:00', '16:00:00');
INSERT INTO workshift (Date, shift, start, end)
VALUES ('2024-03-19', 'Afternoon', '14:00:00', '20:00:00');
INSERT INTO workshift (Date, shift, start, end)
VALUES ('2024-03-19', 'Late Morning', '11:00:00', '20:00:00');
INSERT INTO workshift (Date, shift, start, end)
VALUES ('2024-03-19', 'Evening', '15:00:00', '20:00:00');
INSERT INTO workshift (Date, shift, start, end)
VALUES ('2024-03-21', 'Afternoon', '12:00:00', '20:00:00');
INSERT INTO workshift (Date, shift, start, end)
VALUES ('2024-03-20', 'Afternoon', '14:00:00', '20:00:00');
INSERT INTO workshift (Date, shift, start, end)
VALUES ('2024-03-21', 'Afternoon', '12:00:00', '20:00:00');
INSERT INTO workshift (Date, shift, start, end)
VALUES ('2024-03-21', 'Afternoon', '13:00:00', '20:00:00');
INSERT INTO workshift (Date, shift, start, end)
VALUES ('2024-03-23', 'Morning', '09:30:00', '14:00:00');
INSERT INTO workshift (Date, shift, start, end)
VALUES ('2024-03-23', 'Morning', '09:30:00', '13:00:00');


Insert Into EmployeeShift (shiftid,employeeid,shiftDate,shiftType)
VALUES ('2','2','2024-03-19','Afternoon');
Insert Into EmployeeShift (shiftid,employeeid,shiftDate,shiftType)
VALUES ('3','2','2024-03-19','Late Morning');
Insert Into EmployeeShift (shiftid,employeeid,shiftDate,shiftType)
VALUES ('3','4','2024-03-19','Evening');
Insert Into EmployeeShift (shiftid,employeeid,shiftDate,shiftType)
VALUES ('4','2','2024-03-19','Evening');
Insert Into EmployeeShift (shiftid,employeeid,shiftDate,shiftType)
VALUES ('5','2','2024-03-21','Afternoon');
Insert Into EmployeeShift (shiftid,employeeid,shiftDate,shiftType)
VALUES ('6','2','2024-03-20','Afternoon');
Insert Into EmployeeShift (shiftid,employeeid,shiftDate,shiftType)
VALUES ('7','2','2024-03-21','Afternoon');
Insert Into EmployeeShift (shiftid,employeeid,shiftDate,shiftType)
VALUES ('8','2','2024-03-21','Afternoon');
Insert Into EmployeeShift (shiftid,employeeid,shiftDate,shiftType)
VALUES ('9','2','2024-03-23','Morning');
Insert Into EmployeeShift (shiftid,employeeid,shiftDate,shiftType)
VALUES ('10','2','2024-03-23','Morning');


INSERT INTO EmployeeLeave (employeeid, Date, LeaveType, status)
VALUES ('3', '2024-03-15', 'sick', 'Pending');
INSERT INTO EmployeeLeave (employeeid, Date, LeaveType, status)
VALUES ('4', '2024-03-16', 'sick', 'Pending');
INSERT INTO EmployeeLeave (employeeid, Date, LeaveType, status)
VALUES ('5', '2024-03-17', 'sick', 'Pending');
INSERT INTO EmployeeLeave (employeeid, Date, LeaveType, status)
VALUES ('6', '2024-03-18', 'sick', 'Pending');

INSERT INTO Attendance (employeeid, Date,clockin,clockout, attendance)
VALUES ('7', '2024-03-19', '13:11:32', '20:00:00','Late');

update useraccount set useraccount.Pass = sha2(useraccount.Pass,0) where useraccount.EmployeeID > 0 AND char_length(useraccount.Pass) < 64