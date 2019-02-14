import unittest
import json
from app import createApp


class TestOffice(unittest.TestCase):
    def setUp(self):
        self.app = createApp("testing")
        self.client = self.app.test_client()
        self.officeID = 3
        self.endpoint = "/api/v2/offices"
        self.data = {
          "id": 3,
          "type": "Office type",
          "name": "Office name"
        }
        self.dataNoNameProperty = {
            "id": 3,
            "type": "Office type",
        }
        self.dataEmptyValues = {
          "id": 3,
          "type": "",
          "name": ""
        }

    def tearDown(self):
        self.app = None
        self.client = None
        self.data = {}
        self.dataUpdate = {}

    def post(self, path, data):
        return self.client.post(path=path, data=json.dumps(data), content_type='application/json')

    def get(self, path):
        return self.client.get(path=path, content_type='application/json')

    def test_create_office(self):
        response = self.post(self.endpoint, self.data)
        self.assertTrue(response.json["data"]["id"])
        self.assertEqual(response.status_code, 200)

    def test_get_all_office(self):
        response = self.get(self.endpoint)
        self.assertEqual(response.status_code, 200)

    def test_get_specific_office(self):
        response = self.get(self.endpoint + "/" + str(self.officeID))
        self.assertEqual(response.status_code, 200)

    def test_with_empty_values(self):
        response = self.post(self.endpoint, self.dataEmptyValues)
        self.assertEqual(response.status_code, 422)

    def test_with_no_name_property(self):
        response = self.post(self.endpoint, self.dataNoNameProperty)
        self.assertEqual(response.status_code, 422)
