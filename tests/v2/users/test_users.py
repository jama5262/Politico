import unittest
import json
from app import createApp
from app.api.database.migrations.migrations import migrate


class TestUsers(unittest.TestCase):
    def setUp(self):
        self.app = createApp("testing")
        self.client = self.app.test_client()
        self.userID = 5
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

    def get(self, path):
            return self.client.get(path=path, content_type='application/json', headers=self.loginUser())

    def test_get_specific_user(self):
            response = self.get("/api/v2/user/" + str(self.userID))
            self.assertEqual(response.status_code, 200)

    def test_get_specific_candidate(self):
            response = self.get("/api/v2/user/candidate/" + str(self.userID))
            self.assertEqual(response.status_code, 200)

