"""Unit tests for get_assessment_progress endpoint."""

import pytest

from timeback.services.powerpath.endpoints.get_assessment_progress import (
    get_assessment_progress,
)
from timeback.models.response import TimebackAssessmentProgressResponse


class MockHttpClient:
    """Mock HTTP client for testing."""

    def __init__(self, response_data):
        self.response_data = response_data
        self.last_path = None
        self.last_params = None

    def get(self, path, params=None):
        self.last_path = path
        self.last_params = params
        return self.response_data


def test_get_assessment_progress_success():
    """Test successful retrieval of assessment progress."""
    mock_http = MockHttpClient(
        {
            "lessonType": "quiz",
            "finalized": False,
            "attempt": 1,
            "score": 75.0,
            "xp": 50,
            "multiplier": 1.0,
            "accuracy": 0.75,
            "correctQuestions": 3,
            "totalQuestions": 4,
            "questions": [
                {
                    "id": "q1",
                    "index": 0,
                    "title": "Question 1",
                    "url": "https://qti.example.com/q1",
                    "difficulty": "medium",
                }
            ],
            "toolProvider": None,
        }
    )

    resp = get_assessment_progress(mock_http, "student-123", "lesson-456")

    assert isinstance(resp, TimebackAssessmentProgressResponse)
    assert resp.lessonType == "quiz"
    assert resp.score == 75.0
    assert resp.accuracy == 0.75
    assert len(resp.questions) == 1


def test_get_assessment_progress_path_and_params():
    """Test that correct path and params are used."""
    mock_http = MockHttpClient(
        {
            "lessonType": "quiz",
            "attempt": 1,
            "xp": None,
            "multiplier": None,
            "accuracy": 0,
            "correctQuestions": 0,
            "totalQuestions": 0,
        }
    )

    get_assessment_progress(mock_http, "student-abc", "lesson-xyz")

    assert mock_http.last_path == "/powerpath/getAssessmentProgress"
    assert mock_http.last_params["student"] == "student-abc"
    assert mock_http.last_params["lesson"] == "lesson-xyz"
    assert "attempt" not in mock_http.last_params


def test_get_assessment_progress_with_attempt():
    """Test with specific attempt number."""
    mock_http = MockHttpClient(
        {
            "lessonType": "quiz",
            "attempt": 2,
            "xp": None,
            "multiplier": None,
            "accuracy": 0,
            "correctQuestions": 0,
            "totalQuestions": 0,
        }
    )

    get_assessment_progress(mock_http, "s", "l", attempt=2)

    assert mock_http.last_params["attempt"] == "2"


def test_get_assessment_progress_powerpath100():
    """Test PowerPath100 lesson type response."""
    mock_http = MockHttpClient(
        {
            "lessonType": "powerpath-100",
            "attempt": 1,
            "score": 80.0,
            "xp": 100,
            "multiplier": 1.5,
            "accuracy": 0.8,
            "correctQuestions": 8,
            "totalQuestions": 10,
            "remainingQuestionsPerDifficulty": {
                "easy": 2,
                "medium": 5,
                "hard": 3,
            },
            "seenQuestions": [],
        }
    )

    resp = get_assessment_progress(mock_http, "s", "l")

    assert resp.lessonType == "powerpath-100"
    assert resp.remainingQuestionsPerDifficulty.easy == 2
    assert resp.remainingQuestionsPerDifficulty.hard == 3

