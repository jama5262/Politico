import unittest
import json
from app import createApp
from app.api.database.migrations.migrations import migrate


class TestVotes(unittest.TestCase):
    def setUp(self):
        self.app = createApp("testing")
        self.client = self.app.test_client()
        self.endpoint = "/api/v2/votes"
        self.data = {
          "office": 1,
          "candidate": 2,
          "created_by": 2
        }
        self.dataDuplicate = {
          "office": 2,
          "candidate": 2,
          "created_by": 1
        }
        self.dataEmpty = {
          "office": "",
          "candidate": "",
          "created_by": ""
        }
        self.dataNoProperties = {
          "office": 1,
          "created_by": 1
        }
        self.loginData = {
          "email": "admin@gmail.com",
          "password": "adminpass"
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

    def test_create_vote(self):
        response = self.post(self.endpoint, self.data)
        self.assertEqual(response.status_code, 200)

    def test_get_all_votes(self):
        response = self.get(self.endpoint)
        self.assertEqual(response.status_code, 200)

    def test_create_duplicate_vote(self):
        response = self.post(self.endpoint, self.dataDuplicate)
        self.assertEqual(response.status_code, 400)

    def test_with_empty_values_vote(self):
        response = self.post(self.endpoint, self.dataEmpty)
        self.assertEqual(response.status_code, 400)

    def test_with_no_name_property_vote(self):
        response = self.post(self.endpoint, self.dataNoProperties)
        self.assertEqual(response.status_code, 400)
