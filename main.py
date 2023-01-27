from flask import Flask, Response, request, render_template
from Database import *
from Controllers.Person_Controller import *

#To save zipfile
from io import BytesIO
import time
import zipfile


app = Flask(__name__)
database = Database()
personsController = Person_Controller()


@app.errorhandler(404)
def not_found(error):
    context = {
        "error" : error
    }

    return render_template('404.html', **context)

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

@app.route('/persons.csv')
def personToCSV():
    all_person_info = database.getAllPersonsInfo()
    information = personsController.getInformationPersonsForCSV(request.args, all_person_info)

    return Response(information, mimetype="text/csv", headers={"Content-Disposition": "attachment; filename=persons.csv"})

@app.route('/persons_by_sex.zip')
def personToZIP():
    all_person_info = database.getAllPersonsInfo()
    # Create a .csv
    personsController.getInformationPersonsTOSeparatedBySexZIP(all_person_info)

    FILEPATHs = ["FILES/persons_male.csv", "FILES/persons_female.csv"]

    fileobj = io.BytesIO() # Create in Memory

    with zipfile.ZipFile(fileobj, 'w') as zf:
        for individualFile in FILEPATHs:
            data = zipfile.ZipInfo(individualFile)
            data.date_time = time.localtime(time.time())[:6]
            data.compress_type = zipfile.ZIP_DEFLATED
            with open(individualFile, 'rb') as fd:
                zf.writestr(data, fd.read())
            

    fileobj.seek(0)


    return Response(fileobj.getvalue(),
                        mimetype='application/zip',
                        headers={'Content-Disposition': 'attachment; filename=persons.zip'})


#Start
if __name__ == '__main__':
    app.run(host='0.0.0.0' ,debug=True, port=4000)
