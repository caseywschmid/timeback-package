"""Unit tests for sync_course_lesson_plans endpoint."""

import pytest

from timeback.services.powerpath.endpoints.sync_course_lesson_plans import (
    sync_course_lesson_plans,
)
from timeback.models.response import TimebackSyncCourseLessonPlansResponse


class MockHttpClient:
    """Mock HTTP client for testing."""

    def __init__(self, response_data):
        self.response_data = response_data
        self.last_path = None

    def post(self, path, json=None):
        self.last_path = path
        return self.response_data


def test_sync_course_lesson_plans_success():
    """Test successful sync of all lesson plans for a course."""
    mock_http = MockHttpClient(
        {"lessonPlansAffected": ["lp-1", "lp-2", "lp-3", "lp-4"]}
    )

    resp = sync_course_lesson_plans(mock_http, "course-123")

    assert isinstance(resp, TimebackSyncCourseLessonPlansResponse)
    assert len(resp.lessonPlansAffected) == 4
    assert "lp-1" in resp.lessonPlansAffected


def test_sync_course_lesson_plans_path():
    """Test that the correct path is used."""
    mock_http = MockHttpClient({"lessonPlansAffected": []})

    sync_course_lesson_plans(mock_http, "course-abc-xyz")

    assert mock_http.last_path == "/powerpath/lessonPlans/course/course-abc-xyz/sync"


def test_sync_course_lesson_plans_no_plans():
    """Test when there are no lesson plans for the course."""
    mock_http = MockHttpClient({"lessonPlansAffected": []})

    resp = sync_course_lesson_plans(mock_http, "new-course")

    assert isinstance(resp, TimebackSyncCourseLessonPlansResponse)
    assert len(resp.lessonPlansAffected) == 0


def test_sync_course_lesson_plans_many():
    """Test sync with many lesson plans."""
    affected = [f"lp-{i}" for i in range(100)]
    mock_http = MockHttpClient({"lessonPlansAffected": affected})

    resp = sync_course_lesson_plans(mock_http, "popular-course")

    assert len(resp.lessonPlansAffected) == 100

