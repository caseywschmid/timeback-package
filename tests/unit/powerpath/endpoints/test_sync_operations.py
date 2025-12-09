"""Unit tests for sync_operations endpoint."""

import pytest

from timeback.services.powerpath.endpoints.sync_operations import sync_operations
from timeback.models.response import TimebackSyncOperationsResponse


class MockHttpClient:
    """Mock HTTP client for testing."""

    def __init__(self, response_data):
        self.response_data = response_data
        self.last_path = None

    def post(self, path, json=None):
        self.last_path = path
        return self.response_data


def test_sync_operations_success():
    """Test successful sync of operations."""
    mock_http = MockHttpClient(
        {
            "success": True,
            "message": "Operations synced",
            "operationCount": 3,
            "operationResults": [
                {"success": True},
                {"success": True},
                {"success": True},
            ],
        }
    )

    resp = sync_operations(mock_http, "lp-123")

    assert isinstance(resp, TimebackSyncOperationsResponse)
    assert resp.success is True
    assert resp.operationCount == 3
    assert len(resp.operationResults) == 3


def test_sync_operations_path():
    """Test that the correct path is used."""
    mock_http = MockHttpClient(
        {"success": True, "operationCount": 0, "operationResults": []}
    )

    sync_operations(mock_http, "lesson-plan-abc")

    assert mock_http.last_path == "/powerpath/lessonPlans/lesson-plan-abc/operations/sync"


def test_sync_operations_with_errors():
    """Test sync with some operation failures."""
    mock_http = MockHttpClient(
        {
            "success": False,
            "operationCount": 2,
            "operationResults": [
                {"success": True},
                {"success": False, "errors": [{"message": "Target not found"}]},
            ],
        }
    )

    resp = sync_operations(mock_http, "lp-with-errors")

    assert resp.success is False
    assert resp.operationResults[1].success is False
    assert resp.operationResults[1].errors[0].message == "Target not found"


def test_sync_operations_no_pending():
    """Test when there are no pending operations."""
    mock_http = MockHttpClient(
        {
            "success": True,
            "message": "No pending operations",
            "operationCount": 0,
            "operationResults": [],
        }
    )

    resp = sync_operations(mock_http, "lp-no-pending")

    assert resp.success is True
    assert resp.operationCount == 0
    assert len(resp.operationResults) == 0

