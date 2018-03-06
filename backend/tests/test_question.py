import json
import pytest

from app.model import Answers
from tests.test_base import TestBase


@pytest.mark.usefixtures('session')
class TestQuestions(TestBase):

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

    def test_answer_returns_correctly_when_logged_in(self, client, session):
        token = self.get_token(client)

        resp = client.post('/answer', data=json.dumps(self.answer),
                           headers={"Authorization": f"Bearer {token}"},
                           content_type="application/json")
        assert 200 == resp.status_code
        data = json.loads(resp.data)
        assert "success" == data["status"]
        assert "Answers Saved" == data["message"]

        result = Answers.query.all()
        assert 11 == len(result)
        assert self.answer[0]["value"] == result[0].answer

    @pytest.mark.xfail
    def test_answer_errors_when_invalid_data_is_posted(self, client):
        token = self.get_token(client)

        wrong_answer = [{
            "questionNr": 1,
            "value": None
        }]

        resp = client.post('/answer',
                           data=json.dumps(wrong_answer),
                           content_type='application/json',
                           headers={"Authorization": f"Bearer {token}"})

        assert 403 == resp.status_code
        data = json.loads(resp.data)
        assert "error" == data["status"]
        assert "Invalid answer" == data["message"]

    def test_result_returns_correctly(self, client):
        token = self.get_token(client)
        self.save_answer(client, token)

        resp = client.get('/result', headers={"Authorization": f"Bearer {token}"})
        assert 200 == resp.status_code
        data = json.loads(resp.data)
        assert "success" == data["status"]
        assert "Result found" == data["message"]
        assert data["data"]
        total_score = sum([row["percent_score"] for row in data["data"]])
        assert 100 == int(total_score)

    def test_result_fails_correctly_with_no_token(self, client):
        resp = client.get('/result')
        assert 401 == resp.status_code
        data = json.loads(resp.data)
        assert "error" == data["status"]
        assert "Must be logged in" == data["message"]
        assert data.get("data") is None
