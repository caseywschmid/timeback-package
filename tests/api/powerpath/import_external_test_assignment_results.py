"""API test for import_external_test_assignment_results endpoint.

This script can be used to test the import_external_test_assignment_results endpoint
against the live PowerPath API.

Usage:
    python -m tests.api.powerpath.import_external_test_assignment_results
"""

from timeback import Timeback
from timeback.models.request import TimebackImportExternalTestAssignmentResultsRequest


def main():
    client = Timeback()

    # Example: Import results for a test assignment
    # Replace with actual student and lesson IDs
    request = TimebackImportExternalTestAssignmentResultsRequest(
        student="<student-sourced-id>",  # Replace with actual student ID
        lesson="<lesson-sourced-id>",  # Replace with actual lesson (ComponentResource) ID
        # applicationName="my-app",  # Optional
    )

    response = client.powerpath.import_external_test_assignment_results(request)

    print("External test assignment results import completed!")
    print("-" * 60)
    print(f"Lesson Type: {response.lessonType}")
    print(f"Lesson ID: {response.lessonId}")
    print(f"Tool Provider: {response.toolProvider}")
    print(f"Finalized: {response.finalized}")
    print(f"Attempt: {response.attempt}")

    if response.credentials:
        print(f"\nCredentials:")
        print(f"  Email: {response.credentials.email}")
        print(f"  Password: {response.credentials.password}")

    if response.testUrl:
        print(f"\nTest URL: {response.testUrl}")
    if response.assignmentId:
        print(f"Assignment ID: {response.assignmentId}")
    if response.testId:
        print(f"Test ID: {response.testId}")

    if response.finalized:
        print("\n✓ Test has been finalized - results are ready!")
    else:
        print("\n⏳ Test not yet finalized - check again later.")


if __name__ == "__main__":
    main()

