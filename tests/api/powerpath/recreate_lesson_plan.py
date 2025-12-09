"""API test for recreate_lesson_plan endpoint.

**WARNING**: This will rebuild the lesson plan from scratch.

Usage:
    python -m tests.api.powerpath.recreate_lesson_plan
"""

from timeback import Timeback


def main():
    client = Timeback()

    # Replace with actual lesson plan ID
    lesson_plan_id = "<lesson-plan-id>"

    print("WARNING: This will recreate the lesson plan from scratch!")
    print("-" * 60)
    print(f"Lesson Plan ID: {lesson_plan_id}")
    print("-" * 60)

    # Uncomment to execute
    # response = client.powerpath.recreate_lesson_plan(lesson_plan_id)
    # print(f"Success: {response.success}")
    # print(f"Operations reapplied: {response.operationCount}")

    print("\nTo execute, uncomment the client call above.")


if __name__ == "__main__":
    main()

