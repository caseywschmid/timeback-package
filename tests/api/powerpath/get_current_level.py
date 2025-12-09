"""API test for get_current_level endpoint.

This script can be used to test the get_current_level endpoint
against the live PowerPath API.

Usage:
    python -m tests.api.powerpath.get_current_level
"""

from timeback import Timeback
from timeback.models.request import TimebackGetCurrentLevelRequest
from timeback.enums import TimebackSubject


def main():
    client = Timeback()

    # Example: Get current level for a student in Reading
    # Replace with actual student sourcedId
    request = TimebackGetCurrentLevelRequest(
        student="<student-sourced-id>",  # Replace with actual student ID
        subject=TimebackSubject.READING,
    )

    response = client.powerpath.get_current_level(request)

    print(f"Grade Level: {response.gradeLevel}")
    print(f"Onboarded: {response.onboarded}")
    print(f"Available Tests: {response.availableTests}")

    if response.onboarded:
        print("\nStudent has completed the onboarding process for this subject.")
    else:
        print("\nStudent has NOT completed the onboarding process yet.")
        if response.availableTests > 0:
            print(f"There are {response.availableTests} more placement test(s) to take.")


if __name__ == "__main__":
    main()

