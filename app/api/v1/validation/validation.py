tableList = ["parties", "offices"]


def checkIfTableExitst(tableName):
    if tableName not in tableList:
        return False
    return True


def checkIfPropertiesExist(data, tupleData):
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
