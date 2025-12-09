"""Unit tests for import_external_test_assignment_results endpoint."""

import pytest

from timeback.services.powerpath.endpoints.import_external_test_assignment_results import (
    import_external_test_assignment_results,
)
from timeback.models.response import TimebackImportExternalTestAssignmentResultsResponse
from timeback.models.request import TimebackImportExternalTestAssignmentResultsRequest


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


def test_import_external_test_assignment_results_success():
    """Test successful import of test assignment results."""
    mock_http = MockHttpClient(
        {
            "lessonType": "placement",
            "lessonId": "lesson-123",
            "toolProvider": "edulastic",
            "finalized": True,
            "attempt": 1,
            "credentials": {
                "email": "student@example.com",
                "password": "test-password",
            },
            "assignmentId": "assignment-456",
            "classId": "class-789",
            "testUrl": "https://edulastic.com/test/123",
            "testId": "test-abc",
        }
    )

    request = TimebackImportExternalTestAssignmentResultsRequest(
        student="student-123",
        lesson="lesson-123",
    )
    resp = import_external_test_assignment_results(mock_http, request)

    assert isinstance(resp, TimebackImportExternalTestAssignmentResultsResponse)
    assert resp.lessonType == "placement"
    assert resp.lessonId == "lesson-123"
    assert resp.toolProvider == "edulastic"
    assert resp.finalized is True
    assert resp.attempt == 1
    assert resp.credentials.email == "student@example.com"
    assert resp.assignmentId == "assignment-456"


def test_import_external_test_assignment_results_query_params():
    """Test that the correct query params are sent."""
    mock_http = MockHttpClient(
        {
            "lessonType": "test-out",
            "lessonId": "lesson-456",
            "toolProvider": "mastery-track",
            "finalized": False,
            "attempt": 2,
        }
    )

    request = TimebackImportExternalTestAssignmentResultsRequest(
        student="student-456",
        lesson="lesson-456",
        applicationName="my-app",
    )
    resp = import_external_test_assignment_results(mock_http, request)

    assert mock_http.last_path == "/powerpath/importExternalTestAssignmentResults"
    assert mock_http.last_params == {
        "student": "student-456",
        "lesson": "lesson-456",
        "applicationName": "my-app",
    }


def test_import_external_test_assignment_results_not_finalized():
    """Test when test is not finalized yet."""
    mock_http = MockHttpClient(
        {
            "lessonType": "unit-test",
            "lessonId": "lesson-789",
            "toolProvider": "edulastic",
            "finalized": False,
            "attempt": 1,
            "credentials": {
                "email": "student@test.com",
                "password": "pass",
            },
            "testUrl": "https://edulastic.com/test/789",
        }
    )

    request = TimebackImportExternalTestAssignmentResultsRequest(
        student="student-789",
        lesson="lesson-789",
    )
    resp = import_external_test_assignment_results(mock_http, request)

    assert isinstance(resp, TimebackImportExternalTestAssignmentResultsResponse)
    assert resp.finalized is False
    assert resp.credentials is not None
    assert resp.testUrl == "https://edulastic.com/test/789"


def test_import_external_test_assignment_results_minimal_response():
    """Test with minimal response (only required fields)."""
    mock_http = MockHttpClient(
        {
            "lessonType": "placement",
            "lessonId": None,
            "toolProvider": None,
            "finalized": False,
            "attempt": 0,
        }
    )

    request = TimebackImportExternalTestAssignmentResultsRequest(
        student="new-student",
        lesson="new-lesson",
    )
    resp = import_external_test_assignment_results(mock_http, request)

    assert isinstance(resp, TimebackImportExternalTestAssignmentResultsResponse)
    assert resp.lessonId is None
    assert resp.toolProvider is None
    assert resp.credentials is None
    assert resp.assignmentId is None

