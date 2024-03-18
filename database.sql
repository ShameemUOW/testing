CREATE DATABASE FYP;
use FYP;

create TABLE userAccount(
	EmployeeID int auto_increment NOT NULL,
    Fullname varchar(50) NOT NULL,
    Address varchar(60) NOT NULL,
    Email varchar(60) NOT NULL,
    Mobile bigint(8) NOT NULL,
    Username varchar(50) NOT NULL,
    Pass varchar(50) NOT NULL,
	MaxHours int(4) NOT NULL,
    PlaceHolder varchar(50) NOT NULL,
    PRIMARY KEY (EmployeeID)
);

create TABLE userProfile(
	EmployeeID int NOT NULL,
    MainRole varchar(50) NOT NULL,
    Job varchar(60),
    PRIMARY KEY (EmployeeID),
    CONSTRAINT FK_EmployeeID FOREIGN KEY (EmployeeID)
    REFERENCES userAccount(EmployeeID)
    on update cascade
    on delete cascade
);


CREATE TABLE workshift (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Date varchar(50) NOT NULL,
    shift VARCHAR(255) NOT NULL,
    start TIME NOT NULL,
    end TIME NOT NULL
);

CREATE TABLE EmployeeShiftInformation (
	EmployeeID int NOT NULL,
    ShiftPref varchar(50) NOT NULL,
    NoOfHrsWorked int NOT NULL,
    PRIMARY KEY (EmployeeID),
    CONSTRAINT FK_EmployeeID2 FOREIGN KEY (EmployeeID)
    REFERENCES userAccount(EmployeeID)
    on update cascade
    on delete cascade
);

CREATE TABLE EmployeeLeave (
    LeaveID INT AUTO_INCREMENT PRIMARY KEY,
    EmployeeID int NOT NULL,
    Fullname VARCHAR(50) NOT NULL,
    Date DATE NOT NULL,
    LeaveType VARCHAR(50) NOT NULL,
    status VARCHAR(50) NOT NULL
    REFERENCES userAccount(EmployeeID)
    on update cascade
    on delete cascade
);


drop database FYP;
