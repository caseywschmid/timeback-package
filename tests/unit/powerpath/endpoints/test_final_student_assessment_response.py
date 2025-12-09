"""Unit tests for final_student_assessment_response endpoint."""

import pytest

from timeback.services.powerpath.endpoints.final_student_assessment_response import (
    final_student_assessment_response,
)
from timeback.models.request import TimebackFinalStudentAssessmentRequest
from timeback.models.response import TimebackFinalStudentAssessmentResponse


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


def test_final_student_assessment_response_success():
    """Test successful finalization of assessment."""
    mock_http = MockHttpClient(
        {"lessonType": "quiz", "finalized": True, "attempt": 1}
    )

    request = TimebackFinalStudentAssessmentRequest(
        student="student-123",
        lesson="lesson-456",
    )
    resp = final_student_assessment_response(mock_http, request)

    assert isinstance(resp, TimebackFinalStudentAssessmentResponse)
    assert resp.lessonType == "quiz"
    assert resp.finalized is True
    assert resp.attempt == 1


def test_final_student_assessment_response_path():
    """Test that the correct path is used."""
    mock_http = MockHttpClient(
        {"lessonType": "test-out", "finalized": True, "attempt": 1}
    )

    request = TimebackFinalStudentAssessmentRequest(student="s", lesson="l")
    final_student_assessment_response(mock_http, request)

    assert mock_http.last_path == "/powerpath/finalStudentAssessmentResponse"


def test_final_student_assessment_response_body():
    """Test that correct body is sent."""
    mock_http = MockHttpClient(
        {"lessonType": "placement", "finalized": True, "attempt": 1}
    )

    request = TimebackFinalStudentAssessmentRequest(
        student="student-abc",
        lesson="lesson-xyz",
    )
    final_student_assessment_response(mock_http, request)

    assert mock_http.last_json["student"] == "student-abc"
    assert mock_http.last_json["lesson"] == "lesson-xyz"


def test_final_student_assessment_response_not_finalized():
    """Test when lesson was already finalized."""
    mock_http = MockHttpClient(
        {"lessonType": "unit-test", "finalized": False, "attempt": 2}
    )

    request = TimebackFinalStudentAssessmentRequest(student="s", lesson="l")
    resp = final_student_assessment_response(mock_http, request)

    assert resp.finalized is False
    assert resp.attempt == 2

