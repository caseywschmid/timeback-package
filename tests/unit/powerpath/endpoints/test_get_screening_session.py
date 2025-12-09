"""Unit tests for get_screening_session endpoint."""

import pytest

from timeback.services.powerpath.endpoints.get_screening_session import get_screening_session
from timeback.models import TimebackScreeningSession


class MockHttpClient:
    """Mock HTTP client for testing."""

    def __init__(self, response_data):
        self.response_data = response_data
        self.last_path = None
        self.last_params = None

    def get(self, path, params=None):
        self.last_path = path
        self.last_params = params
        return self.response_data


def test_get_screening_session_success():
    """Test successful retrieval of screening session."""
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

    resp = get_screening_session(mock_http, "student-123")

    assert isinstance(resp, TimebackScreeningSession)
    assert resp.nweaStudentId == "550e8400-e29b-41d4-a716-446655440000"
    assert resp.password == "test-password-123"
    assert resp.name == "John Doe"
    assert resp.status == "active"
    assert resp.assignment.assignedTestKey == "reading-screening-v1"
    assert resp.assignment.status == "assigned"
    assert resp.assignment.nweaStatus == "AWAITING_STUDENT"


def test_get_screening_session_path():
    """Test that the correct path is called."""
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
                "assignedTestKey": None,
                "status": None,
                "nweaStatus": None,
            },
            "termId": "term-1",
        }
    )

    resp = get_screening_session(mock_http, "user-456")

    assert mock_http.last_path == "/powerpath/screening/session/user-456"


def test_get_screening_session_with_null_assignment():
    """Test handling of null assignment fields."""
    mock_http = MockHttpClient(
        {
            "nweaStudentId": "uuid-123",
            "createdOn": "2024-01-10T09:00:00Z",
            "password": "secret",
            "name": "Jane Smith",
            "proctorId": "proctor-uuid",
            "pin": "5678",
            "testSessionId": "session-uuid",
            "status": "inactive",
            "assignment": {
                "assignedTestKey": None,
                "status": None,
                "nweaStatus": None,
            },
            "termId": "term-2024-fall",
        }
    )

    resp = get_screening_session(mock_http, "student-789")

    assert isinstance(resp, TimebackScreeningSession)
    assert resp.status == "inactive"
    assert resp.assignment.assignedTestKey is None
    assert resp.assignment.status is None
    assert resp.assignment.nweaStatus is None


def test_get_screening_session_in_progress():
    """Test session with test in progress."""
    mock_http = MockHttpClient(
        {
            "nweaStudentId": "student-nwea-id",
            "createdOn": "2024-01-20T14:00:00Z",
            "password": "in-progress-pass",
            "name": "Active Student",
            "proctorId": "proctor-id",
            "pin": "9999",
            "testSessionId": "active-session-id",
            "status": "active",
            "assignment": {
                "assignedTestKey": "math-screening-v2",
                "status": "in_progress",
                "nweaStatus": "IN_PROGRESS",
            },
            "termId": "term-2024-spring",
        }
    )

    resp = get_screening_session(mock_http, "active-student")

    assert isinstance(resp, TimebackScreeningSession)
    assert resp.assignment.status == "in_progress"
    assert resp.assignment.nweaStatus == "IN_PROGRESS"

