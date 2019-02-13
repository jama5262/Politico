from app.api.v2.utils.validations.validation import validate
from app.api.v2.utils.returnMessages import returnMessages

dataStore = {
  "petitions": {
    "1": {
      "id": 1,
      "office": 1,
      "createdBy": 1,
      "text": "Reason for petition",
      "evidence": "Petition evidence"
    },
    "2": {
      "id": 2,
      "office": 1,
      "createdBy": 1,
      "text": "Reason for petition",
      "evidence": "Petition evidence"
    }
  }
}


class PetitionModel():
    def __init__(self, data):
        self.data = data
        self.propertyName = "petitions"
 
    def createPetition(self):
        valid = validate(self.propertyName, self.data)
        if valid["isValid"] is False:
            return valid["data"]
        dataStore[self.propertyName][str(self.data["id"])] = self.data
        return returnMessages.success(200, self.data)

    def getAllPetitions(self):
        return returnMessages.success(200, dataStore[self.propertyName])
