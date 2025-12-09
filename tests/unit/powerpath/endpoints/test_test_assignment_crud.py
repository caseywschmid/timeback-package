"""Unit tests for get, update, and delete test assignment endpoints."""

import pytest

from timeback.services.powerpath.endpoints.get_test_assignment import (
    get_test_assignment,
)
from timeback.services.powerpath.endpoints.update_test_assignment import (
    update_test_assignment,
)
from timeback.services.powerpath.endpoints.delete_test_assignment import (
    delete_test_assignment,
)
from timeback.models.request import TimebackUpdateTestAssignmentRequest
from timeback.models.timeback_test_assignment import TimebackTestAssignment


class MockHttp:
    """Mock HTTP client for testing."""

    def __init__(self, response_data: dict = None):
        self.response_data = response_data
        self.last_path = None
        self.last_json = None

    def get(self, path: str, params: dict = None):
        self.last_path = path
        return self.response_data

    def put(self, path: str, json: dict = None):
        self.last_path = path
        self.last_json = json
        return self.response_data

    def delete(self, path: str):
        self.last_path = path
        return None


class TestGetTestAssignment:
    """Tests for get_test_assignment endpoint."""

    def test_get_assignment_success(self):
        """Test successful retrieval of single assignment."""
        mock_response = {
            "sourcedId": "assign-123",
            "studentSourcedId": "student-456",
            "studentEmail": "student@example.com",
            "assignedByUserSourcedId": "teacher-789",
            "subject": "Math",
            "grade": "5",
            "assignmentStatus": "in_progress",
            "testName": "Unit Test",
            "assignedAt": "2024-01-15T10:00:00Z",
            "expiresAt": "2024-02-15T10:00:00Z",
            "completedAt": None,
            "resourceSourcedId": "resource-111",
            "componentResourceSourcedId": "cr-222",
        }

        mock_http = MockHttp(mock_response)
        resp = get_test_assignment(mock_http, "assign-123")

        assert isinstance(resp, TimebackTestAssignment)
        assert resp.sourcedId == "assign-123"
        assert resp.studentEmail == "student@example.com"
        assert resp.subject == "Math"
        assert resp.assignmentStatus == "in_progress"

    def test_get_assignment_correct_path(self):
        """Test correct path with ID."""
        mock_response = {
            "sourcedId": "a",
            "studentSourcedId": "s",
            "studentEmail": "e@e.com",
            "assignedByUserSourcedId": None,
            "subject": "Math",
            "grade": "3",
            "assignmentStatus": "assigned",
        }

        mock_http = MockHttp(mock_response)
        get_test_assignment(mock_http, "my-assignment-id")

        assert mock_http.last_path == "/powerpath/test-assignments/my-assignment-id"


class TestUpdateTestAssignment:
    """Tests for update_test_assignment endpoint."""

    def test_update_assignment_success(self):
        """Test successful update (204 response)."""
        mock_http = MockHttp(None)  # 204 returns nothing
        request = TimebackUpdateTestAssignmentRequest(testName="New Test Name")

        # Should not raise
        result = update_test_assignment(mock_http, "assign-123", request)
        assert result is None

    def test_update_assignment_correct_path_and_body(self):
        """Test correct path and body."""
        mock_http = MockHttp(None)
        request = TimebackUpdateTestAssignmentRequest(testName="Updated Name")
        update_test_assignment(mock_http, "assign-abc", request)

        assert mock_http.last_path == "/powerpath/test-assignments/assign-abc"
        assert mock_http.last_json == {"testName": "Updated Name"}


class TestDeleteTestAssignment:
    """Tests for delete_test_assignment endpoint."""

    def test_delete_assignment_success(self):
        """Test successful deletion (204 response)."""
        mock_http = MockHttp(None)

        # Should not raise
        result = delete_test_assignment(mock_http, "assign-to-delete")
        assert result is None

    def test_delete_assignment_correct_path(self):
        """Test correct path."""
        mock_http = MockHttp(None)
        delete_test_assignment(mock_http, "my-assignment-id")

        assert mock_http.last_path == "/powerpath/test-assignments/my-assignment-id"

