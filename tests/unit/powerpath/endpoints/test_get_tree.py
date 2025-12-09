"""Unit tests for get_tree endpoint."""

import pytest

from timeback.services.powerpath.endpoints.get_tree import get_tree
from timeback.models import LessonPlan
from timeback.models.request import TimebackGetTreeRequest


class MockHttpClient:
    """Mock HTTP client for testing."""

    def __init__(self, response_data):
        self.response_data = response_data
        self.last_path = None

    def get(self, path, params=None):
        self.last_path = path
        return self.response_data


def test_get_tree_success():
    """Test successful retrieval of lesson plan tree."""
    mock_http = MockHttpClient(
        {
            "lessonPlan": {
                "lessonPlan": {
                    "course": {
                        "sourcedId": "course-123",
                        "status": "active",
                        "title": "Math Grade 5",
                        "org": {"sourcedId": "org-1"},
                    },
                    "subComponents": [
                        {
                            "sourcedId": "unit-1",
                            "title": "Unit 1: Numbers",
                            "status": "active",
                            "sortOrder": "1",
                            "componentResources": [],
                            "subComponents": [],
                        },
                        {
                            "sourcedId": "unit-2",
                            "title": "Unit 2: Algebra",
                            "status": "active",
                            "sortOrder": "2",
                            "componentResources": [],
                            "subComponents": [],
                        },
                    ],
                }
            }
        }
    )

    request = TimebackGetTreeRequest(
        course_id="course-123",
        user_id="student-456",
    )
    resp = get_tree(mock_http, request)

    assert isinstance(resp, LessonPlan)
    assert resp.course["sourcedId"] == "course-123"
    assert resp.course["title"] == "Math Grade 5"
    assert len(resp.subComponents) == 2
    assert resp.subComponents[0].sourcedId == "unit-1"


def test_get_tree_path():
    """Test that the correct path is used."""
    mock_http = MockHttpClient(
        {
            "lessonPlan": {
                "lessonPlan": {
                    "course": {
                        "sourcedId": "c1",
                        "status": "active",
                        "title": "Course",
                        "org": {"sourcedId": "org"},
                    },
                    "subComponents": [],
                }
            }
        }
    )

    request = TimebackGetTreeRequest(
        course_id="course-abc",
        user_id="user-xyz",
    )
    resp = get_tree(mock_http, request)

    assert mock_http.last_path == "/powerpath/lessonPlans/course-abc/user-xyz"


def test_get_tree_empty_subcomponents():
    """Test when there are no subcomponents."""
    mock_http = MockHttpClient(
        {
            "lessonPlan": {
                "lessonPlan": {
                    "course": {
                        "sourcedId": "empty-course",
                        "status": "active",
                        "title": "Empty Course",
                        "org": {"sourcedId": "org"},
                    },
                    "subComponents": [],
                }
            }
        }
    )

    request = TimebackGetTreeRequest(
        course_id="empty-course",
        user_id="student",
    )
    resp = get_tree(mock_http, request)

    assert isinstance(resp, LessonPlan)
    assert len(resp.subComponents) == 0

