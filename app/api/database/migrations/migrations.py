from app.api.database.database import Database


schema = """

  DROP TABLE IF EXISTS petitions CASCADE;
  DROP TABLE IF EXISTS votes CASCADE;
  DROP TABLE IF EXISTS candidates CASCADE;
  DROP TABLE IF EXISTS users CASCADE;
  DROP TABLE IF EXISTS offices CASCADE;
  DROP TABLE IF EXISTS parties CASCADE;

  CREATE TABLE IF NOT EXISTS parties(
    id serial PRIMARY KEY,
    name VARCHAR (100) UNIQUE NOT NULL,
    abbr VARCHAR (100) NOT NULL,
    hq_Address VARCHAR (100) NOT NULL,
    logo_Url VARCHAR (255) NOT NULL
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
    passport_Url VARCHAR (255) NOT NULL,
    is_Admin BOOLEAN DEFAULT 'no'
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

  CREATE TABLE IF NOT EXISTS petitions(
    id serial PRIMARY KEY,
    created_By INTEGER REFERENCES users(id),
    office INTEGER REFERENCES offices(id),
    created_On DATE NOT NULL DEFAULT NOW(),
    text TEXT
  );

  INSERT INTO parties (name, abbr, hq_address, logo_url)
  VALUES ('Kenya African National Union', 'KANU', 'Nairobi', 'https://upload.wikimedia.org/wikipedia/en/7/77/Kenya_African_National_Union.gif');
  INSERT INTO parties (name, abbr, hq_address, logo_url)
  VALUES ('Wiper Democratic Movement', 'WDM', 'Nairobi', 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Wiper_kenya_wdm_logo.png/180px-Wiper_kenya_wdm_logo.png');
  INSERT INTO parties (name, abbr, hq_address, logo_url)
  VALUES ('Party of National Unity', 'PNU', 'Nairobi', 'https://scontent.fnbo2-1.fna.fbcdn.net/v/t1.0-9/15107266_1641931199440720_3113004755651256116_n.jpg?_nc_cat=101&_nc_ht=scontent.fnbo2-1.fna&oh=dd470a86f4183893c1162706e1cc6657&oe=5D251F27');
  INSERT INTO parties (name, abbr, hq_address, logo_url)
  VALUES ('Forum for the Restoration of Democracy', 'FRD', 'Nairobi', 'https://upload.wikimedia.org/wikipedia/en/thumb/1/17/FORD_-_KENYA_logo.png/150px-FORD_-_KENYA_logo.png');
  INSERT INTO parties (name, abbr, hq_address, logo_url)
  VALUES ('National Rainbow Coalition', 'NARK', 'Nairobi', 'https://upload.wikimedia.org/wikipedia/en/5/52/Narc_Kenya_logo.jpg');
  INSERT INTO parties (name, abbr, hq_address, logo_url)
  VALUES ('Chama Cha Uzalendo', 'CCU', 'Nairobi', 'https://pbs.twimg.com/profile_images/801425724473278464/DC0sw8GL_400x400.jpg');

  INSERT INTO offices (name, type)
  VALUES ('Ministry of Defence', 'State');
  INSERT INTO offices (name, type)
  VALUES ('Ministry of Foreign Affairs', 'State');
  INSERT INTO offices (name, type)
  VALUES ('Ministry of Industry, Trade & Co-operatives', 'State');
  INSERT INTO offices (name, type)
  VALUES ('Ministry of Health', 'State');
  INSERT INTO offices (name, type)
  VALUES ('Ministry of Devolution and the ASALS', 'State');
  INSERT INTO offices (name, type)
  VALUES ('Ministry of Education', 'State');

  INSERT INTO users (first_name, last_name, other_name, email, password, phone_number, passport_url, is_admin)
  VALUES ('Admin', 'Admin', 'Admin', 'admin@gmail.com', 'adminpass', '0700000000', 'https://cdn3.iconfinder.com/data/icons/vector-icons-6/96/256-512.png', 'yes');
  INSERT INTO users (first_name, last_name, other_name, email, password, phone_number, passport_url, is_admin)
  VALUES ('Izuku', 'Mydoriya', 'Mha', 'email1@gmail.com', 'password1', '0711111111', 'https://66.media.tumblr.com/71a49cd9ce18be4882d09e735576cbe6/tumblr_ouiy06T2zb1tm5eijo2_250.png', 'no');
  INSERT INTO users (first_name, last_name, other_name, email, password, phone_number, passport_url, is_admin)
  VALUES ('Mob', 'Psycho', 'Hundred', 'email2@gmail.com', 'password1', '0711111112', 'https://vignette.wikia.nocookie.net/mob-psycho-100/images/8/8c/Mob_anime.png/revision/latest/scale-to-width-down/250?cb=20160712054631', 'no');
  INSERT INTO users (first_name, last_name, other_name, email, password, phone_number, passport_url, is_admin)
  VALUES ('One', 'Punch', 'Man', 'email3@gmail.com', 'password1', '0711111113', 'https://avatarfiles.alphacoders.com/468/thumb-46807.png', 'no');
  INSERT INTO users (first_name, last_name, other_name, email, password, phone_number, passport_url, is_admin)
  VALUES ('Asta', 'Yami', 'Yuno', 'email4@gmail.com', 'password1', '0711111114', 'https://art.pixilart.com/34fccbb7c9a83f1.png', 'no');
  INSERT INTO users (first_name, last_name, other_name, email, password, phone_number, passport_url, is_admin)
  VALUES ('All', 'Might', 'PlusUltra', 'email5@gmail.com', 'password1', '0711111115', 'https://pbs.twimg.com/media/DGRwW3ZUIAAQREF.jpg', 'no');
  INSERT INTO users (first_name, last_name, other_name, email, password, phone_number, passport_url, is_admin)
  VALUES ('John', 'Doe', 'Okay', 'email6@gmail.com', 'password1', '0711111116', 'https://cdn3.iconfinder.com/data/icons/vector-icons-6/96/256-512.png', 'no');

  INSERT INTO candidates (office, party, candidate)
  VALUES (1, 2, 2);
  INSERT INTO candidates (office, party, candidate)
  VALUES (2, 1, 5);
  INSERT INTO candidates (office, party, candidate)
  VALUES (3, 1, 3);
  INSERT INTO candidates (office, party, candidate)
  VALUES (1, 2, 4);

  INSERT INTO votes (created_by, office, candidate)
  VALUES (1, 1, 2);

  INSERT INTO petitions (created_By, office, text)
  VALUES (1, 1, 'Reason 1 here');
  INSERT INTO petitions (created_By, office, text)
  VALUES (2, 3, 'Reason 2 here');
  INSERT INTO petitions (created_By, office, text)
  VALUES (5, 1, 'Reason 3 here');
  INSERT INTO petitions (created_By, office, text)
  VALUES (3, 2, 'Reason 4 here');
"""


def migrate():
    return Database(schema).executeQuery()
