"""API test for make_external_test_assignment endpoint.

This script can be used to test the make_external_test_assignment endpoint
against the live PowerPath API.

Usage:
    python -m tests.api.powerpath.make_external_test_assignment
"""

from timeback import Timeback
from timeback.models.request import TimebackMakeExternalTestAssignmentRequest


def main():
    client = Timeback()

    # Example: Make an external test assignment
    # Replace with actual student and lesson IDs
    request = TimebackMakeExternalTestAssignmentRequest(
        student="<student-sourced-id>",  # Replace with actual student ID
        lesson="<lesson-sourced-id>",  # Replace with actual lesson (ComponentResource) ID
        # applicationName="my-app",  # Optional: for authentication
        # testId="specific-test-id",  # Optional: for MasteryTrack, overrides subject+grade
        # skipCourseEnrollment=True,  # Optional: skip automatic enrollment
    )

    response = client.powerpath.make_external_test_assignment(request)

    print("External test assignment created!")
    print("-" * 60)
    print(f"Tool Provider: {response.toolProvider}")
    print(f"Lesson Type: {response.lessonType}")
    print(f"Attempt: {response.attempt}")

    if response.credentials:
        print(f"\nCredentials for student:")
        print(f"  Email: {response.credentials.email}")
        print(f"  Password: {response.credentials.password}")

    if response.testUrl:
        print(f"\n🔗 Test URL: {response.testUrl}")
    if response.assignmentId:
        print(f"Assignment ID: {response.assignmentId}")
    if response.classId:
        print(f"Class ID: {response.classId}")
    if response.testId:
        print(f"Test ID: {response.testId}")

    print("\nStudent can now take the test using the credentials above.")


if __name__ == "__main__":
    main()

