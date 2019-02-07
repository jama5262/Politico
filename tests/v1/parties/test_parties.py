import unittest
import json
from app import createApp


class TesParties(unittest.TestCase):
    def setUp(self):
        self.app = createApp("testing")
        self.client = self.app.test_client()
        self.data = {
          "id": 3,
          "name": "Party Name",
          "abbr": "Party Abbreviation",
          "logoUrl": "Party URL",
          "hqAddress": "Party HQ",
        }

    def post(self, path):
        return self.client.post(path=path, data=json.dumps(self.data), content_type='application/json')

    def get(self, path):
        return self.client.get(path=path, content_type='application/json')

    def test_create_party(self):
        response = self.post("/api/v1/parties")
        self.assertEqual(response.status_code, 201)

    def test_get_all_parties(self):
        response = self.post("/api/v1/parties")
        self.assertEqual(response.status_code, 201)
