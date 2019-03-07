class SchemaGenerator():
    def __init__(self, tableName, columnName=None, data=None, id=None):
        self.tableName = tableName
        self.columnName = columnName
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
            SELECT * FROM """ + self.tableName + """ WHERE """ + self.columnName + """ = """ + self.id + """
        """

    def selectAll(self):
        return """
            SELECT * FROM """ + self.tableName + """
        """

    def updateSpecific(self):
        string = ""
        result = []
        count = 0
        for x in self.data:
            col = x
            row = self.data[x]
            string = col + " = '" + row + "'"
            result.append(string)
            count += 1
        output = str(tuple(result)).replace('"', '').replace('(', '').replace(')', '')
        if count <= 1:
            output = output.replace(",", "")
        return """
            UPDATE """ + self.tableName + """ 
            SET """ + output + """
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
