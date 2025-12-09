"""API test for get_lesson_plan endpoint.

Usage:
    python -m tests.api.powerpath.get_lesson_plan
"""

from timeback import Timeback


def main():
    client = Timeback()

    # Replace with actual lesson plan ID
    lesson_plan_id = "<lesson-plan-id>"

    print(f"Getting lesson plan: {lesson_plan_id}")
    print("-" * 60)

    lesson_plan = client.powerpath.get_lesson_plan(lesson_plan_id)

    print(f"Course: {lesson_plan.course.title}")
    print(f"Course ID: {lesson_plan.course.sourcedId}")
    print(f"Components: {len(lesson_plan.subComponents)}")


if __name__ == "__main__":
    main()

