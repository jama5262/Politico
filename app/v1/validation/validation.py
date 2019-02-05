def checkForParty(data):
    if all(x in data for x in ("id", "name", "hqAddress", "logoUrl")):
        return True
    return False
