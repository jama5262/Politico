from app.api.v2.utils.validations.validation import validate
from app.api.v2.utils.validations.validation import checkIfValuesHaveFirstLetterUpperCase
from app.api.v2.utils.returnMessages import returnMessages
from app.api.database.schemaGenerator.schemaGenerator import SchemaGenerator
from app.api.database.database import Database


class AuthModel():
    def __init__(self, data=None, id=None):
        self.tableName = "users"
        if data is not None:
            self.data = checkIfValuesHaveFirstLetterUpperCase(data)
        self.id = id

    def registerUser(self):
        valid = validate(self.tableName, self.data)
        if valid["isValid"] is False:
            return valid["data"]
        schema = SchemaGenerator(self.tableName, self.data).insterInto()
        db = Database(schema).executeQuery()
        if db["status"] == 400:
            return {
                "status": db["status"],
                "error": db["error"]
            }
        return returnMessages.success(200, {
            "user": self.data
        })

    def loginUser(self):
        valid = validate("userLogin", self.data)
        if valid["isValid"] is False:
            return valid["data"]
        schema = SchemaGenerator(self.tableName, self.data).userLogin()
        db = Database(schema, True).executeQuery()
        if db["status"] == 400:
            return {
                "status": db["status"],
                "error": db["error"]
            }
        if not db["data"]:
            return {
                "status": 401,
                "error": "Wrong login credentials"
            }
        db["data"][0].pop("password")
        return returnMessages.success(200, {
            "user": db["data"][0]
        })
