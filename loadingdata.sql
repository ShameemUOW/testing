insert into useraccount values ('0','NIL','NIL','NIL','00000000','NIL','NIL');
insert into useraccount values ('1','Jake','America 2','jake@gmail.com','12341234','jake','jake22');
insert into useraccount values ('2','Tom','America 3','Tom@gmail.com','45671234','Tom','Tom22');
insert into useraccount values ('3','Son','America 4','Son@gmail.com','86751234','Son','son22');
insert into useraccount values ('4','Daughter','America 5','Daughter@gmail.com','23451234','Daughter','Daughter22');
insert into useraccount values ('5','Aiden','America 2','Aiden@gmail.com','12341234','aiden','aiden22');
insert into useraccount values ('6','Mike','America 1','mike@gmail.com','32121234','mike','mike22');
insert into useraccount values ('7','Harold','America 1','Harold@gmail.com','23121234','harold','harold22');
insert into useraccount values ('8','James','America 5','James@gmail.com','23121223','james','james22');
insert into useraccount values ('9','Jack','America 6','Jack@gmail.com','23121212','jack','jack22');
insert into useraccount values ('10','Noah','America 7','Noah@gmail.com','23121234','noah','noah22');

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