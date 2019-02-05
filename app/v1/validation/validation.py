def checkForCreateParty(data):
    if all(x in data for x in ("id", "name", "hqAddress", "logoUrl")):
        return True
    return False


def checkForGetAllParties(data):
    if not data:
        return False
    return True
