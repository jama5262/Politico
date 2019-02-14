import psycopg2


class Database():
    def __init__(self, query, retrieve=False):
        self.user = "postgres"
        self.password = "root"
        self.host = "localhost"
        self.port = "5432"
        self.database = "politico"
        self.query = query
        self.retrieve = retrieve
  
    def executeQuery(self):
        try:
            conn = psycopg2.connect(user=self.user, password=self.password, host=self.host, port=self.port, database=self.database)
            cursor = conn.cursor()
            cursor.execute(self.query)
            conn.commit()
            if self.retrieve is True:
                col = [desc[0] for desc in cursor.description]
                results = []
                for row in cursor.fetchall():
                    results.append(dict(zip(col, row)))
                return {
                  "status": 200,
                  "data": results
                }
            return {
              "status": 200,
              "data": "success"
            }
        except (Exception, psycopg2.DatabaseError) as error:
            return {
              "status": 500,
              "error": "Database error => " + str(error)
            }
        finally:
            if(conn):
                cursor.close()
                conn.close()
