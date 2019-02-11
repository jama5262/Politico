tableList = ["parties", "offices"]
propertyData = {
  "parties": ("id", "name", "hqAddress", "logoUrl", "abbr"),
  "offices": ("id", "name", "type")
}


def validate(dataStore, tableName, operation, data=None, id=None):
    if checkIfTableExists(tableName) is False:
        return {
            "isValid": False,
            "data": {
                "status": 404,
                "error": "404 (Not Found), The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again."
            }
        }
    if data is not None or id is not None:
        if checkIfDataExists(dataStore[tableName], id) is False and operation != "c":
            return {
                "isValid": False,
                "data": {
                    "status": 404,
                    "error": "404 (Not Found), The " + tableName + " you are looking for does not exist"
                }
            }
        if operation == "c" or operation == "u":
            if checkIfPropertiesExists(data, propertyData[tableName]) is False:
               return {
                    "isValid": False,
                    "data": {
                        "status": 422,
                        "error": "422 (Unprocessable Entity), Please make sure to enter the correct requests, which are " + str(propertyData[tableName])
                    }
                }
            elif checkIfPropertyValuesAreEmpty(data) is False:
                return {
                    "isValid": False,
                    "data": {
                        "status": 422,
                        "error": "422 (Unprocessable Entity), Please make sure the values are not empty, and that you have valid syntax"
                    }
                }
    else:
        if checkIfAllDataExists(dataStore[tableName]) is False:
            return {
                "isValid": False,
                "data": {
                    "status": 404,
                    "error": "404 (Not Found), " + tableName + " data were not found"
                }
            }
    return {
        "isValid": True
    }


def checkIfTableExists(tableName):
    if tableName not in tableList:
        return False
    return True


def checkIfPropertiesExists(data, tupleData):
    if all(x in data for x in tupleData):
        return True
    return False


def checkIfPropertyValuesAreEmpty(data):
    for x in data:
        if not data[x]:
            return False
    return True


def checkIfDataExists(data, id):
    if id not in data:
        return False
    return True


def checkIfAllDataExists(data):
    if not data:
        return False
    return True
