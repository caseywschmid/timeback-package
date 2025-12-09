"""API test for get_tree endpoint.

This script can be used to test the get_tree endpoint
against the live PowerPath API.

Usage:
    python -m tests.api.powerpath.get_tree
"""

from timeback import Timeback
from timeback.models.request import TimebackGetTreeRequest


def main():
    client = Timeback()

    # Replace with actual IDs
    request = TimebackGetTreeRequest(
        course_id="<course-sourced-id>",
        user_id="<student-sourced-id>",
    )

    print(f"Getting lesson plan tree...")
    print(f"Course: {request.course_id}")
    print(f"Student: {request.user_id}")
    print("-" * 60)

    lesson_plan = client.powerpath.get_tree(request)

    print(f"Course: {lesson_plan.course.get('title', 'N/A')}")
    print(f"Components: {len(lesson_plan.subComponents)}")
    print("-" * 60)

    for component in lesson_plan.subComponents:
        print(f"  - {component.title} ({component.sourcedId})")
        for sub in component.subComponents or []:
            print(f"    - {sub.title}")


if __name__ == "__main__":
    main()

