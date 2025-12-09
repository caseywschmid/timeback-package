"""Unit tests for create_test_assignment endpoint."""

import pytest

from timeback.services.powerpath.endpoints.create_test_assignment import (
    create_test_assignment,
)
from timeback.models.request import TimebackCreateTestAssignmentRequest
from timeback.models.response import TimebackCreateTestAssignmentResponse
from timeback.enums import TimebackSubject, TimebackGrade


class MockHttp:
    """Mock HTTP client for testing."""

    def __init__(self, response_data: dict):
        self.response_data = response_data
        self.last_path = None
        self.last_json = None

    def post(self, path: str, json: dict = None):
        self.last_path = path
        self.last_json = json
        return self.response_data


class TestCreateTestAssignment:
    """Tests for create_test_assignment endpoint."""

    def test_create_test_assignment_success(self):
        """Test successful creation of test assignment."""
        mock_response = {
            "assignmentId": "assign-123",
            "lessonId": "lesson-456",
            "resourceId": "resource-789",
        }

        mock_http = MockHttp(mock_response)
        request = TimebackCreateTestAssignmentRequest(
            student="student-123",
            subject=TimebackSubject.MATH,
            grade=TimebackGrade.GRADE_5,
        )
        resp = create_test_assignment(mock_http, request)

        assert isinstance(resp, TimebackCreateTestAssignmentResponse)
        assert resp.assignmentId == "assign-123"
        assert resp.lessonId == "lesson-456"
        assert resp.resourceId == "resource-789"

    def test_create_test_assignment_correct_path_and_body(self):
        """Test correct path and request body."""
        mock_http = MockHttp({
            "assignmentId": "a",
            "lessonId": "l",
            "resourceId": "r",
        })
        request = TimebackCreateTestAssignmentRequest(
            student="student-abc",
            subject=TimebackSubject.READING,
            grade=TimebackGrade.GRADE_3,
            testName="My Custom Test",
        )
        create_test_assignment(mock_http, request)

        assert mock_http.last_path == "/powerpath/test-assignments"
        assert mock_http.last_json["student"] == "student-abc"
        assert mock_http.last_json["subject"] == "Reading"
        assert mock_http.last_json["grade"] == "3"
        assert mock_http.last_json["testName"] == "My Custom Test"

    def test_create_test_assignment_without_test_name(self):
        """Test creation without optional testName."""
        mock_http = MockHttp({
            "assignmentId": "a",
            "lessonId": "l",
            "resourceId": "r",
        })
        request = TimebackCreateTestAssignmentRequest(
            student="student-123",
            subject=TimebackSubject.SCIENCE,
            grade=TimebackGrade.GRAGE_8,  # Note: typo in enum definition
        )
        create_test_assignment(mock_http, request)

        assert "testName" not in mock_http.last_json

