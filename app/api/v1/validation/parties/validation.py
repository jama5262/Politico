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


def checkIfPartyValuesAreEmpty(data):
    for x in data:
        if not data[x]:
            return False
    return True