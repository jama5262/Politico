from app.api.v2.utils.validations.validation import validate
from app.api.v2.utils.returnMessages import returnMessages
from app.api.database.schemaGenerator.schemaGenerator import SchemaGenerator
from app.api.database.database import Database

dataStore = {
  "users": {
      "1": {
          "id": 1,
          "firstname": "FirstName",
          "lastname": "LastName",
          "othername": "OtherName",
          "email": "Email 1",
          "phoneNumber": "PhoneNumber",
          "passportUrl": "Passport URL",
          "password": "pass1",
          "isAdmin": True
      },
      "2": {
          "id": 2,
          "firstname": "FirstName",
          "lastname": "LastName",
          "othername": "OtherName",
          "email": "Email 2",
          "phoneNumber": "PhoneNumber",
          "passportUrl": "Passport URL",
          "password": "pass2",
          "isAdmin": True
      },
      "3": {
          "id": 3,
          "firstname": "FirstName",
          "lastname": "LastName",
          "othername": "OtherName",
          "email": "Email 3",
          "phoneNumber": "PhoneNumber",
          "passportUrl": "Passport URL",
          "password": "pass3",
          "isAdmin": True
      }
  }
}


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
        print(schema)
        if db["status"] == 500:
            return {
                "status": db["status"],
                "error": db["error"]
            }
        if not db["data"]:
            return {
                "status": 404,
                "error": "404 (NotFound), The user does not exist"
            }
        return returnMessages.success(200, db["data"])
