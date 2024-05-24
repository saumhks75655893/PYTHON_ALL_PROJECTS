create database if not exists HotelManagement;
use HotelManagement; 

create table customer
(ref int primary key not null,
Name varchar(50),
MotherName varchar(50),
Gender varchar(50),
PostCode varchar(50),
MobileNo varchar(50),
Email varchar(50),
Nationality varchar(50),
IdProof varchar(50),
IdNumber varchar(50),
Address varchar(50)
);

show tables;
desc customer;

select * from customer;

create table yes
(y_id int primary key,
y_name varchar(250));

select * from yes;
truncate yes;