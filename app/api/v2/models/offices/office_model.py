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
        if db["data"] < 1:
            return returnMessages.error(404, "404 (Not Found) The party was not found")
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
        if db["data"] < 1:
            return returnMessages.error(404, "404 (Not Found) The party was not found")
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
        return returnMessages.success(200, self.data)

    def officeResults(self):
        schema = SchemaGenerator("office_results", None, self.id).selectSpecificOfficeResult()
        db = Database(schema, True).executeQuery()
        if db["status"] == 500:
            return {
                "status": db["status"],
                "error": db["error"]
            }
        if not db["data"]:
            return {
                "status": 404,
                "error": "404 (NotFound), The party you are lookng for does not exist"
            }
        return returnMessages.success(200, db["data"])
