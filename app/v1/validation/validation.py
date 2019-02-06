# PARTY VALIDATION
def checkPartyProperties(data):
    if all(x in data for x in ("id", "name", "hqAddress", "logoUrl", "abbr")):
        return True
    return False


def checkIfPartiesExits(data):
    if not data["Parties"]:
        return False
    return True


def checkIfPartyExits(data, partyID):
    if partyID not in data["Parties"]:
        return False
    return True


# OFFICE VALIDATION
def checkOfficeProperties(data):
    if all(x in data for x in ("id", "name", "type")):
        return True
    return False


def checkIfOfficesExits(data):
    if not data["Offices"]:
        return False
    return True
