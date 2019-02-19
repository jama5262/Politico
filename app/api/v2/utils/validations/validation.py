from app.api.v2.utils.returnMessages.returnMessages import error
import string

propertyData = {
  "parties": ("name", "hq_address", "logo_url", "abbr"),
  "offices": ("name", "type"),
  "candidates": ("candidate", "office", "party"),
  "users": ("first_name", "last_name", "other_name", "email", "password", "phone_number", "passport_url", "is_admin"),
  "userLogin": ("email", "password"),
  "votes": ("office", "candidate", "created_by"),
  "petitions": ("office", "created_by", "text")
}

upperCaseProperties = ["name", "first_name", "last_name", "other_name", "type", "text"]


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
    if checkIfOnlyHasSpace(data) is True:
        return {
            "isValid": False,
            "data": error(422, "422 (Unprocessable Entity), Please make sure the values do not have whitespaces")
        }
    if checkIfUneededPropertiesExists(propertyName, data) is False:
        return {
            "isValid": False,
            "data": error(422, "422 (Unprocessable Entity), Please make sure to enter the correct requests, which are " + str(propertyData[propertyName]))
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


def checkIfUneededPropertiesExists(propertyName, data):
    for x in data:
        if x not in propertyData[propertyName]:
            return False
    else:
        return True


def checkIfOnlyHasSpace(data):
    for x in data:
        if isinstance(data[x], str):
            if data[x].isspace():
                return True
    else:
        return False


def checkIfValuesHaveFirstLetterUpperCase(data):
    for x in data:
        if isinstance(data[x], str):
            if x in upperCaseProperties:
                data[x] = data[x].title()
    return data
