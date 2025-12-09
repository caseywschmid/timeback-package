"""API test for get_test_out endpoint.

**DEPRECATED**: This endpoint is deprecated. Use get_course_progress instead.

This script can be used to test the get_test_out endpoint
against the live PowerPath API.

Usage:
    python -m tests.api.powerpath.get_test_out
"""

import warnings
from timeback import Timeback
from timeback.models.request import TimebackGetTestOutRequest


def main():
    client = Timeback()

    # Example: Get test-out information for a student and course
    # Replace with actual student and course IDs
    request = TimebackGetTestOutRequest(
        student="<student-sourced-id>",  # Replace with actual student ID
        course="<course-sourced-id>",  # Replace with actual course ID
    )

    # Note: This will emit a DeprecationWarning
    with warnings.catch_warnings():
        warnings.simplefilter("always", DeprecationWarning)
        response = client.powerpath.get_test_out(request)

    print("Test-out information retrieved!")
    print("-" * 60)
    print("WARNING: This endpoint is deprecated. Use get_course_progress() instead.")
    print("-" * 60)
    print(f"Lesson Type: {response.lessonType}")
    print(f"Lesson ID: {response.lessonId}")
    print(f"Finalized: {response.finalized}")
    print(f"Tool Provider: {response.toolProvider}")

    if response.attempt is not None:
        print(f"Attempt: {response.attempt}")

    if response.credentials:
        print(f"\nCredentials:")
        print(f"  Email: {response.credentials.email}")
        print(f"  Password: {response.credentials.password}")

    if response.testUrl:
        print(f"\nTest URL: {response.testUrl}")

    if response.lessonId is None:
        print("\n⚠️ No test-out lesson found in this course.")
    elif response.finalized:
        print("\n✓ Test-out has been completed.")
    else:
        print("\n⏳ Test-out available but not yet completed.")


if __name__ == "__main__":
    main()

