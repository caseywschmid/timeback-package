"""API test for create_external_test_out endpoint.

**DEPRECATED**: This endpoint is deprecated. Use start_test_out instead.

This script can be used to test the create_external_test_out endpoint
against the live PowerPath API.

Usage:
    python -m tests.api.powerpath.create_external_test_out
"""

import warnings
from timeback import Timeback
from timeback.models.request import TimebackCreateExternalTestOutRequest


def main():
    client = Timeback()

    # Example: Create an external test-out for a course
    # Replace with actual course ID
    request = TimebackCreateExternalTestOutRequest(
        courseId="<course-sourced-id>",  # Replace with actual course ID
        toolProvider="edulastic",
        grades=["5", "6"],
        xp=100,  # Required for test-out
        lessonTitle="Grade 5-6 Test-Out",
        launchUrl="https://edulastic.com/test/example",
        unitTitle="Test-Out Assessments",
    )

    # Note: This will emit a DeprecationWarning
    with warnings.catch_warnings():
        warnings.simplefilter("always", DeprecationWarning)
        response = client.powerpath.create_external_test_out(request)

    print("External test-out created successfully!")
    print("-" * 60)
    print("WARNING: This endpoint is deprecated. Use start_test_out() instead.")
    print("-" * 60)
    print(f"Lesson Type: {response.lessonType}")
    print(f"Lesson ID (ComponentResource): {response.lessonId}")
    print(f"Course Component ID: {response.courseComponentId}")
    print(f"Resource ID: {response.resourceId}")
    print(f"Tool Provider: {response.toolProvider}")
    if response.launchUrl:
        print(f"Launch URL: {response.launchUrl}")
    if response.vendorId:
        print(f"Vendor ID: {response.vendorId}")
    if response.grades:
        print(f"Grades: {response.grades}")


if __name__ == "__main__":
    main()

