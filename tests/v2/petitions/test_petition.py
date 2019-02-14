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

    def tearDown(self):
        migrate()

    def post(self, path, data):
        return self.client.post(path=path, data=json.dumps(data), content_type='application/json')

    def get(self, path):
        return self.client.get(path=path, content_type='application/json')

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