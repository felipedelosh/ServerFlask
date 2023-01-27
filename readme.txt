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
        open postman or navigator in route:
        localhost:4000/health
        and the server return the message.


________________________________________
Objetive:

This server is create to add/get persons information. 
Need filter all information and download in diferen formats via API


![](/Docs/exmapleDownloadCSVPersons.png)

.csv
localhost:4000/persons.csv


![](/Docs/exampleDownloadZip.png)
.zip
localhost:4000/persons_by_sex.zip

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

Filters:

1 -> Filter via gender... Obtan all mens if add params: filter_gender = F
                          Obtan all womaen if add params: filter_gender = m

2 -> Filter via age... if you need persons more than 30yo put the filter : filter_age_up = 29
                       if you need persons less than 50 yo put the filter: filter_age_down = 49
                       and is posible to conbinate to obtain between.

2 -> Filter via city location... If you need persons to area only put a filter: filter_location = city to need



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
localhost:4000/persons.csv

Retrun a .csv file with filters Params

Params to filter:
filter_gender = String M or F return only diferent male or female registers
filter_age_up = integer return only registers with age upper (exclusive)
filter_age_down = integer return only registers with age down (exclusive)
filter_location = String 


.csv sepator via | "Pipeline"


++++++++++++++++++++++++++++++
localhost:4000/persons_by_sex.zip

Return 2 .csv file and contain:
 persons_male.csv : all information about mens
 persons_female.csv : all information about women



DASENDE 
