"""Unit tests for reset_attempt endpoint."""

import pytest

from timeback.services.powerpath.endpoints.reset_attempt import reset_attempt
from timeback.models.request import TimebackResetAttemptRequest
from timeback.models.response import TimebackResetAttemptResponse


class MockHttp:
    """Mock HTTP client for testing."""

    def __init__(self, response_data: dict):
        self.response_data = response_data
        self.last_path = None
        self.last_json = None

    def post(self, path: str, json: dict = None):
        self.last_path = path
        self.last_json = json
        return self.response_data


class TestResetAttempt:
    """Tests for reset_attempt endpoint."""

    def test_reset_attempt_success(self):
        """Test successful attempt reset."""
        mock_response = {
            "success": True,
            "score": 0,
        }

        mock_http = MockHttp(mock_response)
        request = TimebackResetAttemptRequest(
            student="student-123",
            lesson="lesson-456",
        )
        resp = reset_attempt(mock_http, request)

        assert isinstance(resp, TimebackResetAttemptResponse)
        assert resp.success is True
        assert resp.score == 0

    def test_reset_attempt_correct_path_and_body(self):
        """Test correct path and request body."""
        mock_http = MockHttp({"success": True, "score": 0})
        request = TimebackResetAttemptRequest(
            student="student-abc",
            lesson="lesson-xyz",
        )
        reset_attempt(mock_http, request)

        assert mock_http.last_path == "/powerpath/resetAttempt"
        assert mock_http.last_json == {
            "student": "student-abc",
            "lesson": "lesson-xyz",
        }

    def test_reset_attempt_failure(self):
        """Test handling reset failure."""
        mock_response = {
            "success": False,
            "score": 50,  # Score unchanged on failure
        }

        mock_http = MockHttp(mock_response)
        request = TimebackResetAttemptRequest(
            student="student-123",
            lesson="lesson-456",
        )
        resp = reset_attempt(mock_http, request)

        assert resp.success is False
        assert resp.score == 50

    def test_reset_attempt_always_zero_on_success(self):
        """Test that score is always 0 on successful reset."""
        mock_response = {
            "success": True,
            "score": 0,
        }

        mock_http = MockHttp(mock_response)
        request = TimebackResetAttemptRequest(
            student="student-123",
            lesson="lesson-456",
        )
        resp = reset_attempt(mock_http, request)

        assert resp.success is True
        assert resp.score == 0

