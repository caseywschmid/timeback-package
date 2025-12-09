"""Unit tests for get_next_placement_test endpoint."""

import pytest

from timeback.services.powerpath.endpoints.get_next_placement_test import get_next_placement_test
from timeback.models.response import TimebackGetNextPlacementTestResponse
from timeback.models.request import TimebackGetNextPlacementTestRequest
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


def test_get_next_placement_test_success():
    """Test successful retrieval of next placement test."""
    mock_http = MockHttpClient(
        {
            "exhaustedTests": False,
            "gradeLevel": "5",
            "lesson": "component-resource-123",
            "onboarded": False,
            "availableTests": 8,
        }
    )

    request = TimebackGetNextPlacementTestRequest(
        student="student-123",
        subject=TimebackSubject.READING,
    )
    resp = get_next_placement_test(mock_http, request)

    assert isinstance(resp, TimebackGetNextPlacementTestResponse)
    assert resp.exhaustedTests is False
    assert resp.gradeLevel == "5"
    assert resp.lesson == "component-resource-123"
    assert resp.onboarded is False
    assert resp.availableTests == 8


def test_get_next_placement_test_passes_query_params():
    """Test that student and subject are passed as query params."""
    mock_http = MockHttpClient(
        {
            "exhaustedTests": False,
            "gradeLevel": "3",
            "lesson": "lesson-456",
            "onboarded": False,
            "availableTests": 10,
        }
    )

    request = TimebackGetNextPlacementTestRequest(
        student="student-456",
        subject=TimebackSubject.MATH,
    )
    resp = get_next_placement_test(mock_http, request)

    assert isinstance(resp, TimebackGetNextPlacementTestResponse)
    assert mock_http.last_path == "/powerpath/placement/getNextPlacementTest"
    assert mock_http.last_params == {
        "student": "student-456",
        "subject": "Math",
    }


def test_get_next_placement_test_exhausted():
    """Test when student has completed all placement tests."""
    mock_http = MockHttpClient(
        {
            "exhaustedTests": True,
            "gradeLevel": None,
            "lesson": None,
            "onboarded": True,
            "availableTests": 0,
        }
    )

    request = TimebackGetNextPlacementTestRequest(
        student="student-advanced",
        subject=TimebackSubject.SCIENCE,
    )
    resp = get_next_placement_test(mock_http, request)

    assert isinstance(resp, TimebackGetNextPlacementTestResponse)
    assert resp.exhaustedTests is True
    assert resp.gradeLevel is None
    assert resp.lesson is None
    assert resp.onboarded is True
    assert resp.availableTests == 0


def test_get_next_placement_test_scored_below_90():
    """Test when student scored below 90 on last test (onboarded = true, no next test)."""
    mock_http = MockHttpClient(
        {
            "exhaustedTests": False,
            "gradeLevel": None,
            "lesson": None,
            "onboarded": True,
            "availableTests": 5,
        }
    )

    request = TimebackGetNextPlacementTestRequest(
        student="student-placed",
        subject=TimebackSubject.LANGUAGE,
    )
    resp = get_next_placement_test(mock_http, request)

    assert isinstance(resp, TimebackGetNextPlacementTestResponse)
    assert resp.exhaustedTests is False
    assert resp.lesson is None
    assert resp.onboarded is True
    assert resp.availableTests == 5


def test_get_next_placement_test_first_test():
    """Test when student hasn't started any tests yet."""
    mock_http = MockHttpClient(
        {
            "exhaustedTests": False,
            "gradeLevel": "0",
            "lesson": "first-lesson-123",
            "onboarded": False,
            "availableTests": 12,
        }
    )

    request = TimebackGetNextPlacementTestRequest(
        student="new-student",
        subject=TimebackSubject.VOCABULARY,
    )
    resp = get_next_placement_test(mock_http, request)

    assert isinstance(resp, TimebackGetNextPlacementTestResponse)
    assert resp.exhaustedTests is False
    assert resp.gradeLevel == "0"
    assert resp.lesson == "first-lesson-123"
    assert resp.onboarded is False
    assert resp.availableTests == 12

