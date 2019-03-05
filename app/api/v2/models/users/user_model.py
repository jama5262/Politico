from app.api.v2.utils.returnMessages import returnMessages
from app.api.database.schemaGenerator.schemaGenerator import SchemaGenerator
from app.api.database.database import Database


class Users():
    def __init__(self, id=None):
        self.id = id

    def getSpecificUser(self):
        schema = SchemaGenerator("users", "id", None, self.id).selectSpecific()
        db = Database(schema, True).executeQuery()
        if db["status"] == 400:
            return {
                "status": db["status"],
                "error": db["error"]
            }
        if not db["data"]:
            return {
                "status": 404,
                "error": "The user was not found"
            }
        return returnMessages.success(200, {
            "data": db["data"],
            "msg": "User retrieved successfully"
        })

    def getAllUsers(self):
        schema = SchemaGenerator("users").selectAll()
        db = Database(schema, True).executeQuery()
        if db["status"] == 400:
            return {
                "status": db["status"],
                "error": db["error"]
            }
        if not db["data"]:
            return {
                "status": 404,
                "error": "Users where not found"
            }
        del db["data"][0]
        return returnMessages.success(200, {
            "data": db["data"],
            "msg": "All users retrieved successfully"
        })

    def getSpecificCandidate(self):
        schema = SchemaGenerator("candidates", "party", None, self.id).selectSpecific()
        db = Database(schema, True).executeQuery()
        if db["status"] == 400:
            return {
                "status": db["status"],
                "error": db["error"]
            }
        if not db["data"]:
            return {
                "status": 404,
                "error": "The candidate in this party was not found"
            }
        return returnMessages.success(200, {
            "data": db["data"],
            "msg": "Candidate retrieved successfully"
        })