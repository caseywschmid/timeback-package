"""Unit tests for assign_screening_test endpoint."""

import pytest

from timeback.services.powerpath.endpoints.assign_screening_test import assign_screening_test
from timeback.models import TimebackScreeningSession
from timeback.models.request import TimebackAssignScreeningTestRequest


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


def test_assign_screening_test_success():
    """Test successful assignment of screening test."""
    mock_http = MockHttpClient(
        {
            "nweaStudentId": "550e8400-e29b-41d4-a716-446655440000",
            "createdOn": "2024-01-15T10:30:00Z",
            "password": "test-password-123",
            "name": "John Doe",
            "proctorId": "660e8400-e29b-41d4-a716-446655440001",
            "pin": "1234",
            "testSessionId": "770e8400-e29b-41d4-a716-446655440002",
            "status": "active",
            "assignment": {
                "assignedTestKey": "reading-screening-v1",
                "status": "assigned",
                "nweaStatus": "AWAITING_STUDENT",
            },
            "termId": "term-2024-spring",
        }
    )

    request = TimebackAssignScreeningTestRequest(
        userId="student-123",
        subject="Reading",
    )
    resp = assign_screening_test(mock_http, request)

    assert isinstance(resp, TimebackScreeningSession)
    assert resp.nweaStudentId == "550e8400-e29b-41d4-a716-446655440000"
    assert resp.assignment.assignedTestKey == "reading-screening-v1"
    assert resp.assignment.status == "assigned"


def test_assign_screening_test_path_and_body():
    """Test that the correct path and body are sent."""
    mock_http = MockHttpClient(
        {
            "nweaStudentId": "uuid",
            "createdOn": "2024-01-15T10:30:00Z",
            "password": "pass",
            "name": "Test",
            "proctorId": "uuid",
            "pin": "0000",
            "testSessionId": "uuid",
            "status": "active",
            "assignment": {
                "assignedTestKey": "math-screening",
                "status": "assigned",
                "nweaStatus": "AWAITING_STUDENT",
            },
            "termId": "term-1",
        }
    )

    request = TimebackAssignScreeningTestRequest(
        userId="user-456",
        subject="Math",
    )
    resp = assign_screening_test(mock_http, request)

    assert mock_http.last_path == "/powerpath/screening/tests/assign"
    assert mock_http.last_json == {
        "userId": "user-456",
        "subject": "Math",
    }


def test_assign_screening_test_all_subjects():
    """Test assignment works for all valid subjects."""
    base_response = {
        "nweaStudentId": "uuid",
        "createdOn": "2024-01-15T10:30:00Z",
        "password": "pass",
        "name": "Test",
        "proctorId": "uuid",
        "pin": "0000",
        "testSessionId": "uuid",
        "status": "active",
        "assignment": {
            "assignedTestKey": "test-key",
            "status": "assigned",
            "nweaStatus": "AWAITING_STUDENT",
        },
        "termId": "term-1",
    }

    for subject in ["Math", "Reading", "Language", "Science"]:
        mock_http = MockHttpClient(base_response)
        request = TimebackAssignScreeningTestRequest(
            userId="student-123",
            subject=subject,
        )
        resp = assign_screening_test(mock_http, request)

        assert isinstance(resp, TimebackScreeningSession)
        assert mock_http.last_json["subject"] == subject


def test_assign_screening_test_enqueued():
    """Test when assignment is enqueued."""
    mock_http = MockHttpClient(
        {
            "nweaStudentId": "student-nwea-id",
            "createdOn": "2024-01-20T14:00:00Z",
            "password": "new-pass",
            "name": "New Student",
            "proctorId": "proctor-id",
            "pin": "9999",
            "testSessionId": "session-id",
            "status": "active",
            "assignment": {
                "assignedTestKey": "language-screening",
                "status": "enqueued",
                "nweaStatus": "ENQUEUED",
            },
            "termId": "term-2024-spring",
        }
    )

    request = TimebackAssignScreeningTestRequest(
        userId="new-student",
        subject="Language",
    )
    resp = assign_screening_test(mock_http, request)

    assert isinstance(resp, TimebackScreeningSession)
    assert resp.assignment.status == "enqueued"
    assert resp.assignment.nweaStatus == "ENQUEUED"

