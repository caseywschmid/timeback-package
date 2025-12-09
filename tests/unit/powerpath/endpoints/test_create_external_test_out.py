"""Unit tests for create_external_test_out endpoint."""

import pytest
import warnings

from timeback.services.powerpath.endpoints.create_external_test_out import (
    create_external_test_out,
)
from timeback.models.response import TimebackCreateExternalTestResponse
from timeback.models.request import TimebackCreateExternalTestOutRequest


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


def test_create_external_test_out_success():
    """Test successful creation of external test-out."""
    mock_http = MockHttpClient(
        {
            "lessonType": "test-out",
            "lessonId": "lesson-123",
            "courseComponentId": "component-456",
            "resourceId": "resource-789",
            "toolProvider": "edulastic",
            "launchUrl": "https://edulastic.com/test/123",
            "vendorId": "vendor-test-1",
            "grades": ["5", "6"],
        }
    )

    request = TimebackCreateExternalTestOutRequest(
        courseId="course-123",
        toolProvider="edulastic",
        grades=["5", "6"],
        xp=100,
        lessonTitle="Grade 5-6 Test-Out",
        launchUrl="https://edulastic.com/test/123",
    )

    # Suppress the deprecation warning for this test
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        resp = create_external_test_out(mock_http, request)

    assert isinstance(resp, TimebackCreateExternalTestResponse)
    assert resp.lessonType == "test-out"
    assert resp.lessonId == "lesson-123"
    assert resp.courseComponentId == "component-456"
    assert resp.resourceId == "resource-789"
    assert resp.toolProvider == "edulastic"


def test_create_external_test_out_emits_deprecation_warning():
    """Test that the endpoint emits a deprecation warning."""
    mock_http = MockHttpClient(
        {
            "lessonType": "test-out",
            "lessonId": "lesson-id",
            "courseComponentId": "component-id",
            "resourceId": "resource-id",
            "toolProvider": "edulastic",
        }
    )

    request = TimebackCreateExternalTestOutRequest(
        courseId="course-123",
        toolProvider="edulastic",
        grades=["3"],
        xp=50,
    )

    with pytest.warns(DeprecationWarning, match="create_external_test_out is deprecated"):
        create_external_test_out(mock_http, request)


def test_create_external_test_out_path_and_body():
    """Test that the correct path and body are sent."""
    mock_http = MockHttpClient(
        {
            "lessonType": "test-out",
            "lessonId": "lesson-id",
            "courseComponentId": "component-id",
            "resourceId": "resource-id",
            "toolProvider": "mastery-track",
        }
    )

    request = TimebackCreateExternalTestOutRequest(
        courseId="course-456",
        toolProvider="mastery-track",
        grades=["3", "4"],
        xp=75,
        unitTitle="Test-Out Unit",
    )

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        resp = create_external_test_out(mock_http, request)

    assert mock_http.last_path == "/powerpath/createExternalTestOut"
    assert mock_http.last_json["courseId"] == "course-456"
    assert mock_http.last_json["toolProvider"] == "mastery-track"
    assert mock_http.last_json["grades"] == ["3", "4"]
    assert mock_http.last_json["lessonType"] == "test-out"
    assert mock_http.last_json["xp"] == 75
    assert mock_http.last_json["unitTitle"] == "Test-Out Unit"


def test_create_external_test_out_minimal_required():
    """Test with only required fields."""
    mock_http = MockHttpClient(
        {
            "lessonType": "test-out",
            "lessonId": "minimal-lesson",
            "courseComponentId": "minimal-component",
            "resourceId": "minimal-resource",
            "toolProvider": "edulastic",
        }
    )

    request = TimebackCreateExternalTestOutRequest(
        courseId="minimal-course",
        toolProvider="edulastic",
        grades=["1"],
        xp=25,
    )

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        resp = create_external_test_out(mock_http, request)

    assert isinstance(resp, TimebackCreateExternalTestResponse)
    # Check that optional fields are not sent when not provided
    assert "lessonTitle" not in mock_http.last_json
    assert "launchUrl" not in mock_http.last_json
    # Required fields should be present
    assert mock_http.last_json["xp"] == 25

