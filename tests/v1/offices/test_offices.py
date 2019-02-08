import unittest
import json
from app import createApp


class TestOffice(unittest.TestCase):
    def setUp(self):
        self.app = createApp("testing")
        self.client = self.app.test_client()
        self.officeID = 3
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

    def test_create_party(self):
        response = self.post("/api/v1/offices", self.data)
        self.assertTrue(response.json["data"]["id"])
        self.assertEqual(response.status_code, 201)

    def test_get_all_parties(self):
        response = self.get("/api/v1/offices")
        self.assertEqual(response.status_code, 201)

    def test_get_specific_party(self):
        response = self.get("/api/v1/offices/" + str(self.officeID))
        self.assertEqual(response.status_code, 201)

    def test_with_empty_values(self):
        response = self.post("/api/v1/offices", self.dataEmptyValues)
        self.assertEqual(response.status_code, 400)

    def test_with_no_name_property(self):
        response = self.post("/api/v1/offices", self.dataNoNameProperty)
        self.assertEqual(response.status_code, 422)
