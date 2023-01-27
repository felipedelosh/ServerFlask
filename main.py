from flask import Flask, Response, request
from Database import *
from Controllers.Person_Controller import *




app = Flask(__name__)
database = Database()
personsController = Person_Controller()

@app.route('/')
def hello():
    return database.getStatitics()

@app.route('/health')
def health():
    return "Server is OK"

@app.route('/person', methods=['GET', 'POST'])
def person():
    if request.method == 'GET':
        all_person_info = database.getAllPersonsInfo()
        return personsController.getPersons(request.args, all_person_info)

    if request.method == 'POST':
        return "Not available in POST"

    return "Estoy acaaaaa"

@app.route('/person/download/csv')
def personToCSV():
    all_person_info = database.getAllPersonsInfo()
    information = personsController.getInformationPersonsForCSV(request.args, all_person_info)

    return Response(information, mimetype="text/csv", headers={"Content-Disposition": "attachment; filename=persons.csv"})


#Start
if __name__ == '__main__':
    app.run(host='0.0.0.0' ,debug=True, port=4000)