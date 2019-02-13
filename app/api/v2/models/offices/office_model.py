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
  },
  "officeMembers": {
      "1": {
          "office": 1,
          "user": 2
      }
  },
  "officeResults": {
      "1": [
          {
            "office": 1,
            "candidate": 2,
            "result": 300
          },
          {
            "office": 1,
            "candidate": 2,
            "result": 300
          },
          {
            "office": 1,
            "candidate": 2,
            "result": 300
          },
      ],
      "2": [
          {
            "office": 1,
            "candidate": 2,
            "result": 300
          },
          {
            "office": 1,
            "candidate": 2,
            "result": 300
          },
          {
            "office": 1,
            "candidate": 2,
            "result": 300
          },
      ]
  }
}


class OfficeModel():
    def __init__(self, data=None, id=None):
        self.propertyName = "offices"
        self.data = data
        self.id = id

    def createOffice(self):
        valid = validate(self.propertyName, self.data)
        if valid["isValid"] is False:
            return valid["data"]
        dataStore[self.propertyName][str(self.data["id"])] = self.data
        return returnMessages.success(201, self.data)

    def getAllOffices(self):
        return returnMessages.success(201, dataStore[self.propertyName])

    def getSpecificOffice(self):
        if self.id not in dataStore["offices"]:
            return returnMessages.error(404, "404 (Not Found), The office you are looking for does not exist")
        return returnMessages.success(201, dataStore[self.propertyName][str(self.id)])

    def editSpecificOffice(self):
        valid = validate(propertyName, self.data)
        if valid["isValid"] is False:
            return valid["data"]
        dataStore[self.propertyName][self.id]["name"] = self.data["name"]
        return returnMessages.success(201, dataStore[self.propertyName][self.id])

    def deleteSpecificOffice(self):
        dataStore[self.propertyName].pop(self.id)
        return returnMessages.success(201, {"message": "Delete successful"})

    def userRegisterToOffice(self):
        if self.id not in dataStore["offices"]:
            return returnMessages.error(404, "(Not Found), The office does not exist")
        officeid = len(dataStore["officeMembers"]) + 1
        self.data["office"] = self.id
        dataStore["officeMembers"][str(officeid)] = self.data
        return returnMessages.success(201, self.data)

    def officeResults(self):
        if self.id not in dataStore["officeResults"]:
            return returnMessages.error(404, "404 (Not Found), The office you are looking for does not exist")
        return returnMessages.success(200, dataStore["officeResults"][self.id])
