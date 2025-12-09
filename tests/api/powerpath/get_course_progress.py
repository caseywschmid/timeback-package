"""API test for get_course_progress endpoint.

Usage:
    python -m tests.api.powerpath.get_course_progress
"""

from timeback import Timeback


def main():
    client = Timeback()

    # Replace with actual IDs
    course_id = "<course-sourced-id>"
    student_id = "<student-sourced-id>"

    print(f"Getting progress for student {student_id} in course {course_id}")
    print("-" * 60)

    response = client.powerpath.get_course_progress(course_id, student_id)

    print(f"Line items: {len(response.lineItems)}")
    print(f"Test-out status: {response.testOut.get('status')}")
    print("-" * 60)

    for item in response.lineItems[:5]:  # Show first 5
        print(f"  [{item.get('type')}] {item.get('title')}")
        print(f"    Results: {len(item.get('results', []))}")


if __name__ == "__main__":
    main()

