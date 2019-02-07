import unittest
import json
from app import createApp


class TestParties(unittest.TestCase):
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
        self.dataUpdate = {
          "id": None,
          "name": "Updated Party Name",
          "abbr": "Updated Party Abbreviation",
          "logoUrl": "Updated Party URL",
          "hqAddress": "Updated Party HQ",
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
        response = self.post("/api/v1/parties")
        self.assertTrue(response.json["data"]["id"])
        self.assertEqual(response.status_code, 201)

    def test_get_all_parties(self):
        response = self.get("/api/v1/parties")
        self.assertEqual(response.status_code, 201)

    def test_get_specific_party(self):
        postParty = self.post("/api/v1/parties")
        response = self.get("/api/v1/parties/" + str(postParty.json["data"]["id"]))
        self.assertEqual(response.status_code, 201)

    def test_edit_specific_party(self):
        postParty = self.post("/api/v1/parties")
        self.dataUpdate["id"] = postParty.json["data"]["id"]
        response = self.patch("/api/v1/parties/" + str(postParty.json["data"]["id"]))
        self.assertEqual(response.status_code, 201)

    def test_delete_specific_party(self):
        postParty = self.post("/api/v1/parties")
        response = self.delete("/api/v1/parties/" + str(postParty.json["data"]["id"]))
        self.assertEqual(response.status_code, 201)
