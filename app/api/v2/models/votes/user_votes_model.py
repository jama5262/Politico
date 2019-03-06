from app.api.v2.utils.validations.validation import validate
from app.api.v2.utils.returnMessages.returnMessages import success
from app.api.database.schemaGenerator.schemaGenerator import SchemaGenerator
from app.api.database.database import Database


class VoteModel():
    def __init__(self, data, id=None):
        self.data = data
        self.propertyName = "votes"
        self.id = id

    def createVote(self):
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
        return success(200, {
            "data": self.data,
            "msg": "Vote created successfully"
        })

    def getAllVotes(self):
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
                "error": "Votes where not found"
            }
        return success(200, {
            "data": db["data"],
            "msg": "All Votes retrieved successfully"
        })

    def getSpecificVote(self):
        schema = SchemaGenerator(self.propertyName, "created_by", None, self.id).selectSpecific()
        db = Database(schema, True).executeQuery()
        if db["status"] == 400:
            return {
                "status": db["status"],
                "error": db["error"]
            }
        if not db["data"]:
            return {
                "status": 404,
                "error": "The vote was not found"
            }
        return returnMessages.success(200, {
            "data": db["data"],
            "msg": "Votes retrieved successfully"
        })
