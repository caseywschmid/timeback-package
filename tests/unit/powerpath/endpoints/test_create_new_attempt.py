"""Unit tests for create_new_attempt endpoint."""

import pytest

from timeback.services.powerpath.endpoints.create_new_attempt import create_new_attempt
from timeback.models.request import TimebackCreateNewAttemptRequest
from timeback.models.response import TimebackCreateNewAttemptResponse


class MockHttpClient:
    """Mock HTTP client for testing."""

    def __init__(self, response_data):
        self.response_data = response_data
        self.last_path = None
        self.last_json = None

    def post(self, path, json=None):
        self.last_path = path
        self.last_json = json
        return self.response_data


def test_create_new_attempt_success():
    """Test successful creation of new attempt."""
    mock_http = MockHttpClient(
        {
            "attempt": {
                "attempt": 2,
                "score": 0,
                "scoreStatus": "not submitted",
                "xp": None,
                "startedAt": "2024-01-15T10:00:00Z",
                "completedAt": None,
            }
        }
    )

    request = TimebackCreateNewAttemptRequest(
        student="student-123",
        lesson="lesson-456",
    )
    resp = create_new_attempt(mock_http, request)

    assert isinstance(resp, TimebackCreateNewAttemptResponse)
    assert resp.attempt.attempt == 2
    assert resp.attempt.scoreStatus == "not submitted"


def test_create_new_attempt_path():
    """Test that the correct path is used."""
    mock_http = MockHttpClient(
        {
            "attempt": {
                "attempt": 1,
                "score": 0,
                "scoreStatus": "not submitted",
                "xp": None,
                "startedAt": None,
                "completedAt": None,
            }
        }
    )

    request = TimebackCreateNewAttemptRequest(student="s", lesson="l")
    create_new_attempt(mock_http, request)

    assert mock_http.last_path == "/powerpath/createNewAttempt"


def test_create_new_attempt_body():
    """Test that correct body is sent."""
    mock_http = MockHttpClient(
        {
            "attempt": {
                "attempt": 1,
                "score": 0,
                "scoreStatus": "not submitted",
                "xp": None,
                "startedAt": None,
                "completedAt": None,
            }
        }
    )

    request = TimebackCreateNewAttemptRequest(
        student="student-abc",
        lesson="lesson-xyz",
    )
    create_new_attempt(mock_http, request)

    assert mock_http.last_json["student"] == "student-abc"
    assert mock_http.last_json["lesson"] == "lesson-xyz"

