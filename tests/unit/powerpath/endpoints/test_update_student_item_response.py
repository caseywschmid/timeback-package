"""Unit tests for update_student_item_response endpoint."""

import pytest

from timeback.services.powerpath.endpoints.update_student_item_response import (
    update_student_item_response,
)
from timeback.models.request import (
    TimebackUpdateStudentItemResponseRequest,
    TimebackStudentItemResult,
)
from timeback.models.response import TimebackUpdateStudentItemResponseResponse


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


def test_update_student_item_response_success():
    """Test successful update of student item response."""
    mock_http = MockHttpClient(
        {
            "componentResourceLineItem": {
                "sourcedId": "ali-123",
                "status": "active",
                "title": "Quiz 1",
            },
            "componentResourceResult": {
                "sourcedId": "result-456",
                "score": 85.5,
                "scoreStatus": "fully graded",
            },
        }
    )

    result = TimebackStudentItemResult(
        status="active",
        scoreDate="2024-01-15T10:00:00Z",
        scoreStatus="fully graded",
        score=85.5,
    )
    request = TimebackUpdateStudentItemResponseRequest(
        student_id="student-123",
        component_resource_id="res-456",
        result=result,
    )
    resp = update_student_item_response(mock_http, request)

    assert isinstance(resp, TimebackUpdateStudentItemResponseResponse)
    assert resp.componentResourceLineItem["sourcedId"] == "ali-123"
    assert resp.componentResourceResult["score"] == 85.5


def test_update_student_item_response_path():
    """Test that the correct path is used."""
    mock_http = MockHttpClient({})

    result = TimebackStudentItemResult(
        status="active",
        scoreDate="2024-01-15T10:00:00Z",
        scoreStatus="submitted",
    )
    request = TimebackUpdateStudentItemResponseRequest(
        student_id="s",
        component_resource_id="r",
        result=result,
    )
    update_student_item_response(mock_http, request)

    assert mock_http.last_path == "/powerpath/lessonPlans/updateStudentItemResponse"


def test_update_student_item_response_body():
    """Test that the correct body is sent."""
    mock_http = MockHttpClient({})

    result = TimebackStudentItemResult(
        status="active",
        scoreDate="2024-01-15T10:00:00Z",
        scoreStatus="partially graded",
        score=70.0,
        comment="Needs improvement",
    )
    request = TimebackUpdateStudentItemResponseRequest(
        student_id="student-abc",
        component_resource_id="res-xyz",
        result=result,
    )
    update_student_item_response(mock_http, request)

    assert mock_http.last_json["studentId"] == "student-abc"
    assert mock_http.last_json["componentResourceId"] == "res-xyz"
    assert mock_http.last_json["result"]["score"] == 70.0
    assert mock_http.last_json["result"]["comment"] == "Needs improvement"


def test_update_student_item_response_minimal():
    """Test with minimal required fields."""
    mock_http = MockHttpClient({})

    result = TimebackStudentItemResult(
        status="active",
        scoreDate="2024-01-15T10:00:00Z",
        scoreStatus="not submitted",
    )
    request = TimebackUpdateStudentItemResponseRequest(
        student_id="s",
        component_resource_id="r",
        result=result,
    )
    update_student_item_response(mock_http, request)

    # Should not have optional fields
    assert "score" not in mock_http.last_json["result"]
    assert "comment" not in mock_http.last_json["result"]

