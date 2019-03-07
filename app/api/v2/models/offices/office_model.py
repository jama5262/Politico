from app.api.v2.utils.validations.validation import validate
from app.api.v2.utils.validations.validation import checkIfValuesHaveFirstLetterUpperCase
from app.api.v2.utils.returnMessages import returnMessages
from app.api.database.schemaGenerator.schemaGenerator import SchemaGenerator
from app.api.database.database import Database


class OfficeModel():
    def __init__(self, data=None, id=None):
        self.propertyName = "offices"
        if data is not None:
            self.data = checkIfValuesHaveFirstLetterUpperCase(data)
        self.id = id

    def createOffice(self):
        print(self.data)
        valid = validate(self.propertyName, self.data)
        if valid["isValid"] is False:
            return valid["data"]
        schema = SchemaGenerator(self.propertyName, None, self.data).insterInto()
        db = Database(schema).executeQuery()
        if db["status"] == 400:
            return {
                "status": db["status"],
                "error": db["error"]
            }
        return returnMessages.success(200, {
            "data": self.data,
            "msg": "Office created successfully"
        })

    def getAllOffices(self):
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
                "error": "Offices where not found"
            }
        return returnMessages.success(200, {
            "data": db["data"],
            "msg": "All offices retrieved successfully"
        })

    def getSpecificOffice(self):
        schema = SchemaGenerator(self.propertyName, "id", None, self.id).selectSpecific()
        db = Database(schema, True).executeQuery()
        if db["status"] == 400:
            return {
                "status": db["status"],
                "error": db["error"]
            }
        if not db["data"]:
            return {
                "status": 404,
                "error": "The office was not found"
            }
        return returnMessages.success(200, {
            "data": db["data"],
            "msg": "Office retrieved successfully"
        })

    def editSpecificOffice(self):
        valid = validate(self.propertyName, self.data)
        if valid["isValid"] is False:
            return valid["data"]
        schema = SchemaGenerator(self.propertyName, None, self.data, self.id).updateSpecific()
        print(schema)
        db = Database(schema).executeQuery()
        if db["status"] == 400:
            return {
                "status": db["status"],
                "error": db["error"]
            }
        if db["data"] < 1:
            return returnMessages.error(404, "The office was not found")
        return returnMessages.success(200, {
            "data": self.data,
            "msg": "Office edited successfully"
        })

    def deleteSpecificOffice(self):
        schema = SchemaGenerator(self.propertyName, None, None, self.id).deleteSpecific()
        print(schema)
        db = Database(schema).executeQuery()
        if db["status"] == 400:
            return {
                "status": db["status"],
                "error": db["error"]
            }
        if db["data"] < 1:
            return returnMessages.error(404, "The office was not found")
        return returnMessages.success(200, {
            "msg": "Office deleted successfully"
        })

    def userRegisterToOffice(self):
        valid = validate("candidates", self.data)
        if valid["isValid"] is False:
            return valid["data"]
        schema = SchemaGenerator("candidates", None, self.data).insterInto()
        db = Database(schema).executeQuery()
        if db["status"] == 400:
            return {
                "status": db["status"],
                "error": db["error"]
            }
        return returnMessages.success(200, {
            "data": self.data,
            "msg": "User registered successfully as a candidate"
        })

    def officeResults(self):
        schema = SchemaGenerator("votes", "office", None, self.id).selectSpecific()
        db = Database(schema, True).executeQuery()
        if db["status"] == 400:
            return {
                "status": db["status"],
                "error": db["error"]
            }
        if not db["data"]:
            return {
                "status": 404,
                "error": "The office you are lookng for does not exist"
            }
        candSet = set()
        officeResults = []
        for candidate in db["data"]:
            candSet.add(candidate["candidate"])

        for aSet in candSet:
            result = 0
            for candidate in db["data"]:
                if aSet == candidate["candidate"]:
                    result += 1
            officeResults.append({
                "office": self.id,
                "candidate": aSet,
                "result": result
            })
        return returnMessages.success(200, {
            "data": officeResults,
            "msg": "Office results retrieved successfully"
        })
