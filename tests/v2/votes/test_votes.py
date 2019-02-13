import unittest
import json
from app import createApp


class TestVotes(unittest.TestCase):
    def setUp(self):
        self.app = createApp("testing")
        self.client = self.app.test_client()
        self.endpoint = "/api/v2/votes"
        self.data = {
          "office": 3,
          "candidate": 1,
          "voter": 4
        }
        self.dataEmpty = {
          "office": "",
          "candidate": "",
          "voter": ""
        }
        self.dataNoProperties = {
          "office": 3,
          "voter": 4
        }

    def post(self, path, data):
        return self.client.post(path=path, data=json.dumps(data), content_type='application/json')

    def test_create_vote(self):
        response = self.post(self.endpoint, self.data)
        self.assertEqual(response.status_code, 200)

    def test_with_empty_values_vote(self):
        response = self.post(self.endpoint, self.dataEmpty)
        self.assertEqual(response.status_code, 422)

    def test_with_no_name_property_vote(self):
        response = self.post(self.endpoint, self.dataNoProperties)
        self.assertEqual(response.status_code, 422)