import unittest
import json
from app import createApp
from app.api.database.migrations.migrations import migrate


class TestPetition(unittest.TestCase):
    def setUp(self):
        self.app = createApp("testing")
        self.client = self.app.test_client()
        self.endpoint = "/api/v2/petitions"
        self.data = {
          "office": 1,
          "created_by": 1,
          "text": "Reason for petition",
        }
        self.dataEmpty = {
          "office": 1,
          "created_by": 1,
          "text": "",
        }
        self.dataNoProperty = {
          "text": "Reason for petition",
        }
        self.loginData = {
          "email": "email1@gmail.com",
          "password": "pass1"
        }

    def tearDown(self):
        migrate()

    def loginUser(self):
        response = self.client.post(path="/api/v2/auth/login", data=json.dumps(self.loginData), content_type='application/json')
        token = response.json["data"]["token"]
        return {
            "Authorization": "Bearer " + token
        }

    def post(self, path, data):
        return self.client.post(path=path, data=json.dumps(data), content_type='application/json', headers=self.loginUser())

    def get(self, path):
        return self.client.get(path=path, content_type='application/json', headers=self.loginUser())

    def test_create_petition(self):
        response = self.post(self.endpoint, self.data)
        self.assertEqual(response.status_code, 200)

    def test_get_all_petitions(self):
        response = self.get(self.endpoint)
        self.assertEqual(response.status_code, 200)

    def test_with_empty_values(self):
        response = self.post(self.endpoint, self.dataEmpty)
        self.assertEqual(response.status_code, 422)

    def test_with_no_name_property(self):
        response = self.post(self.endpoint, self.dataNoProperty)
        self.assertEqual(response.status_code, 422)