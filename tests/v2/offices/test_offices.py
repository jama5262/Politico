import unittest
import json
from app import createApp
from app.api.database.migrations.migrations import migrate


class TestOffice(unittest.TestCase):
    def setUp(self):
        self.app = createApp("testing")
        self.client = self.app.test_client()
        self.officeID = 3
        self.endpoint = "/api/v2/offices"
        self.data = {
          "type": "Office type",
          "name": "Office name"
        }
        self.dataNoNameProperty = {
            "type": "Office type",
        }
        self.dataEmptyValues = {
          "type": "",
          "name": ""
        }
        self.dataUpdate = {
          "type": "Updated",
          "name": "Updated"
        }

    def tearDown(self):
        migrate()

    def post(self, path, data):
        return self.client.post(path=path, data=json.dumps(data), content_type='application/json')

    def get(self, path):
        return self.client.get(path=path, content_type='application/json')

    def patch(self, path, data):
        return self.client.patch(path=path, data=json.dumps(data), content_type='application/json')

    def delete(self, path):
        return self.client.delete(path=path, content_type='application/json')

    def test_create_office(self):
        response = self.post(self.endpoint, self.data)
        self.assertEqual(response.status_code, 200)

    def test_get_all_office(self):
        response = self.get(self.endpoint)
        self.assertEqual(response.status_code, 200)

    def test_edit_specific_office(self):
        postOffice = self.post(self.endpoint, self.data)
        response = self.patch(self.endpoint + "/" + str(self.officeID), self.dataUpdate)
        self.assertEqual(response.status_code, 200)

    def test_delete_specific_office(self):
        postOffice = self.post(self.endpoint, self.data)
        response = self.delete(self.endpoint + "/" + str(self.officeID))
        self.assertEqual(response.status_code, 200)

    def test_get_specific_office(self):
        postOffice = self.post(self.endpoint, self.data)
        response = self.get(self.endpoint + "/" + str(self.officeID))
        self.assertEqual(response.status_code, 200)

    def test_with_empty_values(self):
        response = self.post(self.endpoint, self.dataEmptyValues)
        self.assertEqual(response.status_code, 422)

    def test_with_no_name_property(self):
        response = self.post(self.endpoint, self.dataNoNameProperty)
        self.assertEqual(response.status_code, 422)
