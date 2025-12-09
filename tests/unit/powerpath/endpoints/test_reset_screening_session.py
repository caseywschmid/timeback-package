"""Unit tests for reset_screening_session endpoint."""

import pytest

from timeback.services.powerpath.endpoints.reset_screening_session import reset_screening_session


class MockHttpClient:
    """Mock HTTP client for testing."""

    def __init__(self, response_data=None):
        self.response_data = response_data
        self.last_path = None
        self.last_json = None

    def post(self, path, json=None):
        self.last_path = path
        self.last_json = json
        return self.response_data


def test_reset_screening_session_success():
    """Test successful reset of screening session."""
    mock_http = MockHttpClient(None)  # 204 returns None

    result = reset_screening_session(mock_http, "user-123")

    assert result is None
    assert mock_http.last_path == "/powerpath/screening/session/reset"
    assert mock_http.last_json == {"userId": "user-123"}


def test_reset_screening_session_path_and_body():
    """Test that the correct path and body are sent."""
    mock_http = MockHttpClient(None)

    result = reset_screening_session(mock_http, "user-456")

    assert mock_http.last_path == "/powerpath/screening/session/reset"
    assert mock_http.last_json == {"userId": "user-456"}


def test_reset_screening_session_different_users():
    """Test reset works for different users."""
    user_ids = ["user-a", "user-b", "user-c"]

    for user_id in user_ids:
        mock_http = MockHttpClient(None)
        result = reset_screening_session(mock_http, user_id)

        assert result is None
        assert mock_http.last_json == {"userId": user_id}

