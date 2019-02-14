from app.api.v2.utils.validations.validation import validate
from app.api.v2.utils.returnMessages.returnMessages import success
from app.api.database.schemaGenerator.schemaGenerator import SchemaGenerator
from app.api.database.database import Database


class VoteModel():
    def __init__(self, data):
        self.data = data
        self.propertyName = "votes"

    def createVote(self):
        valid = validate(self.propertyName, self.data)
        if valid["isValid"] is False:
            return valid["data"]
        schema = SchemaGenerator(self.propertyName, self.data).insterInto()
        db = Database(schema).executeQuery()
        if db["status"] == 500:
            return {
                "status": db["status"],
                "error": db["error"]
            }
        return success(200, self.data)
