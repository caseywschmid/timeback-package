"""API test for delete_lesson_plans_by_course_id endpoint.

This script can be used to test the delete_lesson_plans_by_course_id endpoint
against the live PowerPath API.

**WARNING**: This is a destructive operation and cannot be undone.

Usage:
    python -m tests.api.powerpath.delete_lesson_plans_by_course_id
"""

from timeback import Timeback


def main():
    client = Timeback()

    # Replace with actual course ID
    course_id = "<course-sourced-id>"

    print("WARNING: This will delete ALL lesson plans for the course!")
    print("-" * 60)
    print(f"Course ID: {course_id}")
    print("-" * 60)

    # Uncomment to execute (be careful!)
    # client.powerpath.delete_lesson_plans_by_course_id(course_id)
    # print("All lesson plans deleted (204 No Content)")

    print("\nTo execute, uncomment the client call above.")


if __name__ == "__main__":
    main()

