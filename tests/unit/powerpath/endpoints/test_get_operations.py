"""Unit tests for get_operations endpoint."""

import pytest

from timeback.services.powerpath.endpoints.get_operations import get_operations
from timeback.models.response import TimebackGetOperationsResponse


class MockHttpClient:
    """Mock HTTP client for testing."""

    def __init__(self, response_data):
        self.response_data = response_data
        self.last_path = None

    def get(self, path, params=None):
        self.last_path = path
        return self.response_data


def test_get_operations_success():
    """Test successful retrieval of operations."""
    mock_http = MockHttpClient(
        {
            "operations": [
                {
                    "id": "op-1",
                    "type": "set-skipped",
                    "payload": {"target": {"type": "component", "id": "c1"}, "value": True},
                    "reason": "Skip this unit",
                    "createdAt": "2024-01-15T10:30:00Z",
                    "sequenceNumber": 1,
                    "createdBy": "user-123",
                },
                {
                    "id": "op-2",
                    "type": "move-item-before",
                    "payload": {"target": {"type": "resource", "id": "r1"}, "reference_id": "r2"},
                    "reason": None,
                    "createdAt": "2024-01-15T11:00:00Z",
                    "sequenceNumber": 2,
                    "createdBy": None,
                },
            ]
        }
    )

    resp = get_operations(mock_http, "lp-123")

    assert isinstance(resp, TimebackGetOperationsResponse)
    assert len(resp.operations) == 2
    assert resp.operations[0].id == "op-1"
    assert resp.operations[0].type == "set-skipped"
    assert resp.operations[0].reason == "Skip this unit"
    assert resp.operations[1].createdBy is None


def test_get_operations_path():
    """Test that the correct path is used."""
    mock_http = MockHttpClient({"operations": []})

    resp = get_operations(mock_http, "lesson-plan-abc")

    assert mock_http.last_path == "/powerpath/lessonPlans/lesson-plan-abc/operations"


def test_get_operations_empty():
    """Test when there are no operations."""
    mock_http = MockHttpClient({"operations": []})

    resp = get_operations(mock_http, "empty-lp")

    assert isinstance(resp, TimebackGetOperationsResponse)
    assert len(resp.operations) == 0


def test_get_operations_with_payload():
    """Test operations include payload data."""
    mock_http = MockHttpClient(
        {
            "operations": [
                {
                    "id": "op-payload",
                    "type": "add-custom-resource",
                    "payload": {
                        "resource_id": "custom-1",
                        "parent_component_id": "unit-1",
                        "skipped": False,
                    },
                    "reason": "Add extra resource",
                    "createdAt": "2024-02-01T09:00:00Z",
                    "sequenceNumber": 5,
                    "createdBy": "teacher-456",
                },
            ]
        }
    )

    resp = get_operations(mock_http, "lp-with-payload")

    assert resp.operations[0].payload["resource_id"] == "custom-1"
    assert resp.operations[0].payload["parent_component_id"] == "unit-1"

