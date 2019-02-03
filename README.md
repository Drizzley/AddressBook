# AddressBook
A desktop application that stroes the addresses of users in a database. Written in Python and using a MySQL database. GUI is made with `TKinter` library included with Python. This application was originally intended for use in a grocery store. This application would help keep track of people who would order groceries online by entering the total amount of the purchase and exporting to an `.CSV` file for book keeping purposes. The exported file is called `customer.csv`. The address is saved for customers who regularly purchase their groceries at this grocery store.

## Video Demo
![addressBookGif](https://github.com/afranco07/gifImageStorage/blob/master/addressBookDemo.gif?raw=true)

## Running The App

**You will need**
- Python 3
- Virtualenv (or any other package that manages python virtual environments for you)
- Tkinter
- Docker

1. Make sure you have Python 3 installed.
2. Make sure you have Docker installed.
2. Make sure you have Tkinter installed. If you don't have it installed:
    - For linux use: `sudo apt-get install python python3-tk`
    - For other Windows or MacOS check: https://tkdocs.com/tutorial/install.html
3. Create a virtual environment for this project and activate it (Make sure it is using python 3).
4. Install the projects dependencies using pip i.e. `pip install -r requirements.txt`
5. Run the `start_app.sh` file by: `./start_app.sh`

If there any errors when trying to start the script, make sure `start_app.sh` is executable. You can do this by `chmod +x start_app.sh`

#### Steps Shown in Video
First a new contact is created using the `Add New` button. Their information is added into the text boxes and after pressing `Done`, their information is added to the database. The information I input was as follows:
```
First Name: Fake
Last Name:  Person
Street:     123 Lane
Apt:        Apt 4B
City:       Fake City
State:      NY
Zip:        09823
[X]Male []Female
```

Next, the contact that was just added is selected from the list on the left and click on the `Export` button. We verify that the information shown is correct, select either `Cash` or `Credit`, and the total amount spent in the text box labeled `Total`. Click on `Export` again and the all the information is written to a `.csv` file named `customer.csv`. What I entered in the `Export Customer` screen:
```
[]Cash [X]Credit
Total $: 123.09
```

After that, I use the terminal to show the contents of the `customer.csv` that was just created. I use the command `cat customer.csv` to output the contents of the file
```
$: cat customer.csv 
Fake Person (m)
Fake City
Apt 4B
"Fake City, NY 09823"
credit: $123.09
```

Finally, I delete the contact that was just created by selecting the contact from the list on the left and pressing the `Remove` button.


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

#### id
Primary key for differentiating between all entries in the database. This field auto increments and has a length of 11.

#### first_name
Person's first name. Max length of 12 characters.

#### last_name
Person's last name. Max length of 12 characters.

#### address1
The address line for the customer. Max length of 50 characters.

#### address2
This field is used for Apartment numbers, etc. Max length of 20 characters.

#### state
Stores thet state. This field has length of 2 characters.
```
Eg.
NY, NJ, PA, CA, etc
```

#### city
Stores the city. Max length of 12 characters.
```
Eg.
Boston, Chicago, Washington, San Francisco
```

#### zip
Stores the zip code. Length of 5 characters

#### sex
Stores the gender of the person. Max length of 1 character. Choices are either `m` for male, or `f` for female.

## Explanantion of Buttons

#### Add New
Use this button to add another person's address to the database. You'll need to enter the person's `First Name`, `Last Name`, `Street`, `Apt`, `City`, `State`, `Zip`, and `Sex`. You may leave any field blank besides `Sex`.

#### Export
Use this button to export the selected person and prepare to send their information to an excel sheet. Here you just need to select either `Cash` or `Credit`, and the total amount of the purchase.

#### Remove
Use this button to remove any person's address information from the database. Just select any person's name in the list and click `Remove`.

## Customer.csv File
Once a person is exported from the application, their information is sent to a `.csv` file named `customer.csv`. The format of this `.csv` file is as follows:
```
First Name Last Name (sex)
Address Line 1
Apartment Number (if applicable)
City, State Zip
[Cash or Credit]: $total amount
```
#### Example of customer.csv
![export_screen](https://github.com/afranco07/gifImageStorage/blob/master/address_book_csv_screen_shot.png?raw=true)