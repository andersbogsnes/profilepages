import json

import pytest


@pytest.mark.usefixtures('session')
class TestBase:
    user = {
        "email": "test@test.com",
        "initials": "abcd",
        "user_name": "Test Testerson",
        "password": "1234"
    }
    answer = [
        {
            "questionNr": 1,
            "value": 4
        },
        {
            "questionNr": 2,
            "value": 4
        },
        {
            "questionNr": 3,
            "value": 4
        },
        {
            "questionNr": 4,
            "value": 4
        },
        {
            "questionNr": 5,
            "value": 4
        },
        {
            "questionNr": 6,
            "value": 4
        },
        {
            "questionNr": 7,
            "value": 4
        },
        {
            "questionNr": 8,
            "value": 4
        },
        {
            "questionNr": 9,
            "value": 4
        },
        {
            "questionNr": 10,
            "value": 4
        },
        {
            "questionNr": 11,
            "value": 4
        }
    ]

    def signup_user(self, client):
        return client.post('/user', data=json.dumps(self.user), content_type="application/json")

    def login_user(self, client):
        self.signup_user(client)
        login_user_info = {
            "email": self.user["email"],
            "password": self.user["password"]
        }
        return client.post("/login", data=json.dumps(login_user_info), content_type='application/json')

    def get_token(self, client):
        resp = self.login_user(client)
        data = json.loads(resp.data)
        return data["data"]["auth"]

    def save_answer(self, client, token=None):
        if token is None:
            token = self.get_token(client)

        return client.post('/answer',
                           data=json.dumps(self.answer),
                           content_type='application/json',
                           headers={'Authorization': f"Bearer {token}"}
                           )