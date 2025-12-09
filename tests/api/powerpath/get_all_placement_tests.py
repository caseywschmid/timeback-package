"""API test for get_all_placement_tests endpoint.

This script can be used to test the get_all_placement_tests endpoint
against the live PowerPath API.

Usage:
    python -m tests.api.powerpath.get_all_placement_tests
"""

from timeback import Timeback
from timeback.models.request import TimebackGetAllPlacementTestsRequest
from timeback.enums import TimebackSubject


def main():
    client = Timeback()

    # Example: Get all placement tests for a student and subject
    # Replace with actual student sourcedId
    request = TimebackGetAllPlacementTestsRequest(
        student="<student-sourced-id>",  # Replace with actual student ID
        subject=TimebackSubject.READING,
    )

    response = client.powerpath.get_all_placement_tests(request)

    print(f"Found {len(response.placementTests)} placement tests")

    for i, test in enumerate(response.placementTests):
        print(f"\nPlacement Test {i + 1}:")
        print(f"  Component Resource: {test.component_resources.get('sourcedId', 'N/A')}")
        print(f"  Resource: {test.resources.get('sourcedId', 'N/A')}")
        print(f"  Lesson Type: {test.resources_metadata.get('lessonType', 'N/A')}")
        if test.assessment_line_items:
            print(f"  Assessment Line Item: {test.assessment_line_items.get('sourcedId', 'N/A')}")
        if test.assessment_results:
            print(f"  Assessment Results: {len(test.assessment_results)} result(s)")


if __name__ == "__main__":
    main()

