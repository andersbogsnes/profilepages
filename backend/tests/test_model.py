from tests.test_base import TestBase
from app.blueprints.survey.model import Question, Answers
import pytest


@pytest.mark.usefixtures('session')
class TestModel(TestBase):
    def test_number_of_questions_is_correct(self):
        assert 11 == Question.count()

    def test_max_version_answer_returns_correctly(self, client):
        token = self.get_token(client)
        self.save_answer(client, token)

        assert 0 == Answers.get_max_version(1)

        self.save_answer(client, token)
        assert 1 == Answers.get_max_version(1)

