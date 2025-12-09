"""Unit tests for get_course_syllabus endpoint."""

import pytest

from timeback.services.powerpath.endpoints.get_course_syllabus import get_course_syllabus
from timeback.models.response import TimebackSyllabusResponse


class MockHttpClient:
    """Mock HTTP client for testing."""

    def __init__(self, response_data):
        self.response_data = response_data
        self.last_path = None

    def get(self, path, params=None):
        self.last_path = path
        return self.response_data


def test_get_course_syllabus_success():
    """Test successful retrieval of course syllabus."""
    mock_http = MockHttpClient(
        {
            "syllabus": {
                "title": "Math 101",
                "units": [
                    {"title": "Unit 1", "lessons": [{"title": "Lesson 1"}]}
                ],
            }
        }
    )

    resp = get_course_syllabus(mock_http, "course-123")

    assert isinstance(resp, TimebackSyllabusResponse)
    assert resp.syllabus["title"] == "Math 101"


def test_get_course_syllabus_path():
    """Test that the correct path is used."""
    mock_http = MockHttpClient({"syllabus": None})

    get_course_syllabus(mock_http, "course-abc-xyz")

    assert mock_http.last_path == "/powerpath/syllabus/course-abc-xyz"


def test_get_course_syllabus_empty():
    """Test when syllabus is empty."""
    mock_http = MockHttpClient({"syllabus": None})

    resp = get_course_syllabus(mock_http, "empty-course")

    assert resp.syllabus is None

