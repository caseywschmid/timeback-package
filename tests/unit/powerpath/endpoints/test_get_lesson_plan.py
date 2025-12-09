"""Unit tests for get_lesson_plan endpoint."""

import pytest

from timeback.services.powerpath.endpoints.get_lesson_plan import get_lesson_plan
from timeback.models import LessonPlan


class MockHttpClient:
    """Mock HTTP client for testing."""

    def __init__(self, response_data):
        self.response_data = response_data
        self.last_path = None

    def get(self, path, params=None):
        self.last_path = path
        return self.response_data


def test_get_lesson_plan_success():
    """Test successful retrieval of lesson plan."""
    mock_http = MockHttpClient(
        {
            "lessonPlan": {
                "lessonPlan": {
                    "course": {
                        "sourcedId": "course-123",
                        "status": "active",
                        "title": "Math 101",
                        "org": {"sourcedId": "org-1"},
                    },
                    "subComponents": [
                        {
                            "sourcedId": "unit-1",
                            "status": "active",
                            "title": "Unit 1",
                            "subComponents": [],
                        }
                    ],
                }
            }
        }
    )

    resp = get_lesson_plan(mock_http, "lp-123")

    assert isinstance(resp, LessonPlan)
    assert resp.course["sourcedId"] == "course-123"
    assert resp.course["title"] == "Math 101"


def test_get_lesson_plan_path():
    """Test that the correct path is used."""
    mock_http = MockHttpClient(
        {
            "lessonPlan": {
                "lessonPlan": {
                    "course": {
                        "sourcedId": "c",
                        "status": "active",
                        "title": "T",
                        "org": {"sourcedId": "o"},
                    },
                    "subComponents": [],
                }
            }
        }
    )

    get_lesson_plan(mock_http, "lesson-plan-abc-xyz")

    assert mock_http.last_path == "/powerpath/lessonPlans/tree/lesson-plan-abc-xyz"


def test_get_lesson_plan_with_components():
    """Test lesson plan with nested components."""
    mock_http = MockHttpClient(
        {
            "lessonPlan": {
                "lessonPlan": {
                    "course": {
                        "sourcedId": "course-1",
                        "status": "active",
                        "title": "Course",
                        "org": {"sourcedId": "org"},
                    },
                    "subComponents": [
                        {
                            "sourcedId": "unit-1",
                            "status": "active",
                            "title": "Unit 1",
                            "subComponents": [
                                {
                                    "sourcedId": "lesson-1",
                                    "status": "active",
                                    "title": "Lesson 1",
                                    "subComponents": [],
                                }
                            ],
                        }
                    ],
                }
            }
        }
    )

    resp = get_lesson_plan(mock_http, "lp")

    assert len(resp.subComponents) == 1
    assert resp.subComponents[0].sourcedId == "unit-1"

