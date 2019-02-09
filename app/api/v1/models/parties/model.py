import json
from app.api.v1.validation import validation
from app.api.v1.returnMessages import returnMessages

dataStore = {
    "Parties": {
        "1": {
            "id": 1,
            "name": "Party Name",
            "abbr": "Party Abbreviation",
            "logoUrl": "Party URL",
            "hqAddress": "Party HQ"
        },
        "2": {
            "id": 2,
            "name": "Party Name",
            "abbr": "Party Abbreviation",
            "logoUrl": "Party URL",
            "hqAddress": "Party HQ"
        }
    }
}

tuples = ("id", "name", "hqAddress", "logoUrl", "abbr")


class Parties():
    def __init__(self, data="Jama"):
        self.data = data

    def createParty(self):
        if validation.checkIfPropertiesExist(self.data, tuples) is False:
            return returnMessages.error(422, "(Unprocessable Entity), Please make sure to enter the correct requests, which are " + str(tuples))
        elif validation.checkIfPropertyValuesAreEmpty(self.data) is False:
            return returnMessages.error(422, "(Bad Request), Please make sure the values are not empty, and that you have valid syntax")
        elif validation.checkIfDataExists(dataStore["Parties"], str(self.data["id"])) is True:
            return returnMessages.error(403, "(Bad Request), You cannot create a party that already exists")
        dataStore["Parties"][str(self.data["id"])] = self.data
        return returnMessages.success(201, self.data)

    def getAllParties(self):
        if validation.checkIfAllDataExists(dataStore["Parties"]) is False:
            return returnMessages.error(404, "(Not Found) Parties were not found")
        return returnMessages.success(201, dataStore["Parties"])

    def getSpecificParty(self, partyID):
        if validation.checkIfDataExists(dataStore["Parties"], partyID) is False:
            return returnMessages.error(404, "(Not Found) The party you are looking for does not exist")
        return returnMessages.success(201, dataStore["Parties"][partyID])

    def editSpecificParty(self, partyID):
        if validation.checkIfPropertiesExist(self.data, tuples) is False:
            return returnMessages.error(422, "(Unprocessable Entity), Please make sure to enter the correct requests, which are " + str(tuples))
        elif validation.checkIfPropertyValuesAreEmpty(self.data) is False:
            return returnMessages.error(422, "(Bad Request), Please make sure the values are not empty, and that you have valid syntax")
        elif validation.checkIfDataExists(dataStore["Parties"], partyID) is False:
            return returnMessages.error(404, "(Not Found) Parties you are trying to edit does not exist")
        party = dataStore["Parties"][partyID]
        party["name"] = self.data["name"]
        party["abbr"] = self.data["abbr"]
        party["logoUrl"] = self.data["logoUrl"]
        party["hqAddress"] = self.data["hqAddress"]
        return returnMessages.success(201, self.data)

    def deleteSpecificParty(self, partyID):
        if validation.checkIfDataExists(dataStore["Parties"], partyID) is False:
            return returnMessages.error(404, "(Not Found) Parties you are trying to delete does not exist")
        dataStore["Parties"].pop(partyID)
        return returnMessages.success(201, {"message": "Party ahas been deleted"})
