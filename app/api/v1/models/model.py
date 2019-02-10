import json
from app.api.v1.validation import validation
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

propertyData = {
  "parties": ("id", "name", "hqAddress", "logoUrl", "abbr"),
  "offices": ("id", "name", "type")
}


class Models():
    def __init__(self, tableName, data):
        self.tableName = tableName
        self.data = data

    def createData(self):
        if validation.checkIfTableExitst(self.tableName) is False:
            return returnMessages.error(404, "404 (Not Found), The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.")
        elif validation.checkIfPropertiesExist(self.data, propertyData[self.tableName]) is False:
            return returnMessages.error(422, "422 (Unprocessable Entity), Please make sure to enter the correct requests, which are " + str(propertyData[self.tableName]))
        elif validation.checkIfPropertyValuesAreEmpty(self.data) is False:
            return returnMessages.error(422, "422 (Unprocessable Entity), Please make sure the values are not empty, and that you have valid syntax")
        elif validation.checkIfDataExists(dataStore[self.tableName], str(self.data["id"])) is True:
            return returnMessages.error(403, "403 (Forbidden), You cannot create " + self.tableName + " that already exists")
        dataStore[self.tableName][str(self.data["id"])] = self.data
        return returnMessages.success(201, self.data)

    def getAllData(self):
        if validation.checkIfTableExitst(self.tableName) is False:
            return returnMessages.error(404, "404 (Not Found), The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.")
        elif validation.checkIfAllDataExists(dataStore[self.tableName]) is False:
            return returnMessages.error(404, "404 (Not Found), " + self.tableName + " data were not found")
        return returnMessages.success(201, dataStore[self.tableName])

    def getSpecificData(self, id):
        if validation.checkIfTableExitst(self.tableName) is False:
            return returnMessages.error(404, "404 (Not Found), The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.")
        elif validation.checkIfDataExists(dataStore[self.tableName], str(id)) is False:
            return returnMessages.error(404, "404 (Not Found), The " + self.tableName + " you are looking for does not exist")
        return returnMessages.success(201, dataStore[self.tableName][str(id)])

    def editSpecificData(self, id):
        if validation.checkIfTableExitst(self.tableName) is False:
            return returnMessages.error(404, "404 (Not Found), The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.")
        elif validation.checkIfPropertiesExist(self.data, propertyData[self.tableName]) is False:
            return returnMessages.error(422, "422 (Unprocessable Entity), Please make sure to enter the correct requests, which are " + str(propertyData[self.tableName]))
        elif validation.checkIfPropertyValuesAreEmpty(self.data) is False:
            return returnMessages.error(422, "422 (Unprocessable Entity), Please make sure the values are not empty, and that you have valid syntax")
        elif validation.checkIfDataExists(dataStore[self.tableName], id) is False:
            return returnMessages.error(404, "404 (Not Found), The " + self.tableName + " you are trying to edit does not exist")
        dataStore[self.tableName][id]["name"] = self.data["name"]
        return returnMessages.success(201, dataStore[self.tableName][id])

    def deleteSpecificData(self, id):
        if validation.checkIfTableExitst(self.tableName) is False:
            return returnMessages.error(404, "404 (Not Found), The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.")
        elif validation.checkIfDataExists(dataStore[self.tableName], id) is False:
            return returnMessages.error(404, "404 (Not Found), The " + self.tableName + " you are trying to delete does not exist")
        dataStore[self.tableName].pop(id)
        return returnMessages.success(201, {"message": "Delete successful"})
