# AddressBook
A desktop application that stroes the addresses of users in a database. Written in Python and using a MySQL database. GUI is made with `TKinter` library included with Python.

## Video Demo
![addressBookGif](./addressBookDemo.gif)


## Database Schema
| Field | Type | Null | Key | Default | Extra |
| ----- | ---- | ---- | --- | ------- | ----- |
| id    | int(11) | NO | PRI | NULL   | auto_increment |
| first_name | varchar(12) | YES | | NULL | |
| last_name | varchar(12) | YES | | NULL | |
| address1 | varchar(50) | YES | | NULL | |
| address2 | varchar(20) | YES | | NULL | |
| state | char(2) | YES | | NULL | |
| city | varchar(12) | YES | | NULL | |
| zip | char(5) | YES | | NULL | |
| sex | char(1) | YES | | NULL | |