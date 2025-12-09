"""Unit tests for recreate_lesson_plan endpoint."""

import pytest

from timeback.services.powerpath.endpoints.recreate_lesson_plan import recreate_lesson_plan
from timeback.models.response import TimebackSyncOperationsResponse


class MockHttpClient:
    """Mock HTTP client for testing."""

    def __init__(self, response_data):
        self.response_data = response_data
        self.last_path = None

    def post(self, path, json=None):
        self.last_path = path
        return self.response_data


def test_recreate_lesson_plan_success():
    """Test successful recreation of lesson plan."""
    mock_http = MockHttpClient(
        {
            "success": True,
            "message": "Lesson plan recreated",
            "operationCount": 5,
            "operationResults": [
                {"success": True},
                {"success": True},
                {"success": True},
                {"success": True},
                {"success": True},
            ],
        }
    )

    resp = recreate_lesson_plan(mock_http, "lp-corrupted")

    assert isinstance(resp, TimebackSyncOperationsResponse)
    assert resp.success is True
    assert resp.operationCount == 5
    assert all(r.success for r in resp.operationResults)


def test_recreate_lesson_plan_path():
    """Test that the correct path is used."""
    mock_http = MockHttpClient(
        {"success": True, "operationCount": 0, "operationResults": []}
    )

    recreate_lesson_plan(mock_http, "lp-xyz-123")

    assert mock_http.last_path == "/powerpath/lessonPlans/lp-xyz-123/recreate"


def test_recreate_lesson_plan_no_operations():
    """Test recreation when there are no historical operations."""
    mock_http = MockHttpClient(
        {
            "success": True,
            "message": "Recreated from base course structure",
            "operationCount": 0,
            "operationResults": [],
        }
    )

    resp = recreate_lesson_plan(mock_http, "new-lp")

    assert resp.success is True
    assert resp.operationCount == 0

