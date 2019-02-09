import json
from app.api.v1.validation import validation
from app.api.v1.returnMessages import returnMessages

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

tuples = ("id", "name", "type")


class Offices:
    def __init__(self, data=None):
        self.data = data

    def creatOffice(self):
        if validation.checkIfPropertiesExist(self.data, tuples) is False:
            return returnMessages.error(422, "(Unprocessable Entity), Please make sure to enter the correct requests, which are " + str(tuples))
        elif validation.checkIfPropertyValuesAreEmpty(self.data) is False:
            return returnMessages.error(422, "(Bad Request), Please make sure the values are not empty, and that you have valid syntax")
        elif validation.checkIfDataExists(dataStore["Offices"], str(self.data["id"])) is True:
            return returnMessages.error(403, "(Bad Request), You cannot create an office that already exists")
        dataStore["Offices"][str(self.data["id"])] = self.data
        return returnMessages.success(201, self.data)

    def getAllOffices(self):
        if validation.checkIfAllDataExists(dataStore["Offices"]) is False:
            return returnMessages.error(404, "(Not Found) Offices were not found")
        return returnMessages.success(201, dataStore["Offices"])

    def getSpecificOffice(self, officeID):
        if validation.checkIfDataExists(dataStore["Offices"], officeID) is False:
            return returnMessages.error(404, "(Not Found) The office you are looking for does not exist")
        return returnMessages.success(201, dataStore["Offices"][officeID])
