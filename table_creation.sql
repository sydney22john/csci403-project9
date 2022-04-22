-- CREATE TABLE STATEMENTS

set search_path to nstevenson;
drop table if exists neighborhood, d_class, property, airbnb;

CREATE TABLE neighborhood (
    number INT PRIMARY KEY, 
    name TEXT
);

CREATE TABLE d_class (
    id TEXT PRIMARY KEY,
    NAME TEXT
);

CREATE TABLE property (
    transaction_num INT PRIMARY KEY,
    reception_date DATE,
    sale_price INT,
    grantor TEXT,
    grantee TEXT, 
    class TEXT,
    mkt_clus TEXT,
    d_class TEXT REFERENCES d_class(id),
    nbhd_1 INT REFERENCES neighborhood(number)
);

CREATE TABLE airbnb (
    id INT PRIMARY KEY,
    neighborhood TEXT,
    price MONEY,
    latitude FLOAT,
    longitude FLOAT
);