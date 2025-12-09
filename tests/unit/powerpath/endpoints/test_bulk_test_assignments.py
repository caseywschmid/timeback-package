"""Unit tests for create_bulk_test_assignments and import_test_assignments endpoints."""

import pytest

from timeback.services.powerpath.endpoints.create_bulk_test_assignments import (
    create_bulk_test_assignments,
)
from timeback.services.powerpath.endpoints.import_test_assignments import (
    import_test_assignments,
)
from timeback.models.request import (
    TimebackBulkTestAssignmentsRequest,
    TimebackBulkTestAssignmentItem,
    TimebackImportTestAssignmentsRequest,
)
from timeback.models.response import TimebackBulkTestAssignmentsResponse
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


class TestCreateBulkTestAssignments:
    """Tests for create_bulk_test_assignments endpoint."""

    def test_bulk_create_success(self):
        """Test successful bulk creation."""
        mock_response = {
            "success": True,
            "results": [
                {"assignmentId": "a1", "lessonId": "l1", "resourceId": "r1"},
                {"assignmentId": "a2", "lessonId": "l2", "resourceId": "r2"},
            ],
            "errors": [],
        }

        mock_http = MockHttp(mock_response)
        request = TimebackBulkTestAssignmentsRequest(
            items=[
                TimebackBulkTestAssignmentItem(
                    student="student-1",
                    subject=TimebackSubject.MATH,
                    grade=TimebackGrade.GRADE_5,
                ),
                TimebackBulkTestAssignmentItem(
                    student="student-2",
                    subject=TimebackSubject.READING,
                    grade=TimebackGrade.GRADE_3,
                ),
            ]
        )
        resp = create_bulk_test_assignments(mock_http, request)

        assert isinstance(resp, TimebackBulkTestAssignmentsResponse)
        assert resp.success is True
        assert len(resp.results) == 2
        assert len(resp.errors) == 0

    def test_bulk_create_with_errors(self):
        """Test bulk creation with validation errors."""
        mock_response = {
            "success": False,
            "results": [],
            "errors": [
                {"row": 0, "message": "Student not found"},
                {"row": 1, "message": "Invalid grade"},
            ],
        }

        mock_http = MockHttp(mock_response)
        request = TimebackBulkTestAssignmentsRequest(
            items=[
                TimebackBulkTestAssignmentItem(
                    student="invalid-student",
                    subject=TimebackSubject.MATH,
                    grade=TimebackGrade.GRADE_5,
                ),
            ]
        )
        resp = create_bulk_test_assignments(mock_http, request)

        assert resp.success is False
        assert len(resp.errors) == 2
        assert resp.errors[0].row == 0
        assert resp.errors[0].message == "Student not found"

    def test_bulk_create_correct_path(self):
        """Test correct endpoint path."""
        mock_http = MockHttp({"success": True, "results": [], "errors": []})
        request = TimebackBulkTestAssignmentsRequest(
            items=[
                TimebackBulkTestAssignmentItem(
                    student="s1",
                    subject=TimebackSubject.MATH,
                    grade=TimebackGrade.GRADE_5,
                ),
            ]
        )
        create_bulk_test_assignments(mock_http, request)

        assert mock_http.last_path == "/powerpath/test-assignments/bulk"


class TestImportTestAssignments:
    """Tests for import_test_assignments endpoint."""

    def test_import_success(self):
        """Test successful import from Google Sheets."""
        mock_response = {
            "success": True,
            "results": [
                {"assignmentId": "a1", "lessonId": "l1", "resourceId": "r1"},
            ],
            "errors": [],
        }

        mock_http = MockHttp(mock_response)
        request = TimebackImportTestAssignmentsRequest(
            spreadsheetUrl="https://docs.google.com/spreadsheets/d/abc123",
            sheet="Test Assignments",
        )
        resp = import_test_assignments(mock_http, request)

        assert isinstance(resp, TimebackBulkTestAssignmentsResponse)
        assert resp.success is True
        assert len(resp.results) == 1

    def test_import_correct_path_and_body(self):
        """Test correct endpoint path and body."""
        mock_http = MockHttp({"success": True, "results": [], "errors": []})
        request = TimebackImportTestAssignmentsRequest(
            spreadsheetUrl="https://docs.google.com/spreadsheets/d/xyz789",
            sheet="Sheet1",
        )
        import_test_assignments(mock_http, request)

        assert mock_http.last_path == "/powerpath/test-assignments/import"
        assert mock_http.last_json["spreadsheetUrl"] == "https://docs.google.com/spreadsheets/d/xyz789"
        assert mock_http.last_json["sheet"] == "Sheet1"

