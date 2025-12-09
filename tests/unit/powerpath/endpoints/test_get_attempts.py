"""Unit tests for get_attempts endpoint."""

import pytest

from timeback.services.powerpath.endpoints.get_attempts import get_attempts
from timeback.models.response import TimebackGetAttemptsResponse


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


class TestGetAttempts:
    """Tests for get_attempts endpoint."""

    def test_get_attempts_success(self):
        """Test successful retrieval of attempts."""
        mock_response = {
            "attempts": [
                {
                    "attempt": 1,
                    "score": 80,
                    "scoreStatus": "fully graded",
                    "xp": 100,
                    "startedAt": "2024-01-15T10:00:00Z",
                    "completedAt": "2024-01-15T10:30:00Z",
                },
                {
                    "attempt": 2,
                    "score": 90,
                    "scoreStatus": "submitted",
                    "xp": 120,
                    "startedAt": "2024-01-16T10:00:00Z",
                    "completedAt": None,
                },
            ]
        }

        mock_http = MockHttp(mock_response)
        resp = get_attempts(mock_http, "student-123", "lesson-456")

        assert isinstance(resp, TimebackGetAttemptsResponse)
        assert len(resp.attempts) == 2
        assert resp.attempts[0].attempt == 1
        assert resp.attempts[0].score == 80
        assert resp.attempts[0].scoreStatus == "fully graded"
        assert resp.attempts[0].xp == 100
        assert resp.attempts[1].attempt == 2
        assert resp.attempts[1].score == 90

    def test_get_attempts_correct_path_and_params(self):
        """Test correct path and query parameters."""
        mock_http = MockHttp({"attempts": []})
        get_attempts(mock_http, "student-abc", "lesson-xyz")

        assert mock_http.last_path == "/powerpath/getAttempts"
        assert mock_http.last_params == {
            "student": "student-abc",
            "lesson": "lesson-xyz",
        }

    def test_get_attempts_empty_list(self):
        """Test handling empty attempts list."""
        mock_http = MockHttp({"attempts": []})
        resp = get_attempts(mock_http, "student-123", "lesson-456")

        assert isinstance(resp, TimebackGetAttemptsResponse)
        assert len(resp.attempts) == 0

    def test_get_attempts_null_fields(self):
        """Test handling null optional fields."""
        mock_response = {
            "attempts": [
                {
                    "attempt": None,
                    "score": 0,
                    "scoreStatus": "not submitted",
                    "xp": None,
                    "startedAt": None,
                    "completedAt": None,
                }
            ]
        }

        mock_http = MockHttp(mock_response)
        resp = get_attempts(mock_http, "student-123", "lesson-456")

        assert len(resp.attempts) == 1
        assert resp.attempts[0].attempt is None
        assert resp.attempts[0].xp is None
        assert resp.attempts[0].startedAt is None

    def test_get_attempts_all_score_statuses(self):
        """Test all valid score status values."""
        statuses = ["exempt", "fully graded", "not submitted", "partially graded", "submitted"]

        for status in statuses:
            mock_response = {
                "attempts": [
                    {
                        "attempt": 1,
                        "score": 50,
                        "scoreStatus": status,
                        "xp": 10,
                        "startedAt": "2024-01-15T10:00:00Z",
                        "completedAt": None,
                    }
                ]
            }

            mock_http = MockHttp(mock_response)
            resp = get_attempts(mock_http, "student-123", "lesson-456")
            assert resp.attempts[0].scoreStatus == status

