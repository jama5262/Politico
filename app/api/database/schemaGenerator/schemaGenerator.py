class SchemaGenerator():
    def __init__(self, tableName, data=None, id=None):
        self.tableName = tableName
        self.data = data
        self.id = id

    def insterInto(self):
        col = []
        row = []
        for x in self.data:
            col.append(x)
            row.append(self.data[x])
        return """
            INSERT INTO """ + self.tableName + """ """ + str(tuple(col)).replace("'", "") + """
            VALUES """ + str(tuple(row)) + """
        """

    def selectSpecific(self):
        return """
            SELECT * FROM """ + self.tableName + """ WHERE id = """ + self.id + """
        """

    def selectAll(self):
        return """
            SELECT * FROM """ + self.tableName + """
        """

    def updateSpecific(self):
        string = ""
        result = []
        for x in self.data:
            col = x
            row = self.data[x]
            string = col + " = '" + row + "'"
            result.append(string)

        return """
            UPDATE """ + self.tableName + """ 
            SET """ + str(tuple(result)).replace('"', '').replace('(', '').replace(')', '') + """
            WHERE id = """ + self.id + """
        """

    def deleteSpecific(self):
        return """
            DELETE FROM """ + self.tableName + """ WHERE id = """ + self.id + """
        """

    def userLogin(self):
        return """
            SELECT * FROM """ + self.tableName + """ WHERE email = '""" + self.data["email"] + """' AND password = '""" + self.data["password"] + """'
        """
