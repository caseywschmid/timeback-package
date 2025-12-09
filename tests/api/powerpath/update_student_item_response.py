"""API test for update_student_item_response endpoint.

Usage:
    python -m tests.api.powerpath.update_student_item_response
"""

from timeback import Timeback
from timeback.models.request import (
    TimebackUpdateStudentItemResponseRequest,
    TimebackStudentItemResult,
)


def main():
    client = Timeback()

    # Replace with actual IDs
    result = TimebackStudentItemResult(
        status="active",
        scoreDate="2024-01-15T10:00:00Z",
        scoreStatus="fully graded",
        score=85.0,
        comment="Good work!",
    )
    request = TimebackUpdateStudentItemResponseRequest(
        student_id="<student-sourced-id>",
        component_resource_id="<component-resource-id>",
        result=result,
    )

    print(f"Updating student item response")
    print(f"Student: {request.student_id}")
    print(f"Resource: {request.component_resource_id}")
    print("-" * 60)

    # Uncomment to execute
    # response = client.powerpath.update_student_item_response(request)
    # print(f"Line Item: {response.componentResourceLineItem}")
    # print(f"Result: {response.componentResourceResult}")

    print("\nTo execute, uncomment the client call above.")


if __name__ == "__main__":
    main()

