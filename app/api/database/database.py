import psycopg2


class Database():
    def __init__(self, query):
        self.user = "postgres"
        self.password = "root"
        self.host = "localhost"
        self.port = "5432"
        self.database = "politico"
        self.query = query
  
    def executeQuery(self):
        try:
            conn = psycopg2.connect(user=self.user, password=self.password, host=self.host, port=self.port, database=self.database)
            cursor = conn.cursor()
            cursor.execute(self.query)
            conn.commit()
            return "table created"
        except (Exception, psycopg2.DatabaseError) as error:
            return error
