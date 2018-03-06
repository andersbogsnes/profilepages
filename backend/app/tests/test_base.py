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

    def signup_user(self, client):
        return client.post('/user', data=json.dumps(self.user), content_type="application/json")

    def login_user(self, client):
        self.signup_user(client)
        login_user_info = {
            "email": self.user["email"],
            "password": self.user["password"]
        }
        return client.post("/login", data=json.dumps(login_user_info), content_type='application/json')