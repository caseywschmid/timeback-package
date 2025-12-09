"""Unit tests for get_subject_progress endpoint."""

import pytest

from timeback.services.powerpath.endpoints.get_subject_progress import get_subject_progress
from timeback.models.response import TimebackGetSubjectProgressResponse
from timeback.models.request import TimebackGetSubjectProgressRequest
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


def minimal_progress_item(idx: str):
    """Create a minimal progress item for testing."""
    return {
        "course": {
            "sourcedId": f"course-{idx}",
            "title": f"Course {idx}",
            "courseCode": f"C{idx}",
            "level": "1",
            "grades": ["3", "4", "5"],
            "subjects": ["Reading"],
            "status": "active",
            "orgSourcedId": "org-123",
            "dateLastModified": "2024-01-01T00:00:00Z",
        },
        "inEnrolled": True,
        "hasUsedTestOut": False,
        "testOutLessonId": f"testout-{idx}",
        "completedLessons": 5,
        "totalLessons": 10,
        "totalAttainableXp": 1000,
        "totalXpEarned": 500,
    }


def test_get_subject_progress_success():
    """Test successful retrieval of subject progress."""
    mock_http = MockHttpClient(
        {
            "progress": [minimal_progress_item("1"), minimal_progress_item("2")],
        }
    )

    request = TimebackGetSubjectProgressRequest(
        student="student-123",
        subject=TimebackSubject.READING,
    )
    resp = get_subject_progress(mock_http, request)

    assert isinstance(resp, TimebackGetSubjectProgressResponse)
    assert len(resp.progress) == 2
    assert resp.progress[0].course.sourcedId == "course-1"
    assert resp.progress[0].completedLessons == 5
    assert resp.progress[0].totalLessons == 10
    assert resp.progress[0].totalXpEarned == 500


def test_get_subject_progress_passes_query_params():
    """Test that student and subject are passed as query params."""
    mock_http = MockHttpClient(
        {
            "progress": [minimal_progress_item("1")],
        }
    )

    request = TimebackGetSubjectProgressRequest(
        student="student-456",
        subject=TimebackSubject.MATH,
    )
    resp = get_subject_progress(mock_http, request)

    assert isinstance(resp, TimebackGetSubjectProgressResponse)
    assert mock_http.last_path == "/powerpath/placement/getSubjectProgress"
    assert mock_http.last_params == {
        "student": "student-456",
        "subject": "Math",
    }


def test_get_subject_progress_empty_results():
    """Test handling of empty progress list."""
    mock_http = MockHttpClient(
        {
            "progress": [],
        }
    )

    request = TimebackGetSubjectProgressRequest(
        student="new-student",
        subject=TimebackSubject.SCIENCE,
    )
    resp = get_subject_progress(mock_http, request)

    assert isinstance(resp, TimebackGetSubjectProgressResponse)
    assert len(resp.progress) == 0


def test_get_subject_progress_with_null_optional_fields():
    """Test handling of null optional fields in course."""
    mock_http = MockHttpClient(
        {
            "progress": [
                {
                    "course": {
                        "sourcedId": "course-1",
                        "title": "Course 1",
                        "courseCode": None,
                        "level": None,
                        "grades": None,
                        "subjects": None,
                        "status": "active",
                        "orgSourcedId": "org-123",
                        "dateLastModified": "2024-01-01T00:00:00Z",
                    },
                    "inEnrolled": False,
                    "hasUsedTestOut": True,
                    "testOutLessonId": None,
                    "completedLessons": 0,
                    "totalLessons": 5,
                    "totalAttainableXp": 500,
                    "totalXpEarned": 0,
                }
            ],
        }
    )

    request = TimebackGetSubjectProgressRequest(
        student="student-789",
        subject=TimebackSubject.LANGUAGE,
    )
    resp = get_subject_progress(mock_http, request)

    assert isinstance(resp, TimebackGetSubjectProgressResponse)
    assert len(resp.progress) == 1
    assert resp.progress[0].course.courseCode is None
    assert resp.progress[0].course.level is None
    assert resp.progress[0].course.grades is None
    assert resp.progress[0].testOutLessonId is None
    assert resp.progress[0].inEnrolled is False
    assert resp.progress[0].hasUsedTestOut is True

