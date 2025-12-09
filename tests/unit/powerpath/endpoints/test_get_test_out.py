"""Unit tests for get_test_out endpoint."""

import pytest
import warnings

from timeback.services.powerpath.endpoints.get_test_out import get_test_out
from timeback.models.response import TimebackGetTestOutResponse
from timeback.models.request import TimebackGetTestOutRequest


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


def test_get_test_out_success():
    """Test successful retrieval of test-out info."""
    mock_http = MockHttpClient(
        {
            "lessonType": "test-out",
            "lessonId": "lesson-123",
            "finalized": True,
            "toolProvider": "edulastic",
            "attempt": 1,
            "credentials": {
                "email": "student@example.com",
                "password": "test-password",
            },
            "assignmentId": "assignment-456",
            "testUrl": "https://edulastic.com/test/123",
        }
    )

    request = TimebackGetTestOutRequest(
        student="student-123",
        course="course-123",
    )

    # Suppress the deprecation warning for this test
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        resp = get_test_out(mock_http, request)

    assert isinstance(resp, TimebackGetTestOutResponse)
    assert resp.lessonType == "test-out"
    assert resp.lessonId == "lesson-123"
    assert resp.finalized is True
    assert resp.toolProvider == "edulastic"
    assert resp.attempt == 1


def test_get_test_out_emits_deprecation_warning():
    """Test that the endpoint emits a deprecation warning."""
    mock_http = MockHttpClient(
        {
            "lessonType": "test-out",
            "lessonId": None,
            "finalized": False,
            "toolProvider": None,
        }
    )

    request = TimebackGetTestOutRequest(
        student="student-123",
        course="course-123",
    )

    with pytest.warns(DeprecationWarning, match="get_test_out is deprecated"):
        get_test_out(mock_http, request)


def test_get_test_out_query_params():
    """Test that the correct query params are sent."""
    mock_http = MockHttpClient(
        {
            "lessonType": "test-out",
            "lessonId": "lesson-456",
            "finalized": False,
            "toolProvider": "mastery-track",
        }
    )

    request = TimebackGetTestOutRequest(
        student="student-456",
        course="course-456",
    )

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        resp = get_test_out(mock_http, request)

    assert mock_http.last_path == "/powerpath/testOut"
    assert mock_http.last_params == {
        "student": "student-456",
        "course": "course-456",
    }


def test_get_test_out_no_test_out_found():
    """Test when no test-out lesson exists in the course."""
    mock_http = MockHttpClient(
        {
            "lessonType": "test-out",
            "lessonId": None,
            "finalized": False,
            "toolProvider": None,
        }
    )

    request = TimebackGetTestOutRequest(
        student="student-789",
        course="course-no-testout",
    )

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        resp = get_test_out(mock_http, request)

    assert isinstance(resp, TimebackGetTestOutResponse)
    assert resp.lessonId is None
    assert resp.finalized is False
    assert resp.toolProvider is None


def test_get_test_out_with_credentials():
    """Test with full external test credentials."""
    mock_http = MockHttpClient(
        {
            "lessonType": "test-out",
            "lessonId": "lesson-ext",
            "finalized": False,
            "toolProvider": "edulastic",
            "attempt": 2,
            "credentials": {
                "email": "test@school.edu",
                "password": "secure123",
            },
            "assignmentId": "edu-assign-1",
            "classId": "edu-class-1",
            "testUrl": "https://edulastic.com/test/abc",
            "testId": "edu-test-1",
        }
    )

    request = TimebackGetTestOutRequest(
        student="student-ext",
        course="course-ext",
    )

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        resp = get_test_out(mock_http, request)

    assert resp.credentials.email == "test@school.edu"
    assert resp.credentials.password == "secure123"
    assert resp.assignmentId == "edu-assign-1"
    assert resp.classId == "edu-class-1"
    assert resp.testUrl == "https://edulastic.com/test/abc"
    assert resp.testId == "edu-test-1"

