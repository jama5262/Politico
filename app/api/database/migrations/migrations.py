from app.api.database.database import Database


schema = """

  DROP TABLE IF EXISTS petitions;
  DROP TABLE IF EXISTS office_results;
  DROP TABLE IF EXISTS votes;
  DROP TABLE IF EXISTS candidates;
  DROP TABLE IF EXISTS users;
  DROP TABLE IF EXISTS offices;
  DROP TABLE IF EXISTS parties;

  CREATE TABLE IF NOT EXISTS parties(
    id serial PRIMARY KEY,
    name VARCHAR (100) UNIQUE NOT NULL,
    abbr VARCHAR (100) NOT NULL,
    hq_Address VARCHAR (100) NOT NULL,
    logo_Url VARCHAR (100) NOT NULL
  );

  CREATE TABLE IF NOT EXISTS offices(
    id serial PRIMARY KEY,
    type VARCHAR (100) NOT NULL,
    name VARCHAR (100) UNIQUE NOT NULL
  );

  CREATE TABLE IF NOT EXISTS users(
    id serial PRIMARY KEY,
    first_name VARCHAR (100) NOT NULL,
    last_name VARCHAR (100) NOT NULL,
    other_name VARCHAR (100) NOT NULL,
    email VARCHAR (100) UNIQUE NOT NULL,
    password VARCHAR (100) NOT NULL,
    phone_Number VARCHAR (100) UNIQUE NOT NULL,
    passport_Url VARCHAR (100) NOT NULL,
    is_Admin BOOLEAN NOT NULL
  );

  CREATE TABLE IF NOT EXISTS candidates(
    id serial PRIMARY KEY,
    office INTEGER REFERENCES offices(id),
    party INTEGER REFERENCES parties(id),
    candidate INTEGER UNIQUE REFERENCES users(id)
  );

  CREATE TABLE IF NOT EXISTS votes(
    created_by INTEGER REFERENCES users(id),
    office INTEGER REFERENCES offices(id),
    candidate INTEGER REFERENCES candidates(id),
    created_On DATE NOT NULL DEFAULT NOW(),
    PRIMARY KEY (office, created_By)
  );

  CREATE TABLE IF NOT EXISTS office_results(
    id serial PRIMARY KEY,
    candidate INTEGER REFERENCES candidates(id),
    office INTEGER REFERENCES offices(id),
    result INTEGER NOT NULL
  );

  CREATE TABLE IF NOT EXISTS petitions(
    id serial PRIMARY KEY,
    created_By INTEGER REFERENCES users(id),
    office INTEGER REFERENCES offices(id),
    created_On DATE NOT NULL DEFAULT NOW(),
    text TEXT
  );

  INSERT INTO parties (name, abbr, hq_address, logo_url)
  VALUES ('Party Name 1', 'PT1', 'Address1', 'Logo1');
  INSERT INTO parties (name, abbr, hq_address, logo_url)
  VALUES ('Party Name 2', 'PT2', 'Address2', 'Logo2');

  INSERT INTO offices (name, type)
  VALUES ('Office Name 1', 'Type1');
  INSERT INTO offices (name, type)
  VALUES ('Office Name 2', 'Type2');
  
  INSERT INTO users (first_name, last_name, other_name, email, password, phone_number, passport_url, is_admin)
  VALUES ('Fname1', 'Lname1', 'Oname1', 'email1@gmail.com', 'pass1', 'phone1', 'passport_url1', 'no');
  INSERT INTO users (first_name, last_name, other_name, email, password, phone_number, passport_url, is_admin)
  VALUES ('Fname2', 'Lname2', 'Oname2', 'email2@gmail.com', 'pass2', 'phone2', 'passport_url2', 'yes');

  INSERT INTO candidates (office, party, candidate)
  VALUES (1, 2, 2);
  INSERT INTO candidates (office, party, candidate)
  VALUES (1, 2, 1);

  INSERT INTO votes (created_by, office, candidate)
  VALUES (1, 1, 2);
  INSERT INTO votes (created_by, office, candidate)
  VALUES (1, 2, 2);

  INSERT INTO office_results (candidate, office, result)
  VALUES (1, 2, 2);
  INSERT INTO office_results (candidate, office, result)
  VALUES (1, 2, 2);

  INSERT INTO petitions (created_By, office, text)
  VALUES (1, 1, 'Reason 1 here');
  INSERT INTO petitions (created_By, office, text)
  VALUES (2, 2, 'Reason 2 here');

"""


def migrate():
    return Database(schema).executeQuery()
