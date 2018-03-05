import json

user = {
    "email": "test@test.com",
    "initials": "abcd",
    "name": "Test Testerson",
    "password": "1234"
}


def test_login_fails_correctly_with_invalid_user(client):
    resp = client.post('/login',
                       data=json.dumps(user),
                       content_type='application/json')
    assert resp.status_code == 404
    data = resp.get_json()
    assert "User doesn't exist" == data['message']
    assert "error" == data["status"]


