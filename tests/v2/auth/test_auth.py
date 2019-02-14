import unittest
import json
from app import createApp
from app.api.database.migrations.migrations import migrate


class TestAuth(unittest.TestCase):
    def setUp(self):
        self.app = createApp("testing")
        self.client = self.app.test_client()
        self.endpoint = "/api/v2/auth"
        self.signupData = {
          "first_name": "FirstName",
          "last_name": "LastName",
          "other_name": "OtherName",
          "email": "email3@gmail.com",
          "phone_number": "PhoneNumber",
          "passport_url": "Passport URL",
          "password": "pass3",
          "is_admin": "yes"
        }
        self.signupDataEmpty = {
          "first_name": "",
          "last_name": "",
          "other_name": "",
          "email": "",
          "phone_number": "",
          "passport_url": "",
          "password": "",
          "is_admin": "yes"
        }
        self.signupDataNoProperty = {
          "first_name": "FirstName",
          "last_name": "LastName",
          "password": "pass3",
          "is_admin": "no"
        }
        self.loginData = {
          "email": "email1@gmail.com",
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

    def tearDown(self):
        migrate()

    def post(self, path, data):
        return self.client.post(path=path, data=json.dumps(data), content_type='application/json')

    def test_register_user(self):
        response = self.post(self.endpoint + "/signup", self.signupData)
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