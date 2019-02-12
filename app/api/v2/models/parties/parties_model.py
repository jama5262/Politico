from app.api.v2.utils.validations.validation import validate
from app.api.v2.utils.returnMessages import returnMessages

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
        self.tableName = "parties"
        self.data = data
        self.id = id

    def createParty(self):
        valid = validate(dataStore, self.tableName, "c", self.data, self.id)
        if valid["isValid"] is False:
            return valid["data"]
        dataStore[self.tableName][str(self.data["id"])] = self.data
        return returnMessages.success(201, self.data)

    def getAllParties(self):
        valid = validate(dataStore, self.tableName, "r")
        if valid["isValid"] is False:
            return valid["data"]
        return returnMessages.success(201, dataStore[self.tableName])

    def getSpecificParty(self):
        valid = validate(dataStore, self.tableName, "rs", None, self.id)
        if valid["isValid"] is False:
            return valid["data"]
        return returnMessages.success(201, dataStore[self.tableName][str(self.id)])

    def editSpecificParty(self):
        valid = validate(dataStore, self.tableName, "r", self.data, self.id)
        if valid["isValid"] is False:
            return valid["data"]
        dataStore[self.tableName][self.id]["name"] = self.data["name"]
        return returnMessages.success(201, dataStore[self.tableName][self.id])

    def deleteSpecificParty(self):
        valid = validate(dataStore, self.tableName, "d", None, self.id)
        if valid["isValid"] is False:
            return valid["data"]
        dataStore[self.tableName].pop(self.id)
        return returnMessages.success(201, {"message": "Delete successful"})
