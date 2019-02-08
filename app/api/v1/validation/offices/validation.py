def checkOfficeProperties(data):
    if all(x in data for x in ("id", "name", "type")):
        return True
    return False


def checkIfOfficesExits(data):
    if not data["Offices"]:
        return False
    return True


def checkIfOfficeExits(data, OfficeID):
    if OfficeID not in data["Offices"]:
        return False
    return True


def checkIfOfficeValuesAreEmpty(data):
    for x in data:
        if not data[x]:
            return False
    return True
