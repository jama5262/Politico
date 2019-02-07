import unittest
import json
from app import createApp


class TestOffice(unittest.TestCase):
    def setUp(self):
        self.app = createApp("testing")
        self.client = self.app.test_client()
        self.data = {
          "id": 2,
          "type": "Office type",
          "name": "Office name"
        }
        self.dataUpdate = {
          "id": None,
          "type": "Update Office type",
          "name": "Update Office name"
        }

    def post(self, path):
        return self.client.post(path=path, data=json.dumps(self.data), content_type='application/json')

    def get(self, path):
        return self.client.get(path=path, content_type='application/json')

    def patch(self, path):
        return self.client.patch(path=path, data=json.dumps(self.dataUpdate), content_type='application/json')

    def delete(self, path):
        return self.client.delete(path=path, content_type='application/json')

    def test_create_party(self):
        response = self.post("/api/v1/offices")
        self.assertTrue(response.json["data"]["id"])
        self.assertEqual(response.status_code, 201)

    def test_get_all_parties(self):
        response = self.get("/api/v1/offices")
        self.assertEqual(response.status_code, 201)

    def test_get_specific_party(self):
        postParty = self.post("/api/v1/offices")
        response = self.get("/api/v1/offices/" + str(postParty.json["data"]["id"]))
        self.assertEqual(response.status_code, 201)
