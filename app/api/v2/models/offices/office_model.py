from app.api.v2.utils.validations.validation import validate
from app.api.v2.utils.returnMessages import returnMessages
from app.api.database.schemaGenerator.schemaGenerator import SchemaGenerator
from app.api.database.database import Database

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
        schema = SchemaGenerator(self.propertyName, self.data).insterInto()
        db = Database(schema).executeQuery()
        if db["status"] == 500:
            return {
                "status": db["status"],
                "error": db["error"]
            }
        return returnMessages.success(200, self.data)

    def getAllOffices(self):
        schema = SchemaGenerator(self.propertyName).selectAll()
        db = Database(schema, True).executeQuery()
        if db["status"] == 500:
            return {
                "status": db["status"],
                "error": db["error"]
            }
        if not db["data"]:
            return {
                "status": 404,
                "error": "404 (NotFound), Offices where not found"
            }
        return returnMessages.success(200, db["data"])

    def getSpecificOffice(self):
        schema = SchemaGenerator(self.propertyName, None, self.id).selectSpecific()
        db = Database(schema, True).executeQuery()
        if db["status"] == 500:
            return {
                "status": db["status"],
                "error": db["error"]
            }
        if not db["data"]:
            return {
                "status": 404,
                "error": "404 (NotFound), The office does not exist"
            }
        return returnMessages.success(200, db["data"])

    def editSpecificOffice(self):
        valid = validate(self.propertyName, self.data)
        if valid["isValid"] is False:
            return valid["data"]
        schema = SchemaGenerator(self.propertyName, self.data, self.id).updateSpecific()
        db = Database(schema).executeQuery()
        if db["status"] == 500:
            return {
                "status": db["status"],
                "error": db["error"]
            }
        return returnMessages.success(200, self.data)

    def deleteSpecificOffice(self):
        schema = SchemaGenerator(self.propertyName, None, self.id).deleteSpecific()
        print(schema)
        db = Database(schema).executeQuery()
        if db["status"] == 500:
            return {
                "status": db["status"],
                "error": db["error"]
            }
        return returnMessages.success(200, {
            "message": "data deleted"
        })

    def userRegisterToOffice(self):
        valid = validate("candidates", self.data)
        if valid["isValid"] is False:
            return valid["data"]
        schema = SchemaGenerator("candidates", self.data).insterInto()
        db = Database(schema).executeQuery()
        if db["status"] == 500:
            return {
                "status": db["status"],
                "error": db["error"]
            }
        return returnMessages.success(201, self.data)

    def officeResults(self):
        if self.id not in dataStore["officeResults"]:
            return returnMessages.error(404, "404 (Not Found), The office you are looking for does not exist")
        return returnMessages.success(200, dataStore["officeResults"][self.id])
