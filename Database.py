import sqlite3

class Database:
    def __init__(self) -> None:
        self.conection = sqlite3.connect("database.db")

        self.createsTables()

    
    def createsTables(self):
        try:

            print("Acaaaaaaa")
            return True
        except:
            return False

