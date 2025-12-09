"""Unit tests for get_current_level endpoint."""

import pytest

from timeback.services.powerpath.endpoints.get_current_level import get_current_level
from timeback.models.response import TimebackGetCurrentLevelResponse
from timeback.models.request import TimebackGetCurrentLevelRequest
from timeback.enums import TimebackSubject


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


def test_get_current_level_success():
    """Test successful retrieval of current level."""
    mock_http = MockHttpClient(
        {
            "gradeLevel": "5",
            "onboarded": True,
            "availableTests": 8,
        }
    )

    request = TimebackGetCurrentLevelRequest(
        student="student-123",
        subject=TimebackSubject.READING,
    )
    resp = get_current_level(mock_http, request)

    assert isinstance(resp, TimebackGetCurrentLevelResponse)
    assert resp.gradeLevel == "5"
    assert resp.onboarded is True
    assert resp.availableTests == 8


def test_get_current_level_passes_query_params():
    """Test that student and subject are passed as query params."""
    mock_http = MockHttpClient(
        {
            "gradeLevel": "3",
            "onboarded": False,
            "availableTests": 10,
        }
    )

    request = TimebackGetCurrentLevelRequest(
        student="student-456",
        subject=TimebackSubject.MATH,
    )
    resp = get_current_level(mock_http, request)

    assert isinstance(resp, TimebackGetCurrentLevelResponse)
    assert mock_http.last_path == "/powerpath/placement/getCurrentLevel"
    assert mock_http.last_params == {
        "student": "student-456",
        "subject": "Math",
    }


def test_get_current_level_with_null_grade():
    """Test handling of null gradeLevel (student hasn't started placement)."""
    mock_http = MockHttpClient(
        {
            "gradeLevel": None,
            "onboarded": False,
            "availableTests": 12,
        }
    )

    request = TimebackGetCurrentLevelRequest(
        student="student-789",
        subject=TimebackSubject.SCIENCE,
    )
    resp = get_current_level(mock_http, request)

    assert isinstance(resp, TimebackGetCurrentLevelResponse)
    assert resp.gradeLevel is None
    assert resp.onboarded is False
    assert resp.availableTests == 12


def test_get_current_level_completed_onboarding():
    """Test when student has completed all placement tests."""
    mock_http = MockHttpClient(
        {
            "gradeLevel": "12",
            "onboarded": True,
            "availableTests": 0,
        }
    )

    request = TimebackGetCurrentLevelRequest(
        student="student-advanced",
        subject=TimebackSubject.LANGUAGE,
    )
    resp = get_current_level(mock_http, request)

    assert isinstance(resp, TimebackGetCurrentLevelResponse)
    assert resp.gradeLevel == "12"
    assert resp.onboarded is True
    assert resp.availableTests == 0

