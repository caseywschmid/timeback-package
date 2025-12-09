"""Unit tests for make_external_test_assignment endpoint."""

import pytest

from timeback.services.powerpath.endpoints.make_external_test_assignment import (
    make_external_test_assignment,
)
from timeback.models.response import TimebackMakeExternalTestAssignmentResponse
from timeback.models.request import TimebackMakeExternalTestAssignmentRequest


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


def test_make_external_test_assignment_success():
    """Test successful test assignment."""
    mock_http = MockHttpClient(
        {
            "toolProvider": "edulastic",
            "lessonType": "placement",
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

    request = TimebackMakeExternalTestAssignmentRequest(
        student="student-123",
        lesson="lesson-123",
    )
    resp = make_external_test_assignment(mock_http, request)

    assert isinstance(resp, TimebackMakeExternalTestAssignmentResponse)
    assert resp.toolProvider == "edulastic"
    assert resp.lessonType == "placement"
    assert resp.attempt == 1
    assert resp.credentials.email == "student@example.com"
    assert resp.testUrl == "https://edulastic.com/test/123"


def test_make_external_test_assignment_path_and_body():
    """Test that the correct path and body are sent."""
    mock_http = MockHttpClient(
        {
            "toolProvider": "mastery-track",
            "lessonType": "test-out",
            "attempt": 2,
        }
    )

    request = TimebackMakeExternalTestAssignmentRequest(
        student="student-456",
        lesson="lesson-456",
        applicationName="my-app",
        testId="specific-test-123",
        skipCourseEnrollment=True,
    )
    resp = make_external_test_assignment(mock_http, request)

    assert mock_http.last_path == "/powerpath/makeExternalTestAssignment"
    assert mock_http.last_json == {
        "student": "student-456",
        "lesson": "lesson-456",
        "applicationName": "my-app",
        "testId": "specific-test-123",
        "skipCourseEnrollment": True,
    }


def test_make_external_test_assignment_minimal_required():
    """Test with only required fields."""
    mock_http = MockHttpClient(
        {
            "toolProvider": "edulastic",
            "lessonType": "unit-test",
            "attempt": 1,
        }
    )

    request = TimebackMakeExternalTestAssignmentRequest(
        student="new-student",
        lesson="new-lesson",
    )
    resp = make_external_test_assignment(mock_http, request)

    assert isinstance(resp, TimebackMakeExternalTestAssignmentResponse)
    assert mock_http.last_json == {
        "student": "new-student",
        "lesson": "new-lesson",
    }
    assert "applicationName" not in mock_http.last_json
    assert "testId" not in mock_http.last_json
    assert "skipCourseEnrollment" not in mock_http.last_json


def test_make_external_test_assignment_skip_enrollment():
    """Test with skipCourseEnrollment flag."""
    mock_http = MockHttpClient(
        {
            "toolProvider": "edulastic",
            "lessonType": "placement",
            "attempt": 1,
            "credentials": {
                "email": "student@test.com",
                "password": "pass",
            },
        }
    )

    request = TimebackMakeExternalTestAssignmentRequest(
        student="student-789",
        lesson="placement-lesson",
        skipCourseEnrollment=True,
    )
    resp = make_external_test_assignment(mock_http, request)

    assert isinstance(resp, TimebackMakeExternalTestAssignmentResponse)
    assert mock_http.last_json["skipCourseEnrollment"] is True

