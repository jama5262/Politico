# Politico
[![Build Status](https://travis-ci.org/jama5262/Politico.svg?branch=develop)](https://travis-ci.org/jama5262/Politico)
[![Coverage Status](https://coveralls.io/repos/github/jama5262/Politico/badge.svg?branch=develop)](https://coveralls.io/github/jama5262/Politico?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/02b9aee071a0230097e2/maintainability)](https://codeclimate.com/github/jama5262/Politico/maintainability)

Politico enables citizens give their mandate to politicians running for different government offices while building trust in the process through transparency.

## Endpoints

Title | Endpoint | Method | Description
--- | --- | --- | ---
Create a party | /v1/parties | POST | An admin creates a party
Get all party | /v1/parties | GET | Get get all parties
Get specific party | /v1/parties/partyID | GET | Get a specific party
Edit specific party | /v1/parties/partyID | PATCH | Edit a specific party
Delete specific party | /v1/parties/partyID | DELETE | Delete a specific party
Create an office | /v1/offices | POST | An admin creates an office
Get all offices | /v1/offices/ | GET | Get all offices
Get specific office | /v1/parties/officeID | GET | Get a specific office

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

## Running the app

To run the app, simply key in the following
```
flask run
```

## Testing the app
To test the app, run the following

```
pytest
```

## Usage

It is recommended to use postman to send requests to the above detailed endpoints
### Party Endpoints
For this endpoint, minimum data required are as follows
```
{
  "id": 1,
  "name": "Party Name",
  "abbr": "Party Abbreviation",
  "logoUrl": "Party Image URL",
  "hqAddress": "Party HQ"
}
```
### Office Endpoints
For this endpoint, minimum data required are as follows
```
{
  "id": 1,
  "type": "Office type",
  "name": "Office name"
}
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.




















