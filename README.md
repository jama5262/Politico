# Politico
## Introduction

[![Build Status](https://travis-ci.org/jama5262/Politico.svg?branch=develop)](https://travis-ci.org/jama5262/Politico)
[![Coverage Status](https://coveralls.io/repos/github/jama5262/Politico/badge.svg?branch=develop)](https://coveralls.io/github/jama5262/Politico?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/02b9aee071a0230097e2/maintainability)](https://codeclimate.com/github/jama5262/Politico/maintainability)

Politico enables citizens give their mandate to politicians running for different government offices while building trust in the process through transparency.

This is the api endpoints branch

### Below are he endpoint for the Politico project

Title | Endpoint | Method | Description
--- | --- | --- | ---
Create a party | /v1/parties | POST | An admin creates a party
Get all party | /v1/parties | GET | Get get all parties
Get specific party | /v1/parties/partyID | GET | Get a specific party
Edit specific party | /v1/parties/partyID | PUT | Edit a specific party
Delete specific party | /v1/parties/partyID | DELETE | Delete a specific party
Create an office | /v1/offices | POST | An admin creates an office
Get all offices | /v1/offices/ | GET | Get all offices
Get specific office | /v1/parties/officeID | GET | Get a specific office

### Set up

Change to directory

`
cd Politico
`

Create an activate virtual environment

`
virtualenv venv
`

For windows key in the following command
`venv\Script\activate`

For mac key in 
`$ source venv/bin/activate`

#### Running the app

Next, just run this command to start up your app

`flask run`

#### Running the test

To run test simply run the following command

`pytest`
