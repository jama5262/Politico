from app.api.v2.utils.validations.validation import validate
from app.api.v2.utils.returnMessages.returnMessages import success

dataStore = {
  "parties": {
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

class PartyModel():
    def __init__(self, data=None, id=None):
        self.propertyName = "parties"
        self.data = data
        self.id = id

    def createParty(self):
        valid = validate(self.propertyName, self.data)
        if valid["isValid"] is False:
            return valid["data"]
        dataStore[self.propertyName][str(self.data["id"])] = self.data
        return success(201, self.data)

    def getAllParties(self):
        return success(201, dataStore[self.propertyName])

    def getSpecificParty(self):
        return success(201, dataStore[self.propertyName][str(self.id)])

    def editSpecificParty(self):
        valid = validate(self.propertyName, self.data)
        if valid["isValid"] is False:
            return valid["data"]
        dataStore[self.propertyName][self.id]["name"] = self.data["name"]
        return success(201, dataStore[self.propertyName][self.id])

    def deleteSpecificParty(self):
        return success(201, {"message": "Delete successful"})
