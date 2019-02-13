import unittest
import json
from app import createApp


class TestAuth(unittest.TestCase):
    def setUp(self):
        self.app = createApp("testing")
        self.client = self.app.test_client()
        self.endpoint = "/api/v2/auth"
        self.signupData = {
          "id": 3,
          "firstname": "FirstName",
          "lastname": "LastName",
          "othername": "OtherName",
          "email": "Email 2",
          "phoneNumber": "PhoneNumber",
          "passportUrl": "Passport URL",
          "password": "pass3",
          "isAdmin": True
        }
        self.signupDataEmpty = {
          "id": 3,
          "firstname": "",
          "lastname": "",
          "othername": "",
          "email": "",
          "phoneNumber": "",
          "passportUrl": "",
          "password": "",
          "isAdmin": True
        }
        self.signupDataNoProperty = {
          "id": 3,
          "firstname": "FirstName",
          "lastname": "LastName",
          "password": "pass3",
          "isAdmin": True
        }
        self.loginData = {
          "email": "Email 1",
          "password": "pass1"
        }
        self.loginDataEmpty = {
          "email": "",
          "password": ""
        }
        self.loginDataNoProperty = {
          "email": "Email 1",
        }
        self.wrongLoginData = {
          "email": "Email 1",
          "password": "pass2"
        }

    def post(self, path, data):
        return self.client.post(path=path, data=json.dumps(data), content_type='application/json')

    def test_register_user(self):
        response = self.post(self.endpoint + "/signup", self.signupData)
        self.assertTrue(response.json["data"]["id"])
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.post(self.endpoint + "/login", self.loginData)
        self.assertEqual(response.status_code, 200)

    def test_wrong_login(self):
        response = self.post(self.endpoint + "/login", self.wrongLoginData)
        self.assertEqual(response.status_code, 401)

    def test_with_empty_values_signup(self):
        response = self.post(self.endpoint + "/signup", self.signupDataEmpty)
        self.assertEqual(response.status_code, 422)

    def test_with_no_name_property_signup(self):
        response = self.post(self.endpoint + "/signup", self.signupDataNoProperty)
        self.assertEqual(response.status_code, 422)

    def test_with_empty_values_login(self):
        response = self.post(self.endpoint + "/login", self.loginDataEmpty)
        self.assertEqual(response.status_code, 422)

    def test_with_no_name_property_login(self):
        response = self.post(self.endpoint + "/login", self.loginDataNoProperty)
        self.assertEqual(response.status_code, 422)