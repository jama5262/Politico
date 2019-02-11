import json
from app.api.v1.validation.validation import validate
from app.api.v1.returnMessages import returnMessages

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
  },
  "offices": {
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


class Models():
    def __init__(self, tableName, data):
        self.tableName = tableName
        self.data = data

    def createData(self):
        valid = validate(dataStore, self.tableName, "c", self.data, str(self.data["id"]))
        if valid["isValid"] is False:
            return valid["data"]
        dataStore[self.tableName][str(self.data["id"])] = self.data
        return returnMessages.success(201, self.data)

    def getAllData(self):
        valid = validate(dataStore, self.tableName, "r")
        if valid["isValid"] is False:
            return valid["data"]
        return returnMessages.success(201, dataStore[self.tableName])

    def getSpecificData(self, id):
        valid = validate(dataStore, self.tableName, "rs", None, id)
        if valid["isValid"] is False:
            return valid["data"]
        return returnMessages.success(201, dataStore[self.tableName][str(id)])

    def editSpecificData(self, id):
        valid = validate(dataStore, self.tableName, "r", self.data, id)
        if valid["isValid"] is False:
            return valid["data"]
        dataStore[self.tableName][id]["name"] = self.data["name"]
        return returnMessages.success(201, dataStore[self.tableName][id])

    def deleteSpecificData(self, id):
        valid = validate(dataStore, self.tableName, "d", None, id)
        if valid["isValid"] is False:
            return valid["data"]
        dataStore[self.tableName].pop(id)
        return returnMessages.success(201, {"message": "Delete successful"})
