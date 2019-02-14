from app.api.v2.utils.validations.validation import validate
from app.api.v2.utils.returnMessages import returnMessages
from app.api.database.schemaGenerator.schemaGenerator import SchemaGenerator
from app.api.database.database import Database


class PetitionModel():
    def __init__(self, data):
        self.data = data
        self.propertyName = "petitions"
 
    def createPetition(self):
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

    def getAllPetitions(self):
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
                "error": "404 (NotFound), petitions where not found"
            }
        return returnMessages.success(200, db["data"])
