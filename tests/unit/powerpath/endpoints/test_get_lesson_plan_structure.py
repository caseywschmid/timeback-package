"""Unit tests for get_lesson_plan_structure endpoint."""

import pytest

from timeback.services.powerpath.endpoints.get_lesson_plan_structure import (
    get_lesson_plan_structure,
)
from timeback.models.response import TimebackLessonPlanStructureResponse


class MockHttpClient:
    """Mock HTTP client for testing."""

    def __init__(self, response_data):
        self.response_data = response_data
        self.last_path = None

    def get(self, path, params=None):
        self.last_path = path
        return self.response_data


def test_get_lesson_plan_structure_success():
    """Test successful retrieval of lesson plan structure."""
    mock_http = MockHttpClient(
        {
            "lessonPlan": {
                "lessonPlan": {
                    "id": "lp-123",
                    "courseId": "course-456",
                    "courseTitle": "Math 101",
                    "structure": [
                        {
                            "type": "component",
                            "title": "Unit 1",
                            "order": "1",
                            "skipped": False,
                            "itemId": "item-1",
                            "componentId": "comp-1",
                        },
                        {
                            "type": "resource",
                            "title": "Video 1",
                            "order": "1.1",
                            "skipped": True,
                            "itemId": "item-2",
                            "componentResourceId": "res-1",
                        },
                    ],
                }
            }
        }
    )

    resp = get_lesson_plan_structure(mock_http, "lp-123")

    assert isinstance(resp, TimebackLessonPlanStructureResponse)
    data = resp.lessonPlan.lessonPlan
    assert data.id == "lp-123"
    assert data.courseTitle == "Math 101"
    assert len(data.structure) == 2
    assert data.structure[0].type == "component"
    assert data.structure[1].skipped is True


def test_get_lesson_plan_structure_path():
    """Test that the correct path is used."""
    mock_http = MockHttpClient(
        {
            "lessonPlan": {
                "lessonPlan": {
                    "id": "x",
                    "courseId": "y",
                    "courseTitle": "z",
                    "structure": [],
                }
            }
        }
    )

    get_lesson_plan_structure(mock_http, "lp-abc-xyz")

    assert mock_http.last_path == "/powerpath/lessonPlans/tree/lp-abc-xyz/structure"


def test_get_lesson_plan_structure_nested():
    """Test structure with nested components."""
    mock_http = MockHttpClient(
        {
            "lessonPlan": {
                "lessonPlan": {
                    "id": "lp",
                    "courseId": "c",
                    "courseTitle": "Course",
                    "structure": [
                        {
                            "type": "component",
                            "title": "Unit",
                            "order": "1",
                            "skipped": False,
                            "itemId": "i1",
                            "subComponents": [
                                {
                                    "type": "component",
                                    "title": "Lesson",
                                    "order": "1.1",
                                    "skipped": False,
                                    "itemId": "i2",
                                }
                            ],
                        }
                    ],
                }
            }
        }
    )

    resp = get_lesson_plan_structure(mock_http, "lp")

    assert len(resp.lessonPlan.lessonPlan.structure[0].subComponents) == 1

