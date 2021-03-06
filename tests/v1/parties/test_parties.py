import unittest
import json
from app import createApp


class TestParties(unittest.TestCase):
    def setUp(self):
        self.app = createApp("testing")
        self.client = self.app.test_client()
        self.endpoint = "/api/v1/parties"
        self.partyID = 3
        self.data = {
          "id": 3,
          "name": "Party Name",
          "abbr": "Party Abbreviation",
          "logoUrl": "Party URL",
          "hqAddress": "Party HQ",
        }
        self.dataUpdate = {
          "id": self.partyID,
          "name": "Updated Party Name",
          "abbr": "Updated Party Abbreviation",
          "logoUrl": "Updated Party URL",
          "hqAddress": "Updated Party HQ",
        }
        self.dataNoNameProperty = {
          "id": self.partyID,
          "abbr": "Updated Party Abbreviation",
          "logoUrl": "Updated Party URL",
          "hqAddress": "Updated Party HQ",
        }
        self.dataEmptyValues = {
          "id": self.partyID,
          "name": "",
          "abbr": "",
          "logoUrl": "",
          "hqAddress": "",
        }

    def post(self, path, data):
        return self.client.post(path=path, data=json.dumps(data), content_type='application/json')

    def get(self, path):
        return self.client.get(path=path, content_type='application/json')

    def patch(self, path):
        return self.client.patch(path=path, data=json.dumps(self.dataUpdate), content_type='application/json')

    def delete(self, path):
        return self.client.delete(path=path, content_type='application/json')

    def test_create_party(self):
        response = self.post(self.endpoint, self.data)
        self.assertTrue(response.json["data"]["id"])
        self.assertEqual(response.status_code, 201)

    def test_get_all_parties(self):
        response = self.get(self.endpoint)
        self.assertEqual(response.status_code, 201)

    def test_get_specific_party(self):
        response = self.get(self.endpoint + "/" + str(self.partyID))
        self.assertEqual(response.status_code, 201)

    def test_edit_specific_party(self):
        postParty = self.post(self.endpoint, self.data)
        self.dataUpdate["id"] = self.partyID
        response = self.patch(self.endpoint + "/" + str(self.partyID))
        self.assertEqual(response.status_code, 201)

    def test_delete_specific_party(self):
        postParty = self.post(self.endpoint, self.data)
        response = self.delete(self.endpoint + "/" + str(self.partyID))
        self.assertEqual(response.status_code, 201)

    def test_with_empty_values(self):
        response = self.post(self.endpoint, self.dataEmptyValues)
        self.assertEqual(response.status_code, 422)

    def test_with_no_name_property(self):
        response = self.post(self.endpoint, self.dataNoNameProperty)
        self.assertEqual(response.status_code, 422)
