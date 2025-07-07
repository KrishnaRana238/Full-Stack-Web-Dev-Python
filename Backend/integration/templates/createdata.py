create database if not exists create_login_data;
use create_login_data;

create table if not exists users(
    id int auto_increment primary key,
    username varchar(50) not null unique,
    email varchar(100) not null unique,
    gender ENUM('Male', 'Female') not null,
    date_of_birth date not null,
    phone varchar(15) not null unique,

    password_hash varchar(255) not null
    created_at timestamp default current_timestamp,
);
