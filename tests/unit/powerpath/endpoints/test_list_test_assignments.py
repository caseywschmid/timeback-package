"""Unit tests for list_student_test_assignments and list_all_test_assignments endpoints."""

import pytest

from timeback.services.powerpath.endpoints.list_student_test_assignments import (
    list_student_test_assignments,
)
from timeback.services.powerpath.endpoints.list_all_test_assignments import (
    list_all_test_assignments,
)
from timeback.models.response import TimebackListTestAssignmentsResponse
from timeback.models.timeback_test_assignment import TimebackTestAssignmentStatus
from timeback.enums import TimebackSubject, TimebackGrade


class MockHttp:
    """Mock HTTP client for testing."""

    def __init__(self, response_data: dict):
        self.response_data = response_data
        self.last_path = None
        self.last_params = None

    def get(self, path: str, params: dict = None):
        self.last_path = path
        self.last_params = params
        return self.response_data


class TestListStudentTestAssignments:
    """Tests for list_student_test_assignments endpoint."""

    def test_list_student_assignments_success(self):
        """Test successful list retrieval."""
        mock_response = {
            "testAssignments": [
                {
                    "sourcedId": "assign-1",
                    "studentSourcedId": "student-123",
                    "studentEmail": "test@example.com",
                    "assignedByUserSourcedId": None,
                    "subject": "Math",
                    "grade": "5",
                    "assignmentStatus": "assigned",
                }
            ],
            "totalCount": 1,
            "pageCount": 1,
            "pageNumber": 1,
            "offset": 0,
            "limit": 100,
        }

        mock_http = MockHttp(mock_response)
        resp = list_student_test_assignments(mock_http, "student-123")

        assert isinstance(resp, TimebackListTestAssignmentsResponse)
        assert len(resp.testAssignments) == 1
        assert resp.testAssignments[0].sourcedId == "assign-1"
        assert resp.totalCount == 1

    def test_list_student_assignments_with_filters(self):
        """Test list with optional filters."""
        mock_response = {
            "testAssignments": [],
            "totalCount": 0,
            "pageCount": 0,
            "pageNumber": 1,
            "offset": 0,
            "limit": 50,
        }

        mock_http = MockHttp(mock_response)
        list_student_test_assignments(
            mock_http,
            student="student-123",
            limit=50,
            offset=10,
            status=TimebackTestAssignmentStatus.COMPLETED,
            subject=TimebackSubject.MATH,
            grade=TimebackGrade.GRADE_5,
        )

        assert mock_http.last_path == "/powerpath/test-assignments"
        assert mock_http.last_params["student"] == "student-123"
        assert mock_http.last_params["limit"] == 50
        assert mock_http.last_params["offset"] == 10
        assert mock_http.last_params["status"] == "completed"
        assert mock_http.last_params["subject"] == "Math"
        assert mock_http.last_params["grade"] == "5"


class TestListAllTestAssignments:
    """Tests for list_all_test_assignments endpoint."""

    def test_list_all_assignments_success(self):
        """Test successful admin list retrieval."""
        mock_response = {
            "testAssignments": [
                {
                    "sourcedId": "assign-1",
                    "studentSourcedId": "student-1",
                    "studentEmail": "one@example.com",
                    "assignedByUserSourcedId": "admin-1",
                    "subject": "Math",
                    "grade": "3",
                    "assignmentStatus": "in_progress",
                },
                {
                    "sourcedId": "assign-2",
                    "studentSourcedId": "student-2",
                    "studentEmail": "two@example.com",
                    "assignedByUserSourcedId": None,
                    "subject": "Reading",
                    "grade": "4",
                    "assignmentStatus": "completed",
                },
            ],
            "totalCount": 2,
            "pageCount": 1,
            "pageNumber": 1,
            "offset": 0,
            "limit": 100,
        }

        mock_http = MockHttp(mock_response)
        resp = list_all_test_assignments(mock_http)

        assert isinstance(resp, TimebackListTestAssignmentsResponse)
        assert len(resp.testAssignments) == 2
        assert resp.totalCount == 2

    def test_list_all_assignments_correct_path(self):
        """Test correct admin endpoint path."""
        mock_response = {
            "testAssignments": [],
            "totalCount": 0,
            "pageCount": 0,
            "pageNumber": 1,
            "offset": 0,
            "limit": 100,
        }

        mock_http = MockHttp(mock_response)
        list_all_test_assignments(mock_http)

        assert mock_http.last_path == "/powerpath/test-assignments/admin"

    def test_list_all_assignments_with_student_filter(self):
        """Test admin list with optional student filter."""
        mock_response = {
            "testAssignments": [],
            "totalCount": 0,
            "pageCount": 0,
            "pageNumber": 1,
            "offset": 0,
            "limit": 100,
        }

        mock_http = MockHttp(mock_response)
        list_all_test_assignments(mock_http, student="student-specific")

        assert mock_http.last_params["student"] == "student-specific"

