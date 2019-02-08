def checkIfPropertiesExist(data, tuple):
    if all(x in data for x in tuple):
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
