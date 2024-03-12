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

insert into userprofile values ('1','System Admin','NIL');
insert into userprofile values ('2','Cafe Staff','Waiter');
insert into userprofile values ('3','Cafe Manager','NIL');
insert into userprofile values ('4','Cafe Owner','NIL');
insert into userprofile values ('5','Cafe Owner','NIL');
insert into userprofile values ('6','Cafe Staff','Cashier');
insert into userprofile values ('7','Cafe Staff','Chef');
insert into userprofile values ('8','Cafe Staff','Waiter');
insert into userprofile values ('9','Cafe Manager', 'NIL'); 
insert into userprofile values ('10','Cafe Manager', 'NIL'); 

select distinct mainrole From userprofile;
select * from useraccount;