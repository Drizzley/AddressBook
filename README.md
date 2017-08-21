# AddressBook
A desktop application that stroes the addresses of users in a database. Written in Python and using a MySQL database. GUI is made with `TKinter` library included with Python. This application was originally intended for use in a grocery store. This application would help keep track of people who would order groceries online by entering the total amount of the purchase and exporting to an excel sheet for book keeping purposes. The address is saved for customers who regularly purchase their groceries at this grocery store.

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

## Explanantion of Buttons

#### Add New
Use this button to add another person's address to the database. You'll need to enter the person's `First Name`, `Last Name`, `Street`, `Apt`, `City`, `State`, `Zip`, and `Sex`. You may leave any field blank besides `Sex`.

#### Export
Use this button to export the selected person and prepare to send their information to an excel sheet. Here you just need to select either `Cash` or `Credit`, and the total amount of the purchase.

#### Remove
Use this button to remove any person's address information from the database. Just select any person's name in the list and click `Remove`.