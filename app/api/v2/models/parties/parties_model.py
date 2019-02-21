from app.api.v2.utils.validations.validation import validate
from app.api.v2.utils.validations.validation import checkIfValuesHaveFirstLetterUpperCase
from app.api.v2.utils.returnMessages.returnMessages import success
from app.api.v2.utils.returnMessages.returnMessages import error
from app.api.database.schemaGenerator.schemaGenerator import SchemaGenerator
from app.api.database.database import Database


class PartyModel():
    def __init__(self, data=None, id=None):
        self.propertyName = "parties"
        if data is not None:
            self.data = checkIfValuesHaveFirstLetterUpperCase(data)
        self.id = id

    def createParty(self):
        valid = validate(self.propertyName, self.data)
        if valid["isValid"] is False:
            return valid["data"]
        schema = SchemaGenerator(self.propertyName, self.data).insterInto()
        db = Database(schema).executeQuery()
        if db["status"] == 400:
            return {
                "status": db["status"],
                "error": db["error"]
            }
        return success(200, {
            "data": self.data,
            "msg": "Party created successfully"
        })
        
    def getAllParties(self):
        schema = SchemaGenerator(self.propertyName).selectAll()
        db = Database(schema, True).executeQuery()
        if db["status"] == 400:
            return {
                "status": db["status"],
                "error": db["error"]
            }
        if not db["data"]:
            return {
                "status": 404,
                "error": "Parties where not found"
            }
        return success(200, {
            "data": db["data"],
            "msg": "All parties retrieved successfully"
        })

    def getSpecificParty(self):
        schema = SchemaGenerator(self.propertyName, None, self.id).selectSpecific()
        db = Database(schema, True).executeQuery()
        if db["status"] == 400:
            return {
                "status": db["status"],
                "error": db["error"]
            }
        if not db["data"]:
            return {
                "status": 404,
                "error": "The party you are lookng for does not exist"
            }
        return success(200, {
            "data": db["data"],
            "msg": "Office retrieved successfully"
        })

    def editSpecificParty(self):
        valid = validate(self.propertyName, self.data)
        if valid["isValid"] is False:
            return valid["data"]
        schema = SchemaGenerator(self.propertyName, self.data, self.id).updateSpecific()
        db = Database(schema).executeQuery()
        if db["status"] == 400:
            return {
                "status": db["status"],
                "error": db["error"]
            }
        if db["data"] < 1:
            return error(404, "The party was not found")
        return success(200, {
            "data": self.data,
            "msg": "Party edited successfully"
        })

    def deleteSpecificParty(self):
        schema = SchemaGenerator(self.propertyName, None, self.id).deleteSpecific()
        print(schema)
        db = Database(schema).executeQuery()
        if db["status"] == 400:
            return {
                "status": db["status"],
                "error": db["error"]
            }
        if db["data"] < 1:
            return error(404, "The party was not found")
        return success(200, {
            "msg": "Party deleted successfully"
        })
