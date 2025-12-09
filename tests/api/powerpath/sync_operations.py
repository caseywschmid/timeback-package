"""API test for sync_operations endpoint.

Usage:
    python -m tests.api.powerpath.sync_operations
"""

from timeback import Timeback


def main():
    client = Timeback()

    # Replace with actual lesson plan ID
    lesson_plan_id = "<lesson-plan-id>"

    print(f"Syncing operations for lesson plan: {lesson_plan_id}")
    print("-" * 60)

    response = client.powerpath.sync_operations(lesson_plan_id)

    print(f"Success: {response.success}")
    print(f"Message: {response.message or 'N/A'}")
    print(f"Operations processed: {response.operationCount}")
    print("-" * 60)

    for i, result in enumerate(response.operationResults):
        status = "✓" if result.success else "✗"
        print(f"  {status} Operation {i + 1}: {'Success' if result.success else 'Failed'}")
        if result.errors:
            for err in result.errors:
                print(f"      Error: {err.message}")


if __name__ == "__main__":
    main()

