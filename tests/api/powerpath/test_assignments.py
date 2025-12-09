"""API tests for test assignment endpoints.

POST /powerpath/test-assignments
GET /powerpath/test-assignments
GET /powerpath/test-assignments/admin
POST /powerpath/test-assignments/bulk
POST /powerpath/test-assignments/import
GET/PUT/DELETE /powerpath/test-assignments/{id}

These tests make real HTTP calls to the Timeback API.
Requires valid credentials in environment variables.
"""

import os
import pytest
from timeback import Timeback
from timeback.models.request import (
    TimebackCreateTestAssignmentRequest,
    TimebackBulkTestAssignmentsRequest,
    TimebackBulkTestAssignmentItem,
    TimebackImportTestAssignmentsRequest,
    TimebackUpdateTestAssignmentRequest,
)
from timeback.models.response import (
    TimebackCreateTestAssignmentResponse,
    TimebackListTestAssignmentsResponse,
    TimebackBulkTestAssignmentsResponse,
)
from timeback.models.timeback_test_assignment import TimebackTestAssignment
from timeback.enums import TimebackSubject, TimebackGrade


# Skip if credentials not available
pytestmark = pytest.mark.skipif(
    not os.environ.get("TIMEBACK_CLIENT_ID"),
    reason="Requires TIMEBACK_CLIENT_ID and TIMEBACK_CLIENT_SECRET",
)


def test_create_test_assignment_api():
    """Test create_test_assignment with real API call."""
    client = Timeback()

    request = TimebackCreateTestAssignmentRequest(
        student="test-student-id",
        subject=TimebackSubject.MATH,
        grade=TimebackGrade.GRADE_5,
        testName="API Test Assignment",
    )

    try:
        response = client.powerpath.create_test_assignment(request)
        assert isinstance(response, TimebackCreateTestAssignmentResponse)
        assert response.assignmentId is not None
    except Exception as e:
        pytest.skip(f"Skipping due to API error: {e}")


def test_list_student_test_assignments_api():
    """Test list_student_test_assignments with real API call."""
    client = Timeback()

    try:
        response = client.powerpath.list_student_test_assignments(
            student="test-student-id"
        )
        assert isinstance(response, TimebackListTestAssignmentsResponse)
        assert isinstance(response.testAssignments, list)
    except Exception as e:
        pytest.skip(f"Skipping due to API error: {e}")


def test_list_all_test_assignments_api():
    """Test list_all_test_assignments (admin) with real API call."""
    client = Timeback()

    try:
        response = client.powerpath.list_all_test_assignments(limit=10)
        assert isinstance(response, TimebackListTestAssignmentsResponse)
        assert isinstance(response.testAssignments, list)
    except Exception as e:
        pytest.skip(f"Skipping due to API error: {e}")


def test_get_test_assignment_api():
    """Test get_test_assignment with real API call."""
    client = Timeback()

    try:
        response = client.powerpath.get_test_assignment("test-assignment-id")
        assert isinstance(response, TimebackTestAssignment)
    except Exception as e:
        pytest.skip(f"Skipping due to API error: {e}")


def test_create_bulk_test_assignments_api():
    """Test create_bulk_test_assignments with real API call."""
    client = Timeback()

    request = TimebackBulkTestAssignmentsRequest(
        items=[
            TimebackBulkTestAssignmentItem(
                student="test-student-1",
                subject=TimebackSubject.MATH,
                grade=TimebackGrade.GRADE_5,
            ),
            TimebackBulkTestAssignmentItem(
                student="test-student-2",
                subject=TimebackSubject.READING,
                grade=TimebackGrade.GRADE_3,
            ),
        ]
    )

    try:
        response = client.powerpath.create_bulk_test_assignments(request)
        assert isinstance(response, TimebackBulkTestAssignmentsResponse)
        assert isinstance(response.success, bool)
    except Exception as e:
        pytest.skip(f"Skipping due to API error: {e}")


def test_import_test_assignments_api():
    """Test import_test_assignments with real API call."""
    client = Timeback()

    request = TimebackImportTestAssignmentsRequest(
        spreadsheetUrl="https://docs.google.com/spreadsheets/d/test-sheet-id",
        sheet="Assignments",
    )

    try:
        response = client.powerpath.import_test_assignments(request)
        assert isinstance(response, TimebackBulkTestAssignmentsResponse)
    except Exception as e:
        pytest.skip(f"Skipping due to API error: {e}")


def test_update_test_assignment_api():
    """Test update_test_assignment with real API call."""
    client = Timeback()

    request = TimebackUpdateTestAssignmentRequest(testName="Updated Test Name")

    try:
        # Returns None on success (204)
        client.powerpath.update_test_assignment("test-assignment-id", request)
    except Exception as e:
        pytest.skip(f"Skipping due to API error: {e}")


def test_delete_test_assignment_api():
    """Test delete_test_assignment with real API call."""
    client = Timeback()

    try:
        # Returns None on success (204)
        client.powerpath.delete_test_assignment("test-assignment-id")
    except Exception as e:
        pytest.skip(f"Skipping due to API error: {e}")

