"""API test for get_operations endpoint.

This script can be used to test the get_operations endpoint
against the live PowerPath API.

Usage:
    python -m tests.api.powerpath.get_operations
"""

from timeback import Timeback


def main():
    client = Timeback()

    # Replace with actual lesson plan ID
    lesson_plan_id = "<lesson-plan-id>"

    print(f"Getting operations for lesson plan: {lesson_plan_id}")
    print("-" * 60)

    response = client.powerpath.get_operations(lesson_plan_id)

    print(f"Total operations: {len(response.operations)}")
    print("-" * 60)

    for op in response.operations:
        print(f"  [{op.sequenceNumber}] {op.type}")
        print(f"      ID: {op.id}")
        print(f"      Created: {op.createdAt}")
        print(f"      By: {op.createdBy or 'N/A'}")
        if op.reason:
            print(f"      Reason: {op.reason}")
        print()


if __name__ == "__main__":
    main()

