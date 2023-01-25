"""
FelipedelosH

Ta make a unit test

"""
from Database import *

# Test init Database
d = Database()

# Test show tables
d.showAllTables()

# Insert Example Person
personInfo = ("Test name", "test lastname", 50, 'N', 'manizales')
d.insertPerson(personInfo)

# get all Persons
d.getAllPersonsInfo()

