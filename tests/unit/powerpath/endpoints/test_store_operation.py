"""Unit tests for store_operation endpoint."""

import pytest

from timeback.services.powerpath.endpoints.store_operation import store_operation
from timeback.models.response import TimebackStoreOperationResponse
from timeback.models.request import TimebackStoreOperationRequest


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


def test_store_operation_set_skipped_success():
    """Test successful store of set-skipped operation."""
    mock_http = MockHttpClient(
        {
            "success": True,
            "message": "Operation stored",
            "operationId": "op-123",
        }
    )

    request = TimebackStoreOperationRequest(
        lesson_plan_id="lp-abc",
        operation={
            "type": "set-skipped",
            "payload": {
                "target": {"type": "component", "id": "comp-123"},
                "value": True,
            },
        },
        reason="Hide this unit for now",
    )
    resp = store_operation(mock_http, request)

    assert isinstance(resp, TimebackStoreOperationResponse)
    assert resp.success is True
    assert resp.operationId == "op-123"


def test_store_operation_path_and_body():
    """Test that the correct path and body are sent."""
    mock_http = MockHttpClient({"success": True})

    request = TimebackStoreOperationRequest(
        lesson_plan_id="lesson-plan-456",
        operation={
            "type": "move-item-before",
            "payload": {
                "target": {"type": "resource", "id": "res-1"},
                "reference_id": "res-2",
            },
        },
    )
    resp = store_operation(mock_http, request)

    assert mock_http.last_path == "/powerpath/lessonPlans/lesson-plan-456/operations"
    assert mock_http.last_json["operation"]["type"] == "move-item-before"
    assert "reason" not in mock_http.last_json


def test_store_operation_with_reason():
    """Test operation with reason included."""
    mock_http = MockHttpClient({"success": True, "operationId": "op-456"})

    request = TimebackStoreOperationRequest(
        lesson_plan_id="lp-xyz",
        operation={
            "type": "add-custom-resource",
            "payload": {
                "resource_id": "custom-res-1",
                "parent_component_id": "unit-1",
            },
        },
        reason="Student requested additional practice",
    )
    resp = store_operation(mock_http, request)

    assert mock_http.last_json["reason"] == "Student requested additional practice"
    assert resp.success is True


def test_store_operation_change_item_parent():
    """Test change-item-parent operation."""
    mock_http = MockHttpClient({"success": True})

    request = TimebackStoreOperationRequest(
        lesson_plan_id="lp-parent-test",
        operation={
            "type": "change-item-parent",
            "payload": {
                "target": {"type": "resource", "id": "res-abc"},
                "new_parent_id": "unit-2",
                "position": "start",
            },
        },
    )
    resp = store_operation(mock_http, request)

    assert resp.success is True
    assert mock_http.last_json["operation"]["type"] == "change-item-parent"

