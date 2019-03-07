import psycopg2
import re


class Database():
    def __init__(self, query, retrieve=False):
        self.query = query
        self.retrieve = retrieve
        self.conn = psycopg2.connect("postgres://jiduvlmktqoqzc:36ae1622f107d8f8f5b0641425ba417f1f29cf525b3b544db3136b8502117151@ec2-23-23-184-76.compute-1.amazonaws.com:5432/d88et68214thdv", sslmode='require')
  
    def executeQuery(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute(self.query)
            self.conn.commit()
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
              "data": cursor.rowcount
            }
        except (Exception, psycopg2.DatabaseError) as error:
            print(str(error))
            return {
                "error": "Error, " + re.match(r"[^[]*\[([^]]*)\]", str(error).replace("DETAIL:  Key ", "[").replace("\n", "]").replace('\"', "").replace(')', "").replace('(', "").replace(" in table users", "")).groups()[0],
                "status": 400
            }
        finally:
            if(self.conn):
                cursor.close()
                self.conn.close()
