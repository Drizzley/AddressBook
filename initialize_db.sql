CREATE DATABASE testdb;

USE testdb;

CREATE TABLE foodtown ( 
  id int(11) unsigned not null auto_increment, 
  first_name varchar(12), 
  last_name varchar(12), 
  phone varchar(10), 
  address1 varchar(50), 
  address2 varchar(50),
  state char(2), 
  city varchar(12), 
  zip char(5), 
  sex char(1), 
  primary key (id) 
);

INSERT INTO foodtown(first_name, last_name, phone, address1, address2, state, city, zip, sex) 
VALUES("Fake", "Person", "1234567890", "123 Lane", "", "NY", "Bellerose", "11426", "M");

INSERT INTO foodtown(first_name, last_name, phone, address1, address2, state, city, zip, sex) 
VALUES("Thomas", "Green", "1234567890", "123 St", "Apt 2C", "NJ", "Englewood", "00001", "M");

INSERT INTO foodtown(first_name, last_name, phone, address1, address2, state, city, zip, sex) 
VALUES("Cynthia", "McPerson", "1234567890", "123 Blvd", "2nd Floor", "CA", "Los Angeles", "00001", "F");