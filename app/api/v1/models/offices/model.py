import json
from app.api.v1.validation.offices import validation

dataStore = {
    "Offices": {
        "1": {
            "id": 1,
            "type": "Office type 1",
            "name": "Office name 1"
        },
        "2": {
            "id": 2,
            "type": "Office type 2",
            "name": "Office name 2"
        }
    }
}


class Offices:
    def __init__(self, data=None):
        self.data = data

    def creatOffice(self):
        if validation.checkOfficeProperties(self.data) is False:
            return {
                "status": 422,
                "error": "Please make sure to enter the correct requests"
            }
        elif validation.checkIfOfficeValuesAreEmpty(self.data) is False:
            return {
                "status": 400,
                "error": "Bad request, please make sure the values are not empty"
            }
        elif validation.checkIfOfficeExits(dataStore, str(self.data["id"])) is True:
            return {
                "status": 403,
                "error": "The office already exists"
            }
        dataStore["Offices"][str(self.data["id"])] = self.data
        return {
            "status": 201,
            "data": self.data
        }

    def getAllOffices(self):
        if validation.checkIfOfficesExits(dataStore) is False:
            return {
                "status": 404,
                "error": "Offices were not found"
            }
        return {
            "status": 201,
            "data": dataStore["Offices"]
        }

    def getSpecificOffice(self, officeID):
        if validation.checkIfOfficeExits(dataStore, officeID) is False:
            return {
                "status": 404,
                "error": "This office does not exist"
            }
        return {
            "status": 201,
            "data": dataStore["Offices"][officeID]
        }
