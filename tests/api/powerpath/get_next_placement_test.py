"""API test for get_next_placement_test endpoint.

This script can be used to test the get_next_placement_test endpoint
against the live PowerPath API.

Usage:
    python -m tests.api.powerpath.get_next_placement_test
"""

from timeback import Timeback
from timeback.models.request import TimebackGetNextPlacementTestRequest
from timeback.enums import TimebackSubject


def main():
    client = Timeback()

    # Example: Get next placement test for a student in Reading
    # Replace with actual student sourcedId
    request = TimebackGetNextPlacementTestRequest(
        student="<student-sourced-id>",  # Replace with actual student ID
        subject=TimebackSubject.READING,
    )

    response = client.powerpath.get_next_placement_test(request)

    print(f"Exhausted Tests: {response.exhaustedTests}")
    print(f"Grade Level: {response.gradeLevel}")
    print(f"Next Lesson: {response.lesson}")
    print(f"Onboarded: {response.onboarded}")
    print(f"Available Tests: {response.availableTests}")

    if response.exhaustedTests:
        print("\nStudent has completed all placement tests for this subject.")
    elif response.lesson:
        print(f"\nStudent should take placement test: {response.lesson}")
    elif response.onboarded:
        print("\nStudent has been placed (scored < 90 on last test).")
    else:
        print("\nStudent hasn't started placement tests yet.")


if __name__ == "__main__":
    main()

