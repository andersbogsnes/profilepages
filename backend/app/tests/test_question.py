import json
import pytest
from app.tests.test_base import TestBase


@pytest.mark.usefixtures('session')
class TestQuestions(TestBase):
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

    def test_questions_return_correctly(self, client):
        resp = client.get('/questions')
        assert 200 == resp.status_code
        data = json.loads(resp.data)
        assert "success" == data["status"]
        assert "Questions loaded successfully" == data["message"]
        assert 11 == len(data["data"])
        assert 1 == data["data"][0]["id"]
        assert "Jeg har mere forstand på mine bank- og investeringsorhold end min rådgiver har" == data["data"][0][
            "text"]

    def test_answer_fails_if_not_authenticated_correctly(self, client):
        resp = client.post('/answer', data=json.dumps(self.answer), content_type='application/json')
        assert 401 == resp.status_code
        data = json.loads(resp.data)
        assert "error" == data["status"]
        assert "Must be logged in" == data["message"]
        assert data.get("data") is None

    def test_answer_returns_correctly_when_logged_in(self, client):
        pass
