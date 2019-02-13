from app.api.v2.utils.returnMessages.returnMessages import error

propertyData = {
  "parties": ("id", "name", "hqAddress", "logoUrl", "abbr"),
  "offices": ("id", "name", "type"),
  "officeMembers": ("user"),
  "usersRegister": ("id", "firstname", "lastname", "othername", "email", "phoneNumber", "passportUrl", "isAdmin"),
  "userLogin": ("email", "password"),
  "votes": ("office", "candidate", "voter"),
  "petitions": ("id", "office", "createdBy", "text", "evidence")
}


def validate(propertyName, data):
    if checkIfPropertiesExists(propertyName, data) is False:
        return {
            "isValid": False,
            "data": error(422, "422 (Unprocessable Entity), Please make sure to enter the correct requests, which are " + str(propertyData[propertyName]))
        }
    if checkIfPropertyValuesAreEmpty(data) is False:
        return {
            "isValid": False,
            "data": error(422, "422 (Unprocessable Entity), Please make sure the values are not empty, and that you have valid syntax")
        }
    return {
        "isValid": True
    }


def checkIfPropertiesExists(propertyName, data):
    if all(x in data for x in propertyData[propertyName]):
        return True
    return False


def checkIfPropertyValuesAreEmpty(data):
    for x in data:
        if not data[x]:
            return False
    return True
