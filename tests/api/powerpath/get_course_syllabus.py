"""API test for get_course_syllabus endpoint.

Usage:
    python -m tests.api.powerpath.get_course_syllabus
"""

from timeback import Timeback


def main():
    client = Timeback()

    # Replace with actual course ID
    course_id = "<course-sourced-id>"

    print(f"Getting syllabus for course: {course_id}")
    print("-" * 60)

    response = client.powerpath.get_course_syllabus(course_id)

    print(f"Syllabus: {response.syllabus}")


if __name__ == "__main__":
    main()

