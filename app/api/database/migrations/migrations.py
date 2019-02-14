from app.api.database.database import Database


tables = """
  CREATE TABLE IF NOT EXISTS parties(
    id serial PRIMARY KEY,
    abbr VARCHAR (100) NOT NULL,
    name VARCHAR (100) UNIQUE NOT NULL,
    hqAddress VARCHAR (100) NOT NULL,
    logoUrl VARCHAR (100) NOT NULL
  );

  CREATE TABLE IF NOT EXISTS offices(
    id serial PRIMARY KEY,
    type VARCHAR (100) NOT NULL,
    name VARCHAR (100) UNIQUE NOT NULL
  );

  CREATE TABLE IF NOT EXISTS users(
    id serial PRIMARY KEY,
    firstname VARCHAR (100) NOT NULL,
    lastname VARCHAR (100) NOT NULL,
    othername VARCHAR (100) NOT NULL,
    email VARCHAR (100) NOT NULL,
    password VARCHAR (100) NOT NULL,
    phoneNumber VARCHAR (100) NOT NULL,
    passportUrl VARCHAR (100) NOT NULL,
    isAdmin BOOLEAN NOT NULL
  );

  CREATE TABLE IF NOT EXISTS candidates(
    id serial PRIMARY KEY,
    office INTEGER REFERENCES offices(id),
    party INTEGER REFERENCES parties(id),
    candidate INTEGER REFERENCES users(id)
  );

  CREATE TABLE IF NOT EXISTS votes(
    id serial PRIMARY KEY,
    createdOn TIMESTAMP NOT NULL,
    createdBy INTEGER REFERENCES users(id),
    office INTEGER REFERENCES offices(id),
    candidate INTEGER REFERENCES candidates(id)
  );

  CREATE TABLE IF NOT EXISTS petitions(
    id serial PRIMARY KEY,
    createdOn TIMESTAMP NOT NULL,
    createdBy INTEGER REFERENCES users(id),
    office INTEGER REFERENCES offices(id),
    text TEXT
  );
"""


def migrate():
    return Database(tables).executeQuery()
