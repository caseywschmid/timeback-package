"""Unit tests for start_test_out endpoint."""

import pytest

from timeback.services.powerpath.endpoints.start_test_out import start_test_out
from timeback.models.response import TimebackStartTestOutResponse
from timeback.models.request import TimebackStartTestOutRequest


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


def test_start_test_out_success_created():
    """Test successful creation of a new test-out assignment."""
    mock_http = MockHttpClient(
        {
            "assignmentId": "assign-123",
            "lessonId": "lesson-456",
            "resourceId": "resource-789",
            "status": "created",
        }
    )

    request = TimebackStartTestOutRequest(
        course_id="course-abc",
        student_id="student-xyz",
    )
    resp = start_test_out(mock_http, request)

    assert isinstance(resp, TimebackStartTestOutResponse)
    assert resp.assignmentId == "assign-123"
    assert resp.lessonId == "lesson-456"
    assert resp.resourceId == "resource-789"
    assert resp.status == "created"


def test_start_test_out_success_existing():
    """Test when existing assignment is reused."""
    mock_http = MockHttpClient(
        {
            "assignmentId": "existing-assign",
            "lessonId": "existing-lesson",
            "resourceId": "existing-resource",
            "status": "existing",
        }
    )

    request = TimebackStartTestOutRequest(
        course_id="course-abc",
        student_id="student-xyz",
    )
    resp = start_test_out(mock_http, request)

    assert resp.status == "existing"


def test_start_test_out_path_and_body():
    """Test that the correct path and body are sent."""
    mock_http = MockHttpClient(
        {
            "assignmentId": "a1",
            "lessonId": "l1",
            "resourceId": "r1",
            "status": "created",
        }
    )

    request = TimebackStartTestOutRequest(
        course_id="my-course",
        student_id="my-student",
    )
    resp = start_test_out(mock_http, request)

    assert mock_http.last_path == "/powerpath/lessonPlans/startTestOut"
    assert mock_http.last_json == {
        "courseId": "my-course",
        "studentId": "my-student",
    }

