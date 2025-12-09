"""API test for store_operation endpoint.

This script can be used to test the store_operation endpoint
against the live PowerPath API.

Usage:
    python -m tests.api.powerpath.store_operation
"""

from timeback import Timeback
from timeback.models.request import TimebackStoreOperationRequest


def main():
    client = Timeback()

    # Replace with actual lesson plan ID
    request = TimebackStoreOperationRequest(
        lesson_plan_id="<lesson-plan-id>",
        operation={
            "type": "set-skipped",
            "payload": {
                "target": {"type": "component", "id": "<component-id>"},
                "value": True,
            },
        },
        reason="Testing set-skipped operation",
    )

    print(f"Storing operation on lesson plan: {request.lesson_plan_id}")
    print(f"Operation type: {request.operation['type']}")
    print("-" * 60)

    response = client.powerpath.store_operation(request)

    print(f"Success: {response.success}")
    print(f"Message: {response.message}")
    print(f"Operation ID: {response.operationId}")


if __name__ == "__main__":
    main()

