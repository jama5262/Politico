from app.api.v2.utils.returnMessages.returnMessages import error

propertyData = {
  "parties": ("name", "hqAddress", "logoUrl", "abbr"),
  "offices": ("name", "type"),
  "candidates": ("candidate", "office", "party"),
  "users": ("first_name", "last_name", "other_name", "email", "password", "phone_number", "passport_url", "is_admin"),
  "userLogin": ("email", "password"),
  "votes": ("office", "candidate", "createdby"),
  "petitions": ("office", "created_By", "text")
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
