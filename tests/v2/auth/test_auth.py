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
          "first_name": "FirstName4",
          "last_name": "LastName4",
          "other_name": "OtherName4",
          "email": "email10@gmail.com",
          "phone_number": "0711111133",
          "passport_url": "https://cdn3.iconfinder.com/data/icons/vector-icons-6/96/256-512.png",
          "password": "password3"
        }
        self.signupDataEmpty = {
          "first_name": "",
          "last_name": "",
          "other_name": "",
          "email": "",
          "phone_number": "",
          "passport_url": "",
          "password": "",
        }
        self.signupDataNoProperty = {
          "first_name": "FirstName",
          "last_name": "LastName",
          "password": "password3",
          "email": "email1@gmail.com"
        }
        self.loginData = {
          "email": "email1@gmail.com",
          "password": "password1"
        }
        self.loginDataEmpty = {
          "email": "",
          "password": ""
        }
        self.loginDataNoProperty = {
          "email": "email1@gmail.com",
        }
        self.wrongLoginData = {
          "email": "email1@gmail.com",
          "password": "password2"
        }
        self.dataInvalidEmailAddressLogin = {
          "email": "email1gmailcom",
          "password": "password2"
        }
        self.dataInvalidPasswordLogin = {
          "email": "email1@gmail.com",
          "password": "pass"
        }
        self.datainvalidPhoneNumberSignup = {
          "first_name": "FirstName4",
          "last_name": "LastName4",
          "other_name": "OtherName4",
          "email": "email4@gmail.com",
          "phone_number": "0711111",
          "passport_url": "http://passport/url",
          "password": "password3"
        }
        self.datainvalidPassportUrlSignup = {
          "first_name": "FirstName4",
          "last_name": "LastName4",
          "other_name": "OtherName4",
          "email": "email4@gmail.com",
          "phone_number": "0755555555",
          "passport_url": "passport/url",
          "password": "password3"
        }

    def tearDown(self):
        migrate()

    def post(self, path, data):
        return self.client.post(path=path, data=json.dumps(data), content_type='application/json')

    def test_register_user(self):
        response = self.post(self.endpoint + "/signup", self.signupData)
        self.assertEqual(response.status_code, 200)

    def test_invalid_phone_number_signup(self):
        response = self.post(self.endpoint + "/signup", self.datainvalidPhoneNumberSignup)
        self.assertEqual(response.status_code, 400)

    def test_invalid_passport_url_signup(self):
        response = self.post(self.endpoint + "/signup", self.datainvalidPassportUrlSignup)
        self.assertEqual(response.status_code, 400)

    def test_login(self):
        response = self.post(self.endpoint + "/login", self.loginData)
        self.assertEqual(response.status_code, 200)

    def test_wrong_login(self):
        response = self.post(self.endpoint + "/login", self.wrongLoginData)
        self.assertEqual(response.status_code, 401)

    def test_invalid_email_address_login(self):
        response = self.post(self.endpoint + "/login", self.dataInvalidEmailAddressLogin)
        self.assertEqual(response.status_code, 400)

    def test_invalid_password_login(self):
        response = self.post(self.endpoint + "/login", self.dataInvalidPasswordLogin)
        self.assertEqual(response.status_code, 400)

    def test_with_empty_values_signup(self):
        response = self.post(self.endpoint + "/signup", self.signupDataEmpty)
        self.assertEqual(response.status_code, 400)

    def test_with_no_name_property_signup(self):
        response = self.post(self.endpoint + "/signup", self.signupDataNoProperty)
        self.assertEqual(response.status_code, 400)

    def test_with_empty_values_login(self):
        response = self.post(self.endpoint + "/login", self.loginDataEmpty)
        self.assertEqual(response.status_code, 400)

    def test_with_no_name_property_login(self):
        response = self.post(self.endpoint + "/login", self.loginDataNoProperty)
        self.assertEqual(response.status_code, 400)