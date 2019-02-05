import json
from app.v1.validation import validation
# from datastore import data


class Parties():
    def __init__(self, data):
        self.data = data

    def getFromDataStore(self):
        with open("datastore\data.json") as f:
            return json.load(f)

    def setToDataStore(self, dataStore):
        with open("dataStore/data.json", "w") as f:
            json.dump(dataStore, f, indent=2)

    def createParty(self):
        if validation.checkForParty(self.data) is False:
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
