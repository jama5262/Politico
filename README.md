# Politico
[![Build Status](https://travis-ci.org/jama5262/Politico.svg?branch=develop)](https://travis-ci.org/jama5262/Politico)
[![Coverage Status](https://coveralls.io/repos/github/jama5262/Politico/badge.svg?branch=develop)](https://coveralls.io/github/jama5262/Politico?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/02b9aee071a0230097e2/maintainability)](https://codeclimate.com/github/jama5262/Politico/maintainability)

Politico enables citizens give their mandate to politicians running for different government offices while building trust in the process through transparency.

## API Documentation
[API Documentation Link](https://documenter.getpostman.com/view/572556/S11Ex16o)

## Run in postman
[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/bccd4c976a5efc9dbbad)

## Endpoints

Title | Endpoint | Method | Description
--- | --- | --- | ---
Sign up user | /api/v2/auth/signup | POST | User can sign up
Login User | /api/v2/auth/login | POST |User can login
Create a party | /api/v2/parties | POST | An admin creates a party
Get all party | /api/v2/parties | GET | Get get all parties
Get specific party | /api/v2/parties/partyID | GET | Get a specific party
Edit specific party | /api/v2/parties/partyID | PATCH | Edit a specific party
Delete specific party | /api/v2/parties/partyID | DELETE | Delete a specific party
Create an office | /api/v2/offices | POST | An admin creates an office
Get all offices | /api/v2/offices/ | GET | Get all offices
Get specific office | /api/v2/offices/officeID | GET | Get a specific office
Edit specific office | /api/v2/offices/officeID | PATCH | Edit a specific office
Delete specific office | /api/v2/offices/officeID | DELETE | Delete a specific office
Register candidate | /api/v2/offices/officeID/register | POST | A politician can register as a candidate
Vote | /api/v2/votes | POST | A user can vote for the candidate
Get specific office results | /api/v2/offices/officeID/result | GET | Get a specific office results after election
Create a petition | /api/v2/petitions | POST | Create a petition for a concluded election
Get all petitions | /api/v2/petitions | GET | Get get all petitions


## Installation

Clone the repo, and cd into it

```
cd Politico
```
Create your virtual environment

```
virtualenv venv
```
For windows key in the following command
```
venv\Script\activate
```

For mac key in 
```
$ source venv/bin/activate
```
## Installing packages
To install packages run the following
```
pip install -r requirements.txt
```
## Create .env file and add the following
Sign up for SENDGRID and create api key and add to .env file
```
export FLASK_APP="run.py"
export FLASK_ENV="development"
export APP_SETTINGS="development"
export SEND_GRID="YOUR_SEND_GRID_API_KEY"
```
## Running the app

To run the app, simply key in the following
```
flask run
```

## Testing the app
To test the app, run the following

```
pytest -v
```

## Usage

It is recommended to use postman to send requests to the above detailed endpoints
### Party Endpoints
For this endpoint, minimum data required are as follows
```
{
  “id” : Integer,
  “name” : String,
  “hq_address” : String,
  “logo_url” : String,
}
```
### Office Endpoints
For this endpoint, minimum data required are as follows
```
{
  “id” : Integer,
  “type” : String, // federal, legislative, state, or local government
  “name” : String,
}
```
### User Endpoints
For this endpoint, minimum data required are as follows
```
{
  “id” : Integer,
  “first_name” : String,
  “last_name” : String,
  “other_name” : String,
  “email” : String,
  ”phone_number” : String,
  “passport_url” : String,
  “is_admin” : Boolean,
}
```
### Candidates Endpoints
For this endpoint, minimum data required are as follows
```
{
  “id” : Integer,
  “office” : Integer, // represents the office’s id
  “party” : Integer, // represents the party’s id
  “candidate” : Integer,
}
```
### Votes Endpoints
For this endpoint, minimum data required are as follows
```
{
  “id” : Integer,
  “created_on” : Date,
  “created_by” : Integer, // represents the voter’s id
  “office” : Integer, // represents the office being voted for
  “candidate” : Integer,
}
```
### Petition Endpoints
For this endpoint, minimum data required are as follows
```
{
  “id” : Integer,
  “created_n” : Date,
  “created_y” : Integer, // represents the citizen who created the petition
  “office” : Integer, // represents the office which election held for
  “text” : String,
}
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.




















