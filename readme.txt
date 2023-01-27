FelipedelosH

This is a server to practice:

Pipelines
Databases
Filter information via controller and database.


________________________________________
Instructions:

Install: python3 -m pip install flask

Before to RUN: Preprare the information DB      
                - Erase file: database.db
                - Run the Script: DataBaseDataGenerator.py 
                - Verify the creation  of database.db 

To RUN: execute archive main.py 
        open postmain or navigator in route:
        localhost:4000/health
        and the server return the message.


________________________________________
Objetive:

This server is create to add/get persons information. 
Need filter all information and download in diferen formats via API

.csv
localhost:4000/person/download/csv
.zip

______________________________________
DB:

Sqlite:

PERSON
ID int PK
name str
lastname str
age int 
gender str (M|F)
location str
_________________________________________





________________________________________
Routes:


++++++++++++++++++++++++++++++
localhost:4000/ 

Is the index route and return Json
{
 name of database,
 quantity of rows in table persons
}


++++++++++++++++++++++++++++++
localhost:4000/person

GET
>
Return a Json with the correspont information about the persons

Params to filter:
filter_gender = String M or F return only diferent male or female registers
filter_age_up = integer return only registers with age upper (exclusive)
filter_age_down = integer return only registers with age down (exclusive)
filter_location = String 

Json to return:

{
 type_of_values : name of table "Person",
 total_values : size of all returned registers,
 total_info_procesed : size of skiped registers,
 data : [{PersonData},{PersonData},{PersonData},{PersonData}...]
}


++++++++++++++++++++++++++++++
localhost:4000/person/download/csv

Retrun a .csv file with filters Params

Params to filter:
filter_gender = String M or F return only diferent male or female registers
filter_age_up = integer return only registers with age upper (exclusive)
filter_age_down = integer return only registers with age down (exclusive)
filter_location = String 


.csv sepator via |


++++++++++++++++++++++++++++++

