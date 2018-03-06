import json
import pytest
import time
from tests.test_base import TestBase


@pytest.mark.usefixtures('session')
class TestAuth(TestBase):
    def test_signup_works_correctly(self, client):
        resp = client.post('/user', data=json.dumps(self.user), content_type="application/json")
        assert 200 == resp.status_code
        data = json.loads(resp.data)
        assert "User created" == data["message"]
        assert "success" == data["status"]

    @pytest.mark.xfail
    def test_signup_invalid_email_fails_correctly(self, client):
        wrong_user = {
            "email": "",
            "initials": "abcd",
            "user_name": "Test Testerson",
            "password": "1234"
        }

        resp = client.post('/user', data=json.dumps(wrong_user), content_type="application/json")
        assert 400 == resp.status_code
        data = json.loads(resp.data)
        assert "error" == data["status"]
        assert "Invalid email" == data["message"]

    @pytest.mark.xfail
    def test_signup_invalid_user_fails_correctly(self, client):
        wrong_user = {
            "email": "test@test.com",
            "initials": "abcd",
            "user_name": "",
            "password": "1234"
        }
        resp = client.post('/user', data=json.dumps(wrong_user), content_type="application/json")
        assert 400 == resp.status_code
        data = json.loads(resp.data)
        assert "error" == data["status"]
        assert "Invalid Username" == data["message"]

    def test_signup_twice_same_user_fails_correctly(self, client):
        resp = self.signup_user(client)
        assert 200 == resp.status_code
        data = json.loads(resp.data)
        assert "success" == data["status"]
        assert "User created" == data["message"]

        resp = self.signup_user(client)
        assert 403 == resp.status_code
        data = json.loads(resp.data)
        assert "error" == data["status"]
        assert "User already exists" == data["message"]

    def test_login_works_correctly(self, client):
        self.signup_user(client)
        login_user_info = {
            "email": self.user["email"],
            "password": self.user["password"]
        }
        resp = client.post('/login', data=json.dumps(login_user_info), content_type='application/json')
        assert 200 == resp.status_code
        data = json.loads(resp.data)
        assert "success" == data["status"]
        assert "Logged in successfully" == data["message"]
        assert self.user["email"] == data["data"]["email"]
        assert self.user["user_name"] == data["data"]["user_name"]
        assert self.user["initials"] == data["data"]["initials"]
        assert data["data"]["auth"]

    def test_login_fails_correctly_with_invalid_user(self, client):
        resp = client.post('/login',
                           data=json.dumps(self.user),
                           content_type='application/json')
        assert resp.status_code == 404
        data = json.loads(resp.data)
        assert "User doesn't exist" == data['message']
        assert "error" == data["status"]

    def test_login_gives_different_token_when_already_logged_in(self, client):
        resp = self.login_user(client)
        old_token = json.loads(resp.data)["data"]["auth"]

        login_info = {
            "email": self.user["email"],
            "password": self.user["password"]
        }
        time.sleep(1)
        resp = client.post('/login', data=json.dumps(login_info), content_type='application/json')
        assert 200 == resp.status_code
        data = json.loads(resp.data)
        assert old_token != data["data"]["auth"]
