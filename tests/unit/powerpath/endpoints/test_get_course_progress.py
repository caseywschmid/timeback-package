"""Unit tests for get_course_progress endpoint."""

import pytest

from timeback.services.powerpath.endpoints.get_course_progress import get_course_progress
from timeback.models.response import TimebackCourseProgressResponse


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


def test_get_course_progress_success():
    """Test successful retrieval of course progress."""
    mock_http = MockHttpClient(
        {
            "lineItems": [
                {
                    "type": "component",
                    "assessmentLineItemSourcedId": "ali-1",
                    "courseComponentSourcedId": "comp-1",
                    "title": "Unit 1",
                    "results": [],
                },
                {
                    "type": "resource",
                    "assessmentLineItemSourcedId": "ali-2",
                    "courseComponentResourceSourcedId": "res-1",
                    "title": "Quiz 1",
                    "results": [
                        {
                            "status": "active",
                            "scoreDate": "2024-01-15T10:00:00Z",
                            "scoreStatus": "fully graded",
                            "score": 85.5,
                        }
                    ],
                },
            ],
            "testOut": {"status": "available"},
        }
    )

    resp = get_course_progress(mock_http, "course-123", "student-456")

    assert isinstance(resp, TimebackCourseProgressResponse)
    assert len(resp.lineItems) == 2
    assert resp.testOut["status"] == "available"


def test_get_course_progress_path():
    """Test that the correct path is used."""
    mock_http = MockHttpClient({"lineItems": [], "testOut": {"status": "not_eligible"}})

    get_course_progress(mock_http, "course-abc", "student-xyz")

    assert (
        mock_http.last_path
        == "/powerpath/lessonPlans/getCourseProgress/course-abc/student/student-xyz"
    )
    assert mock_http.last_params is None


def test_get_course_progress_with_lesson_filter():
    """Test filtering by lesson ID."""
    mock_http = MockHttpClient({"lineItems": [], "testOut": {"status": "not_eligible"}})

    get_course_progress(mock_http, "course-1", "student-1", lesson_id="lesson-123")

    assert mock_http.last_params == {"lessonId": "lesson-123"}


def test_get_course_progress_test_out_in_progress():
    """Test test-out status in_progress."""
    mock_http = MockHttpClient(
        {
            "lineItems": [],
            "testOut": {
                "status": "in_progress",
                "assignmentId": "assign-1",
                "lessonId": "lesson-1",
            },
        }
    )

    resp = get_course_progress(mock_http, "c", "s")

    assert resp.testOut["status"] == "in_progress"
    assert resp.testOut["assignmentId"] == "assign-1"

