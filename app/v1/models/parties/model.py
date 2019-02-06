import json
from app.v1.validation import validation


class Parties():
    def __init__(self, data="Jama"):
        self.data = data

    def getFromDataStore(self):
        with open("datastore\data.json") as f:
            return json.load(f)

    def setToDataStore(self, dataStore):
        with open("dataStore/data.json", "w") as f:
            json.dump(dataStore, f, indent=2)

    def createParty(self):
        if validation.checkPartyProperties(self.data) is False:
            return {
                "status": 422,
                "error": "Please make sure to enter the correct requests"
            }
        dataStore = self.getFromDataStore()
        dataStore["Parties"][self.data["id"]] = self.data
        self.setToDataStore(dataStore)
        return {
            "status": 200,
            "data": self.data
        }

    def getAllParties(self):
        dataStore = self.getFromDataStore()
        if validation.checkIfPartiesExits(dataStore) is False:
            return {
                "status": 404,
                "error": "Parties were not found"
            }
        return {
            "status": 200,
            "data": self.getFromDataStore()["Parties"]
        }

    def getSpecificParty(self, partyID):
        dataStore = self.getFromDataStore()
        if validation.checkIfPartyExits(dataStore, partyID) is False:
            return {
                "status": 404,
                "error": "This party does not exist"
            }
        return {
            "status": 200,
            "data": dataStore["Parties"][partyID]
        }

    def editSpecificParty(self, partyID):
        dataStore = self.getFromDataStore()
        if validation.checkIfPartyExits(dataStore, partyID) is False:
            return {
                "status": 404,
                "error": "This party does not exist"
            }
        elif validation.checkPartyProperties(self.data) is False:
            return {
                "status": 422,
                "error": "Please make sure to enter the correct requests"
            }
        party = dataStore["Parties"][partyID]
        party["name"] = self.data["name"]
        party["abbr"] = self.data["abbr"]
        party["logoUrl"] = self.data["logoUrl"]
        party["hqAddress"] = self.data["hqAddress"]
        self.setToDataStore(dataStore)
        return {
            "status": 200,
            "data": self.data
        }

    def deleteSpecificParty(self, partyID):
        dataStore = self.getFromDataStore()
        if validation.checkIfPartyExits(dataStore, partyID) is False:
            return {
                "status": 404,
                "error": "This party does not exist"
            }
        dataStore["Parties"].pop(partyID)
        self.setToDataStore(dataStore)
        return {
            "status": 200,
            "data": {
                "message": "Party deleted"
            }
        }