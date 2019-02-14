from app.api.v2.utils.validations.validation import validate
from app.api.v2.utils.returnMessages import returnMessages
from app.api.database.schemaGenerator.schemaGenerator import SchemaGenerator
from app.api.database.database import Database


class AuthModel():
    def __init__(self, data=None, id=None):
        self.tableName = "users"
        self.data = data
        self.id = id

    def registerUser(self):
        valid = validate(self.tableName, self.data)
        if valid["isValid"] is False:
            return valid["data"]
        schema = SchemaGenerator(self.tableName, self.data).insterInto()
        db = Database(schema).executeQuery()
        if db["status"] == 500:
            return {
                "status": db["status"],
                "error": db["error"]
            }
        return returnMessages.success(200, self.data)

    def loginUser(self):
        valid = validate("userLogin", self.data)
        if valid["isValid"] is False:
            return valid["data"]
        schema = SchemaGenerator(self.tableName, self.data).userLogin()
        db = Database(schema, True).executeQuery()
        if db["status"] == 500:
            return {
                "status": db["status"],
                "error": db["error"]
            }
        if not db["data"]:
            return {
                "status": 401,
                "error": "401 (Unauthorized), Wrong login credentials"
            }
        return returnMessages.success(200, {
            "token": "sometokenhere",
            "user": db["data"]
        })
