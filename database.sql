CREATE DATABASE FYP;
use FYP;

create TABLE userAccount(
	CafeID int NOT NULL,
    Fullname varchar(50) NOT NULL,
    Address varchar(60) NOT NULL,
    Email varchar(60) NOT NULL,
    Mobile bigint(8) NOT NULL,
    Username varchar(50) NOT NULL,
    Pass varchar(50) NOT NULL,
    PRIMARY KEY (CafeID)
);
