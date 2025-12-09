"""Unit tests for create_lesson_plan endpoint."""

import pytest

from timeback.services.powerpath.endpoints.create_lesson_plan import create_lesson_plan
from timeback.models.response import TimebackCreateLessonPlanResponse
from timeback.models.request import TimebackCreateLessonPlanRequest


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


def test_create_lesson_plan_success():
    """Test successful creation of a lesson plan."""
    mock_http = MockHttpClient({"lessonPlanId": "lp-123-456"})

    request = TimebackCreateLessonPlanRequest(
        course_id="course-abc",
        user_id="user-xyz",
    )
    resp = create_lesson_plan(mock_http, request)

    assert isinstance(resp, TimebackCreateLessonPlanResponse)
    assert resp.lessonPlanId == "lp-123-456"


def test_create_lesson_plan_path_and_body():
    """Test that the correct path and body are sent."""
    mock_http = MockHttpClient({"lessonPlanId": "lp-new"})

    request = TimebackCreateLessonPlanRequest(
        course_id="course-123",
        user_id="student-456",
    )
    resp = create_lesson_plan(mock_http, request)

    assert mock_http.last_path == "/powerpath/lessonPlans/"
    assert mock_http.last_json == {
        "courseId": "course-123",
        "userId": "student-456",
    }


def test_create_lesson_plan_with_class_id():
    """Test lesson plan creation with optional classId."""
    mock_http = MockHttpClient({"lessonPlanId": "lp-with-class"})

    request = TimebackCreateLessonPlanRequest(
        course_id="course-abc",
        user_id="user-xyz",
        class_id="class-123",
    )
    resp = create_lesson_plan(mock_http, request)

    assert mock_http.last_json == {
        "courseId": "course-abc",
        "userId": "user-xyz",
        "classId": "class-123",
    }
    assert resp.lessonPlanId == "lp-with-class"


def test_create_lesson_plan_existing():
    """Test when lesson plan already exists (returns 200 with existing ID)."""
    mock_http = MockHttpClient({"lessonPlanId": "existing-lp-id"})

    request = TimebackCreateLessonPlanRequest(
        course_id="course-existing",
        user_id="user-existing",
    )
    resp = create_lesson_plan(mock_http, request)

    assert isinstance(resp, TimebackCreateLessonPlanResponse)
    assert resp.lessonPlanId == "existing-lp-id"

