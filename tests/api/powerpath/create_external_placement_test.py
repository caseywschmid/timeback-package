"""API test for create_external_placement_test endpoint.

This script can be used to test the create_external_placement_test endpoint
against the live PowerPath API.

Usage:
    python -m tests.api.powerpath.create_external_placement_test
"""

from timeback import Timeback
from timeback.models.request import TimebackCreateExternalPlacementTestRequest


def main():
    client = Timeback()

    # Example: Create an external placement test for a course
    # Replace with actual course ID
    request = TimebackCreateExternalPlacementTestRequest(
        courseId="<course-sourced-id>",  # Replace with actual course ID
        toolProvider="edulastic",
        grades=["5", "6"],
        lessonTitle="Grade 5-6 Placement Test",
        launchUrl="https://edulastic.com/test/example",
        unitTitle="Placement Tests",
        # Optional: courseIdOnFail="<fallback-course-id>",  # Course to enroll if score < 90%
    )

    response = client.powerpath.create_external_placement_test(request)

    print("External placement test created successfully!")
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
    if response.courseIdOnFail:
        print(f"Course on Fail: {response.courseIdOnFail}")
    if response.grades:
        print(f"Grades: {response.grades}")


if __name__ == "__main__":
    main()

