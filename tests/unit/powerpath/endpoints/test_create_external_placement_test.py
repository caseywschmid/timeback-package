"""Unit tests for create_external_placement_test endpoint."""

import pytest

from timeback.services.powerpath.endpoints.create_external_placement_test import (
    create_external_placement_test,
)
from timeback.models.response import TimebackCreateExternalTestResponse
from timeback.models.request import TimebackCreateExternalPlacementTestRequest


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


def test_create_external_placement_test_success():
    """Test successful creation of external placement test."""
    mock_http = MockHttpClient(
        {
            "lessonType": "placement",
            "lessonId": "lesson-123",
            "courseComponentId": "component-456",
            "resourceId": "resource-789",
            "toolProvider": "edulastic",
            "launchUrl": "https://edulastic.com/test/123",
            "vendorId": "vendor-test-1",
            "courseIdOnFail": "fallback-course-id",
            "grades": ["5", "6"],
        }
    )

    request = TimebackCreateExternalPlacementTestRequest(
        courseId="course-123",
        toolProvider="edulastic",
        grades=["5", "6"],
        lessonTitle="Grade 5-6 Placement Test",
        launchUrl="https://edulastic.com/test/123",
    )
    resp = create_external_placement_test(mock_http, request)

    assert isinstance(resp, TimebackCreateExternalTestResponse)
    assert resp.lessonType == "placement"
    assert resp.lessonId == "lesson-123"
    assert resp.courseComponentId == "component-456"
    assert resp.resourceId == "resource-789"
    assert resp.toolProvider == "edulastic"


def test_create_external_placement_test_path_and_body():
    """Test that the correct path and body are sent."""
    mock_http = MockHttpClient(
        {
            "lessonType": "placement",
            "lessonId": "lesson-id",
            "courseComponentId": "component-id",
            "resourceId": "resource-id",
            "toolProvider": "mastery-track",
        }
    )

    request = TimebackCreateExternalPlacementTestRequest(
        courseId="course-456",
        toolProvider="mastery-track",
        grades=["3", "4"],
        unitTitle="Placement Unit",
    )
    resp = create_external_placement_test(mock_http, request)

    assert mock_http.last_path == "/powerpath/createExternalPlacementTest"
    assert mock_http.last_json["courseId"] == "course-456"
    assert mock_http.last_json["toolProvider"] == "mastery-track"
    assert mock_http.last_json["grades"] == ["3", "4"]
    assert mock_http.last_json["lessonType"] == "placement"
    assert mock_http.last_json["unitTitle"] == "Placement Unit"


def test_create_external_placement_test_minimal_required():
    """Test with only required fields."""
    mock_http = MockHttpClient(
        {
            "lessonType": "placement",
            "lessonId": "minimal-lesson",
            "courseComponentId": "minimal-component",
            "resourceId": "minimal-resource",
            "toolProvider": "edulastic",
        }
    )

    request = TimebackCreateExternalPlacementTestRequest(
        courseId="minimal-course",
        toolProvider="edulastic",
        grades=["1"],
    )
    resp = create_external_placement_test(mock_http, request)

    assert isinstance(resp, TimebackCreateExternalTestResponse)
    # Check that optional fields are not sent when not provided
    assert "lessonTitle" not in mock_http.last_json
    assert "launchUrl" not in mock_http.last_json
    assert "courseIdOnFail" not in mock_http.last_json


def test_create_external_placement_test_with_course_on_fail():
    """Test with courseIdOnFail specified."""
    mock_http = MockHttpClient(
        {
            "lessonType": "placement",
            "lessonId": "lesson-with-fallback",
            "courseComponentId": "component-id",
            "resourceId": "resource-id",
            "toolProvider": "edulastic",
            "courseIdOnFail": "remedial-course-id",
        }
    )

    request = TimebackCreateExternalPlacementTestRequest(
        courseId="advanced-course",
        toolProvider="edulastic",
        grades=["8", "9"],
        courseIdOnFail="remedial-course-id",
    )
    resp = create_external_placement_test(mock_http, request)

    assert isinstance(resp, TimebackCreateExternalTestResponse)
    assert resp.courseIdOnFail == "remedial-course-id"
    assert mock_http.last_json["courseIdOnFail"] == "remedial-course-id"

