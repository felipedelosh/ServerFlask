import sqlite3

class Database:
    def __init__(self) -> None:
        self.conection = sqlite3.connect("database.db")

        self.createsTables()

    
    def createsTables(self):
        sql = """
        create table if not exists Person
        (
            id integer primary key AUTOINCREMENT,
            name text,
            lastname text,
            age integer,
            gender text,
            location text
        )
        """
        try:
            self.conection = sqlite3.connect("database.db")
            self.conection.execute(sql)
            self.conection.close()
        except:
            print("Error Generate DB")

    def showAllTables(self):
        sql = """
        SELECT * FROM sqlite_master WHERE type = "table"
        """
        try:
            self.conection = sqlite3.connect("database.db")
            cursor = self.conection.execute(sql)

            for i in cursor:
                print(i)

        except:
            print("Error Conection DB")

        self.conection.close()

    def insertPerson(self, personValues):
        """ 
        personValues  = (str,str,int,str,str)
        """
        sql = """
        insert into Person (name,lastname,age,gender,location) values (?,?,?,?,?)
        """
        try:
            self.conection = sqlite3.connect("database.db")
            self.conection.execute(sql, personValues)
            self.conection.commit()
        except:
            print("Error Inser person: "+str(personValues))

        self.conection.close()

    def getAllPersonsInfo(self):
        sql = """
        select * from Person
        """
        data = []
        try:
            
            self.conection = sqlite3.connect("database.db")
            cursor = self.conection.execute(sql)

            for i in cursor:
                person = {}
                # name,lastname,age,geneder,location
                person["name"] = i[1]
                person["lastname"] = i[2]
                person["age"] = int(i[3])
                person["gender"] = i[4]
                person["location"] = i[5]
                data.append(person)

            cursor.close()
        except:
            print("Error To get All persons info")
        

        self.conection.close()
        return data

    def getCountOfPersons(self, information):
        sql = """
        select count(*) from Person
        """
        try:
            self.conection = sqlite3.connect("database.db")
            cursor = self.conection.execute(sql)

            information['total_rows'] = str(cursor.fetchone()[0])
            cursor.close()
        except:
            information['total_rows'] = "Error To Calculate"

        self.conection.close()

    def getStatitics(self):
        information = {
            "name_of_database" : "database.db"
        }
        self.getCountOfPersons(information)


        return information
