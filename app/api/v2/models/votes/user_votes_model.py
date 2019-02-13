from app.api.v2.utils.validations.validation import validate
from app.api.v2.utils.returnMessages.returnMessages import success

dataStore = {
  "votes": {
    "1": {
      "office": 1,
      "candidate": 1,
      "voter": 1
    },
    "2": {
      "office": 2,
      "candidate": 3,
      "voter": 2
    }
  }
}


class VoteModel():
    def __init__(self, data):
        self.data = data
        self.propertyName = "votes"

    def createVote(self):
        valid = validate(self.propertyName, self.data)
        if valid["isValid"] is False:
            return valid["data"]
        voterID = len(dataStore["votes"]) + 1
        dataStore["votes"][voterID] = self.data
        return success(200, self.data)
