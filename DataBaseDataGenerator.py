"""
FelipedelosH

2023


This class is create to generate Randomn data of Persons...
name,lastname,age,geneder,location

"""
import random
from Database import *


PersonsNamesMales = [
"Santiago",
"Andres",
"Felipe",
"Matías",
"Emmanuel",
"Emiliano",
"Jerónimo",
"Samuel",
"Maximiliano",
"Mathias",
"Thiago",
"Martín"
]


PersonsNamesFemales = [
"Angie",
"Daniela",
"Luciana",
"Juanita",
"Lorena"
"Salomé",
"Isabella",
"Mariana",
"Antonella",
"Gabriela",
"Mariangel",
"Samantha",
"Victoria",
"Valentina",
"María"
]

PersonsLastNames = [
"Rodríguez",
"Gómez",
"López",
"González",
"García",
"Martínez",
"Ramírez",
"Sánchez",
"Hernández",
"Díaz",
"Pérez",
"Torres",
"Rojas",
"Vargas",
"Moreno",
"Gutiérrez",
"Jiménez",
"Muñoz",
"Castro",
"Ortiz",
"Álvarez",
"Ruiz",
"Suárez",
"Romero",
"Herrera",
"Hernández",
"Valencia",
"Quintero",
"Restrepo",
"Giraldo",
"Morales",
"Mejía",
"Arias",
"Parra",
"Jaramillo",
"Cárdenas",
"Osorio",
"Castillo",
"Salazar",
"Cardona",
"Flórez",
"Medina",
"Rivera",
"Montoya",
"Cortes",
"Correa",
"Marín",
"Rincón",
"Zapata",
"Escobar",
"Velásquez"
]

locations = [
"Bogotá",
"Medellín",
"Cartagena",
"Cali",
"Santa marta",
"Barranquilla",
"Manizales",
"Pereira",
"Arauca",
"Palmira",
"Riosucio",
"Anserma",
"Pácora",
"Viterbo",
"Santa rosa de cabal",
"Guática"
]


def getRandomMaleName():
    return PersonsNamesMales[random.randint(0, len(PersonsNamesMales)-1)]

def getRandomFemaleName():
    return PersonsNamesFemales[random.randint(0, len(PersonsNamesFemales)-1)]

def getRandomLastName():
    return PersonsLastNames[random.randint(0, len(PersonsLastNames)-1)]

def getRandomLocation():
    return locations[random.randint(0, len(locations)-1)]

def getRandomSex():
    sex = ['M', 'F']
    return sex[random.randint(0, len(sex)-1)]

def getRandomAge():
    return random.randint(0, 80)

def getRandomPersonInfo():
    """
    Return a (name,lastname,age,geneder,location)
    """
    sex = getRandomSex()

    if sex == 'M':
        name = getRandomMaleName()
    else:
        name = getRandomFemaleName()

    lastname = getRandomLastName() + " " + getRandomLastName()
    age = getRandomAge()
    location = getRandomLocation()

    return (name, lastname, age, sex, location)



# Charge X persons in Database
d = Database()
for _ in range(0, 1000):
    personInfo = getRandomPersonInfo()
    d.insertPerson(personInfo)
    print(personInfo)
