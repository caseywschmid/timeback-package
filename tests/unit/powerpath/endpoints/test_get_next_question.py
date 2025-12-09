"""Unit tests for get_next_question endpoint."""

import pytest

from timeback.services.powerpath.endpoints.get_next_question import get_next_question
from timeback.models.response import TimebackNextQuestionResponse


class MockHttp:
    """Mock HTTP client for testing."""

    def __init__(self, response_data: dict):
        self.response_data = response_data
        self.last_path = None
        self.last_params = None

    def get(self, path: str, params: dict = None):
        self.last_path = path
        self.last_params = params
        return self.response_data


class TestGetNextQuestion:
    """Tests for get_next_question endpoint."""

    def test_get_next_question_success(self):
        """Test successful retrieval of next question."""
        mock_response = {
            "score": 75.5,
            "question": {
                "id": "q-123",
                "index": 5,
                "title": "Math Question 5",
                "url": "https://qti.example.com/question/123",
                "difficulty": "medium",
                "humanApproved": True,
                "content": {
                    "type": "choice",
                    "rawXml": "<qti-assessment-item>...</qti-assessment-item>",
                },
            },
        }

        mock_http = MockHttp(mock_response)
        resp = get_next_question(mock_http, "student-123", "lesson-456")

        assert isinstance(resp, TimebackNextQuestionResponse)
        assert resp.score == 75.5
        assert resp.question.id == "q-123"
        assert resp.question.index == 5
        assert resp.question.title == "Math Question 5"
        assert resp.question.difficulty == "medium"

    def test_get_next_question_correct_path_and_params(self):
        """Test correct path and query parameters."""
        mock_response = {
            "score": 0,
            "question": {
                "id": "q-1",
                "index": 0,
                "title": "First Question",
                "url": "https://qti.example.com/q/1",
                "difficulty": "easy",
            },
        }

        mock_http = MockHttp(mock_response)
        get_next_question(mock_http, "student-abc", "lesson-xyz")

        assert mock_http.last_path == "/powerpath/getNextQuestion"
        assert mock_http.last_params == {
            "student": "student-abc",
            "lesson": "lesson-xyz",
        }

    def test_get_next_question_with_response_data(self):
        """Test question with previous response data."""
        mock_response = {
            "score": 50,
            "question": {
                "id": "q-456",
                "index": 3,
                "title": "Previously Answered",
                "url": "https://qti.example.com/q/456",
                "difficulty": "hard",
                "response": "choice-A",
                "correct": False,
                "result": {
                    "score": 0,
                    "feedback": "Try again!",
                    "outcomes": {"SCORE": "0"},
                },
            },
        }

        mock_http = MockHttp(mock_response)
        resp = get_next_question(mock_http, "student-123", "lesson-456")

        assert resp.question.response == "choice-A"
        assert resp.question.correct is False
        assert resp.question.result is not None

    def test_get_next_question_with_learning_objectives(self):
        """Test question with learning objectives."""
        mock_response = {
            "score": 60,
            "question": {
                "id": "q-789",
                "index": 7,
                "title": "Algebra Problem",
                "url": "https://qti.example.com/q/789",
                "difficulty": "medium",
                "learningObjectives": ["lo-1", "lo-2", "lo-3"],
            },
        }

        mock_http = MockHttp(mock_response)
        resp = get_next_question(mock_http, "student-123", "lesson-456")

        assert resp.question.learningObjectives == ["lo-1", "lo-2", "lo-3"]

    def test_get_next_question_all_difficulties(self):
        """Test all valid difficulty values."""
        difficulties = ["easy", "medium", "hard"]

        for difficulty in difficulties:
            mock_response = {
                "score": 0,
                "question": {
                    "id": "q-1",
                    "index": 0,
                    "title": "Test Question",
                    "url": "https://qti.example.com/q/1",
                    "difficulty": difficulty,
                },
            }

            mock_http = MockHttp(mock_response)
            resp = get_next_question(mock_http, "student-123", "lesson-456")
            assert resp.question.difficulty == difficulty

