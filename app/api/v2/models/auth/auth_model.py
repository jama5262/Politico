from app.api.v2.utils.validations.validation import validate
from app.api.v2.utils.returnMessages import returnMessages

dataStore = {
  "users": {
      "1": {
          "id": 1,
          "firstname": "FirstName",
          "lastname": "LastName",
          "othername": "OtherName",
          "email": "Email",
          "phoneNumber": "PhoneNumber",
          "passportUrl": "Passport URL",
          "isAdmin": True
      },
      "2": {
          "id": 1,
          "firstname": "FirstName",
          "lastname": "LastName",
          "othername": "OtherName",
          "email": "Email",
          "phoneNumber": "PhoneNumber",
          "passportUrl": "Passport URL",
          "isAdmin": True
      }
  }
}


class AuthModel():
    def __init__(self, data=None, id=None):
        self.tableName = "users"
        self.data = data
        self.id = id

    def createUser(self):
        valid = validate(dataStore, self.tableName, "c", self.data, self.id)
        if valid["isValid"] is False:
            return valid["data"]
        dataStore[self.tableName][str(self.data["id"])] = self.data
        return returnMessages.success(201, self.data)
