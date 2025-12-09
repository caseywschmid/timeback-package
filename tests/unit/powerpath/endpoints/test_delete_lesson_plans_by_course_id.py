"""Unit tests for delete_lesson_plans_by_course_id endpoint."""

import pytest

from timeback.services.powerpath.endpoints.delete_lesson_plans_by_course_id import (
    delete_lesson_plans_by_course_id,
)


class MockHttpClient:
    """Mock HTTP client for testing."""

    def __init__(self, response_data=None):
        self.response_data = response_data
        self.last_path = None

    def delete(self, path):
        self.last_path = path
        return self.response_data


def test_delete_lesson_plans_by_course_id_success():
    """Test successful deletion of all lesson plans for a course."""
    mock_http = MockHttpClient(None)  # 204 returns None

    result = delete_lesson_plans_by_course_id(mock_http, "course-123")

    assert result is None
    assert mock_http.last_path == "/powerpath/lessonPlans/course-123/deleteAll"


def test_delete_lesson_plans_by_course_id_path():
    """Test that the correct path is used."""
    mock_http = MockHttpClient(None)

    delete_lesson_plans_by_course_id(mock_http, "my-course-abc")

    assert mock_http.last_path == "/powerpath/lessonPlans/my-course-abc/deleteAll"


def test_delete_lesson_plans_by_course_id_different_courses():
    """Test deletion works for different courses."""
    course_ids = ["course-a", "course-b", "course-c"]

    for course_id in course_ids:
        mock_http = MockHttpClient(None)
        result = delete_lesson_plans_by_course_id(mock_http, course_id)

        assert result is None
        assert mock_http.last_path == f"/powerpath/lessonPlans/{course_id}/deleteAll"

