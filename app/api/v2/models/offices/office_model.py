from app.api.v2.utils.validations.validation import validate
from app.api.v2.utils.returnMessages import returnMessages

dataStore = {
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


class OfficeModel():
    def __init__(self, data=None, id=None):
        self.tableName = "offices"
        self.data = data
        self.id = id

    def createOffice(self):
        valid = validate(dataStore, self.tableName, "c", self.data, self.id)
        if valid["isValid"] is False:
            return valid["data"]
        dataStore[self.tableName][str(self.data["id"])] = self.data
        return returnMessages.success(201, self.data)

    def getAllOffices(self):
        valid = validate(dataStore, self.tableName, "r")
        if valid["isValid"] is False:
            return valid["data"]
        return returnMessages.success(201, dataStore[self.tableName])

    def getSpecificOffice(self):
        valid = validate(dataStore, self.tableName, "rs", None, self.id)
        if valid["isValid"] is False:
            return valid["data"]
        return returnMessages.success(201, dataStore[self.tableName][str(self.id)])

    def editSpecificOffice(self):
        valid = validate(dataStore, self.tableName, "r", self.data, self.id)
        if valid["isValid"] is False:
            return valid["data"]
        dataStore[self.tableName][self.id]["name"] = self.data["name"]
        return returnMessages.success(201, dataStore[self.tableName][self.id])

    def deleteSpecificOffice(self):
        valid = validate(dataStore, self.tableName, "d", None, self.id)
        if valid["isValid"] is False:
            return valid["data"]
        dataStore[self.tableName].pop(self.id)
        return returnMessages.success(201, {"message": "Delete successful"})
