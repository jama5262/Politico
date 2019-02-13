from app.api.v2.utils.validations.validation import validate
from app.api.v2.utils.returnMessages import returnMessages

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
        valid = validate("usersRegister", self.data)
        if valid["isValid"] is False:
            return valid["data"]
        dataStore[self.tableName][str(self.data["id"])] = self.data
        return returnMessages.success(200, self.data)

    def loginUser(self):
        valid = validate("userLogin", self.data)
        if valid["isValid"] is False:
            return valid["data"]
        for user in dataStore["users"]:
            if dataStore["users"][user]["email"] == self.data["email"]:
                if dataStore["users"][user]["password"] == self.data["password"]:
                    return returnMessages.success(200, {
                        "token": "some_token_here",
                        "user": dataStore["users"][user]
                    })
                else:
                    return returnMessages.error(401, "401 (Unauthorized), Wrong credentials")
                break
            else:
                return returnMessages.error(404, "404 (NotFound), The user does not exist")