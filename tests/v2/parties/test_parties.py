import unittest
import json
from app import createApp
from app.api.database.migrations.migrations import migrate


class TestParties(unittest.TestCase):
    def setUp(self):
        self.app = createApp("testing")
        self.client = self.app.test_client()
        self.endpoint = "/api/v2/parties"
        self.partyID = 3
        self.data = {
          "name": "Party Name",
          "abbr": "Party Abbreviation",
          "logo_url": "http://logo/url",
          "hq_address": "Party HQ"
        }
        self.dataUpdate = {
          "name": "Updated Party Name",
          "abbr": "Updated Party Abbreviation",
          "logo_url": "http://logo/url",
          "hq_address": "Updated Party HQ"
        }
        self.dataNoNameProperty = {
          "abbr": "Updated Party Abbreviation",
          "logo_url": "http://logo/url",
          "hq_address": "Updated Party HQ"
        }
        self.dataEmptyValues = {
          "name": "",
          "abbr": "",
          "logo_url": "",
          "hq_address": ""
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

    def patch(self, path, data):
        return self.client.patch(path=path, data=json.dumps(data), content_type='application/json', headers=self.loginUser())

    def delete(self, path):
        return self.client.delete(path=path, content_type='application/json', headers=self.loginUser())

    def test_create_party(self):
        response = self.post(self.endpoint, self.data)
        self.assertEqual(response.status_code, 200, response)

    def test_get_all_parties(self):
        response = self.get(self.endpoint)
        self.assertEqual(response.status_code, 200)

    def test_get_specific_party(self):
        postParty = self.post(self.endpoint, self.data)
        response = self.get(self.endpoint + "/" + str(self.partyID))
        self.assertEqual(response.status_code, 200)

    def test_get_specific_party_not_found(self):
        response = self.get(self.endpoint + "/2000")
        self.assertEqual(response.status_code, 404)

    def test_edit_specific_party(self):
        postParty = self.post(self.endpoint, self.data)
        response = self.patch(self.endpoint + "/" + str(self.partyID), self.dataUpdate)
        self.assertEqual(response.status_code, 200)

    def test_edit_specific_party_not_found(self):
        response = self.patch(self.endpoint + "/2000", self.dataUpdate)
        self.assertEqual(response.status_code, 404)

    def test_delete_specific_party(self):
        postParty = self.post(self.endpoint, self.data)
        response = self.delete(self.endpoint + "/" + str(self.partyID))
        self.assertEqual(response.status_code, 200)

    def test_delete_specific_party_not_found(self):
        response = self.delete(self.endpoint + "/2000")
        self.assertEqual(response.status_code, 404)

    def test_with_empty_values(self):
        response = self.post(self.endpoint, self.dataEmptyValues)
        self.assertEqual(response.status_code, 400)

    def test_with_no_name_property(self):
        response = self.post(self.endpoint, self.dataNoNameProperty)
        self.assertEqual(response.status_code, 400)
