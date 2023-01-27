"""
FelipedelosH
2023

This class is create to manipulate and filter all information abouts persons

"""
#To Download .csv
import io
import csv

class Person_Controller:
    def __init__(self) -> None:
        pass

    def getPersons(self, filters, data):
        information = {}
        export_info = []
        
        count = 0

        filter_gender = "filter_gender" in filters
        filter_age_up = "filter_age_up" in filters
        filter_age_down = "filter_age_down" in filters
        filter_location = "filter_location" in filters
        

        for i in data:
            if filter_gender:
                if str(i["gender"]).upper() == str(filters["filter_gender"]).upper():
                    count = count + 1
                    continue

            if filter_age_up:
                try:
                    if int(i["age"]) < int(filters["filter_age_up"]):
                        count = count + 1
                        continue
                except:
                    continue

            if filter_age_down:
                try:
                    if int(i["age"]) > int(filters["filter_age_down"]):
                        count = count + 1
                        continue
                except:
                    continue

            if filter_location:
                if str(i["location"]).upper() != str(filters["filter_location"]).upper():
                    count = count + 1
                    continue

            # If pass al filters save
            export_info.append(i)
    
            
            
            
        information['data'] = export_info
        information['type_of_values'] = "person"
        information['total_values'] = len(export_info)
        information['total_info_procesed'] = count
        
        return information

    def getInformationPersonsForCSV(self, filters, data):
        information = self.getPersons(filters, data)
        csv_info = []
        csv_info.append("ID|Name|lastName|Age|Gender|Location") 
        
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(csv_info)

        counter_id = 0
        for i in information["data"]:
            id = str(counter_id)
            name = str(i["name"])
            lastName = str(i["lastname"])
            age = str(i["age"])
            gender = i["gender"]
            location = i["location"]
            writer.writerow([f"{id}|{name}|{lastName}|{age}|{gender}|{location}"])

            counter_id = counter_id + 1

        
        output.seek(0)
        return output
