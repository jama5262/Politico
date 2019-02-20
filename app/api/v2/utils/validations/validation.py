from app.api.v2.utils.returnMessages.returnMessages import error
import string
import re

propertyData = {
  "parties": ("name", "hq_address", "logo_url", "abbr"),
  "offices": ("name", "type"),
  "candidates": ("candidate", "office", "party"),
  "users": ("first_name", "last_name", "other_name", "email", "password", "phone_number", "passport_url"),
  "userLogin": ("email", "password"),
  "votes": ("office", "candidate", "created_by"),
  "petitions": ("office", "created_by", "text")
}

upperCaseProperties = ["name", "first_name", "last_name", "other_name", "type", "text"]
officeTypes = ("Federal", "Legislative", "State", "Local Government")


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


def checkIfValidEmail(data):
    if "email" in data:
        if re.match("[^@]+@[^@]+\.[^@]+", data["email"]) is None:
            return False
    return True


def checkIfValidPassword(data):
    if "password" in data:
        if len(data["password"]) < 6:
            return False
    return True


def checkIfValidPhoneNumber(data):
    if "phone_number" in data:
        phone_number = data["phone_number"]
        if not phone_number.startswith("07"):
            return False
        if len(phone_number) != 10:
            return False
    return True


def checkIfValidOfficeType(data):
    if "type" in data:
        if data["type"] not in officeTypes:
            return False
    return True


def checkIfValidUrl(data):
    if "passport_url" in data: 
        if re.match(r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+", data["passport_url"]) is None:
            return False
    if "logo_url" in data: 
        if re.match(r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+", data["logo_url"]) is None:
            return False
    return True


def validate(propertyName, data):
    if checkIfPropertiesExists(propertyName, data) is False:
        return {
            "isValid": False,
            "data": error(403, "Please make sure to enter the correct requests, which are " + str(propertyData[propertyName]))
        }
    if checkIfUneededPropertiesExists(propertyName, data) is False:
        return {
            "isValid": False,
            "data": error(403, "Please make sure to enter the correct requests, which are " + str(propertyData[propertyName]))
        }
    if checkIfPropertyValuesAreEmpty(data) is False:
        return {
            "isValid": False,
            "data": error(403, "Please make sure the values are not empty, and that you have valid syntax")
        }
    if checkIfOnlyHasSpace(data) is True:
        return {
            "isValid": False,
            "data": error(403, "Please make sure the values do not have whitespaces")
        }
    if checkIfValidEmail(data) is False:
        return {
            "isValid": False,
            "data": error(403, "Please make sure you have a valid email syntax")
        }
    if checkIfValidPassword(data) is False:
        return {
            "isValid": False,
            "data": error(403, "Please make sure the password is more than 6 characters")
        }
    if checkIfValidPhoneNumber(data) is False:
        return{
            "isValid": False,
            "data": error(403, "Please make sure you have a valid phone number syntax")
        }
    if checkIfValidOfficeType(data) is False:
        return{
            "isValid": False,
            "data": error(403, "Please make sure you have the correct office type which are,  " + str(officeTypes))
        }
    if checkIfValidUrl(data) is False:
        return{
            "isValid": False,
            "data": error(403, "Please make sure you have a valid url syntax")
        }
    return {
        "isValid": True
    }
