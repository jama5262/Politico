import json
from app.api.v1.validation import validation

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
            return {
                "status": 422,
                "error": "Please make sure to enter the correct requests, which are " + str(tuples)
            }
        elif validation.checkIfPropertyValuesAreEmpty(self.data) is False:
            return {
                "status": 400,
                "error": "Bad request, please make sure the values are not empty"
            }
        elif validation.checkIfDataExists(dataStore["Parties"], str(self.data["id"])) is True:
            return {
                "status": 403,
                "error": "The party already exists"
            }
        dataStore["Parties"][str(self.data["id"])] = self.data
        return {
            "status": 201,
            "data": self.data
        }

    def getAllParties(self):
        if validation.checkIfAllDataExists(dataStore["Parties"]) is False:
            return {
                "status": 404,
                "error": "Parties were not found"
            }
        return {
            "status": 201,
            "data": dataStore["Parties"]
        }

    def getSpecificParty(self, partyID):
        if validation.checkIfDataExists(dataStore["Parties"], partyID) is False:
            return {
                "status": 404,
                "error": "This party does not exist"
            }
        return {
            "status": 201,
            "data": dataStore["Parties"][partyID]
        }

    def editSpecificParty(self, partyID):
        if validation.checkIfPropertiesExist(self.data, tuples) is False:
            return {
                "status": 422,
                "error": "Please make sure to enter the correct requests"
            }
        elif validation.checkIfPropertyValuesAreEmpty(self.data) is False:
            return {
                "status": 400,
                "error": "Bad request, please make sure the values are not empty"
            }
        elif validation.checkIfDataExists(dataStore["Parties"], partyID) is False:
            return {
                "status": 404,
                "error": "This party does not exist"
            }
        party = dataStore["Parties"][partyID]
        party["name"] = self.data["name"]
        party["abbr"] = self.data["abbr"]
        party["logoUrl"] = self.data["logoUrl"]
        party["hqAddress"] = self.data["hqAddress"]
        return {
            "status": 201,
            "data": self.data
        }

    def deleteSpecificParty(self, partyID):
        if validation.checkIfDataExists(dataStore["Parties"], partyID) is False:
            return {
                "status": 404,
                "error": "This party does not exist"
            }
        dataStore["Parties"].pop(partyID)
        return {
            "status": 201,
            "data": {
                "message": "Party deleted"
            }
        }
