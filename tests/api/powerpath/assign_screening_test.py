"""API test for assign_screening_test endpoint.

This script can be used to test the assign_screening_test endpoint
against the live PowerPath API.

Usage:
    python -m tests.api.powerpath.assign_screening_test
"""

from timeback import Timeback
from timeback.models.request import TimebackAssignScreeningTestRequest


def main():
    client = Timeback()

    # Example: Assign a Reading screening test to a user
    # Replace with actual user sourcedId
    request = TimebackAssignScreeningTestRequest(
        userId="<user-sourced-id>",  # Replace with actual user ID
        subject="Reading",  # Valid: Math, Reading, Language, Science
    )

    response = client.powerpath.assign_screening_test(request)

    print(f"Screening test assigned successfully!")
    print("-" * 60)
    print(f"NWEA Student ID: {response.nweaStudentId}")
    print(f"Session Status: {response.status}")
    print(f"Test Session ID: {response.testSessionId}")
    print(f"PIN: {response.pin}")
    print(f"Password: {response.password}")
    print()
    print("Assignment:")
    print(f"  Assigned Test Key: {response.assignment.assignedTestKey}")
    print(f"  Status: {response.assignment.status}")
    print(f"  NWEA Status: {response.assignment.nweaStatus}")


if __name__ == "__main__":
    main()

