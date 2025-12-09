"""API test for start_test_out endpoint.

This script can be used to test the start_test_out endpoint
against the live PowerPath API.

Usage:
    python -m tests.api.powerpath.start_test_out
"""

from timeback import Timeback
from timeback.models.request import TimebackStartTestOutRequest


def main():
    client = Timeback()

    # Replace with actual IDs
    request = TimebackStartTestOutRequest(
        course_id="<course-sourced-id>",
        student_id="<student-sourced-id>",
    )

    print(f"Starting test-out assignment...")
    print(f"Course: {request.course_id}")
    print(f"Student: {request.student_id}")
    print("-" * 60)

    response = client.powerpath.start_test_out(request)

    print(f"Status: {response.status}")
    print(f"Assignment ID: {response.assignmentId}")
    print(f"Lesson ID: {response.lessonId}")
    print(f"Resource ID: {response.resourceId}")


if __name__ == "__main__":
    main()

