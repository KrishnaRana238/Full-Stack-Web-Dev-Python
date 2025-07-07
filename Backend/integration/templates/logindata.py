create database loin_data;
use loin_data;

create table users(
    id int auto_increment primary key,
    username varchar(50) not null unique,
    email varchar(100) not null unique,
    password_hash varchar(255) not null,
);

