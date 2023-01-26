"""
FelipedelosH
2023

This class is create to manipulate and filter all information abouts persons

"""
class Person_Controller:
    def __init__(self) -> None:
        pass

    def getPersons(self, filters, data):
        information = {}
        export_info = []
        
        count = 0

        filter_gender = "filter_gender" in filters

        for i in data:
            if filter_gender:
                if i["gender"] == filters["filter_gender"]:
                    count = count + 1
                    continue

            
            export_info.append(i)
    
            
            
            
        information['data'] = export_info
        information['type_of_values'] = "person"
        information['total_values'] = len(export_info)
        information['total_info_procesed'] = count
        
        return information

